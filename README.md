# Chatbot-using-LLM-and-Ollama

This is a simple Streamlit-based chatbot app that uses a Large Language Model (LLM) served via Ollama and integrated with LangChain. It allows users to ask questions and get AI-generated responses in a chat-style interface. Built for fast prototyping and local experimentation.

🛠️ Features
🧠 Uses llama3.2 model via Ollama

🔗 Integrated with LangChain for streamlined LLM interaction

💬 Maintains a chat history for contextual interaction

⚡ Lightweight and fast using Streamlit UI

🧠 How it Works
Users input a question in the Streamlit app.

ChatOllama from langchain_ollama sends the prompt to the locally running LLM via Ollama.

The response is displayed and added to the session's chat history.



Chatbot-using-LLM-and-Ollama/
│
├── app.py           # Main Streamlit app
├── requirements.txt # Python dependencies (optional)
└── README.md        # Project documentation

