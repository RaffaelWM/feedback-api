# 🧠 Analisador de Feedback / Feedback Analyzer

Este projeto é uma aplicação web simples para análise de sentimentos em feedbacks, construída com **FastAPI** no backend e uma interface frontend em HTML/CSS/JS. Utiliza a **API da OpenAI** para classificar sentimentos como **Satisfeito**, **Insatisfeito** e **Neutro**.

This project is a simple web application for sentiment analysis on feedbacks, built using **FastAPI** on the backend and a HTML/CSS/JS frontend. It uses **OpenAI's API** to classify sentiments into categories like **Satisfied**, **Unsatisfied**, and **Neutral**.

---

## 🚀 Funcionalidades / Features

- Envio de texto de feedback pelo frontend  
- Classificação de sentimentos via OpenAI GPT-3.5-turbo  
- Visualização do histórico de feedbacks analisados  
- Limite de 150 caracteres por feedback  
- Feedback visual no botão durante o processo  

- Send feedback text from the frontend  
- Sentiment classification via OpenAI GPT-3.5-turbo  
- View analyzed feedback history  
- Character limit (150) enforced  
- Visual feedback on the button during request  

---

## 🛠️ Tecnologias Utilizadas / Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) — Backend Python moderno e rápido  
- [OpenAI API](https://platform.openai.com/) — Inteligência artificial para NLP  
- HTML5, CSS3, JavaScript — Frontend  
- Uvicorn — Servidor ASGI para FastAPI  

- [FastAPI](https://fastapi.tiangolo.com/) — Modern, high-performance Python backend  
- [OpenAI API](https://platform.openai.com/) — AI service for NLP  
- HTML5, CSS3, JavaScript — Frontend  
- Uvicorn — ASGI server for FastAPI  

---

## ⚙️ Como Rodar Localmente / How to Run Locally

1. Clone o repositório / Clone the repository

```bash
git clone https://github.com/RaffaelWM/feedback-api.git
cd feedback-api
```

2. Crie um ambiente virtual / Create a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências / Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure a chave da OpenAI / Set your OpenAI API key

Crie um arquivo `.env` com o conteúdo:  
Create a `.env` file with:

```env
OPENAI_API_KEY=sua_chave_aqui / your_api_key_here
```

5. Inicie o servidor / Start the server

```bash
uvicorn main:app --reload
```

Acesse / Access: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker

```bash
docker build -t feedback-api .
docker run -p 8000:8000 feedback-api
```

---

## 📁 Estrutura / Project Structure

```
.
├── main.py              # Backend FastAPI / FastAPI backend
├── requirements.txt     # Dependências / Dependencies
├── Dockerfile           # Docker config
└── static/
    └── index.html       # Frontend HTML/CSS/JS
```

---

## 🧪 Como Usar / How to Use

1. Digite um feedback (máx. 150 caracteres)  
2. Clique em "Analisar"  
3. Veja a classificação e histórico

1. Enter feedback (max 150 characters)  
2. Click "Analyze"  
3. View the classification and history

---

## 👨‍💻 Autor / Author

Desenvolvido por / Developed by  
**Raffael Wustemberg**  
[LinkedIn](https://www.linkedin.com/in/raffaelwm/)  
