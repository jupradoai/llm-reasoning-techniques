import streamlit as st
import requests
import json

st.set_page_config(
    page_title="LLM Reasoning Techniques",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 LLM Reasoning Techniques")
st.write("Demonstração de diferentes técnicas de raciocínio usando LLMs")

# Seleção da estratégia
strategy = st.sidebar.selectbox(
    "Escolha a Estratégia",
    [
        "Tool-Augmented Reasoning",
        "Chain-of-Thought",
        "Rationale Engineering",
        "In-Context Learning",
        "Finetuning Simulado",
        "Memória e Contexto",
        "Protocolo de Contexto",
        "Todas as Estratégias"
    ]
)

# Mapeamento de estratégias para endpoints
ENDPOINTS = {
    "Tool-Augmented Reasoning": "/api/tool-augmented",
    "Chain-of-Thought": "/api/chain-of-thought",
    "Rationale Engineering": "/api/rationale",
    "In-Context Learning": "/api/in-context",
    "Finetuning Simulado": "/api/finetuning",
    "Memória e Contexto": "/api/memory",
    "Protocolo de Contexto": "/api/protocol",
    "Todas as Estratégias": "/api/all"
}

# Input do usuário
user_input = st.text_area("Digite sua pergunta sobre o clima:", height=100)

if st.button("Enviar"):
    if user_input:
        try:
            # Fazer requisição para o endpoint correspondente
            response = requests.post(
                f"http://localhost:5000{ENDPOINTS[strategy]}",
                json={"query": user_input}
            )
            
            if response.status_code == 200:
                result = response.json()
                st.success("Resposta:")
                st.write(result["message"])
            else:
                st.error("Erro ao processar a requisição")
        except Exception as e:
            st.error(f"Erro: {str(e)}")
    else:
        st.warning("Por favor, digite uma pergunta") 