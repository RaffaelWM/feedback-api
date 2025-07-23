from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import openai
import json

app = FastAPI()

API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=API_KEY)

# Servir arquivos estáticos (HTML, CSS, JS) da pasta static/
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste se quiser restringir origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para servir o HTML principal
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# Modelo Pydantic para input
class TextoInput(BaseModel):
    texto: str

@app.post("/analisar")
async def analisar_texto(dados: TextoInput):
    frases = [linha.strip() for linha in dados.texto.split('\n') if linha.strip()]
    prompt = "\n".join(frases)

    system_prompt = (
        "Você é um classificador de feedbacks. Para o texto recebido, retorne uma lista em JSON contendo apenas objetos com os campos 'categoria' e 'sentimento'."
        "O sentimento deve ser um dos seguintes: Satisfeito, Neutro ou Insatisfeito."
        "Não inclua frases ou informações extras, apenas o JSON puro."

    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=200,
    )

    conteudo = response.choices[0].message.content.strip()

    # Tenta converter para JSON e retornar, senão retorna erro simples
    try:
        dados_json = json.loads(conteudo)
    except json.JSONDecodeError:
        dados_json = [{"categoria": "Erro", "sentimento": "Neutro"}]

    return {"resultado": dados_json}
