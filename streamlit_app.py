import streamlit as st
import requests

st.title("📄 Smart Doc Assistant")

"""
Olá! Eu sou o Smart Doc Assistant, seu assistente inteligente para consultas e resumos de documentos. 
Envie suas perguntas e eu ajudo a encontrar as respostas nos documentos com rapidez e precisão.
"""

# Inicializar o estado da sessão para armazenar o histórico de conversas
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Olá! Como posso ajudar com seus documentos hoje?"}]

# Exibir mensagens de chat do histórico da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceitar entrada do usuário
if prompt := st.chat_input("Digite uma mensagem para o assistente:"):
    # Adicionar a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Enviar solicitação para a API do Langflow atualizada
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer sk-0EDDDAlNjRscbzqGZtDVsalsBvW52niFZ_2qfpQn-Xk"
        }
        data = {
            "input_value": prompt,
            "output_type": "chat",
            "input_type": "chat",
            "tweaks": {
                "Pinecone-QMd60": {},
                "SplitText-DWvkT": {},
                "Pinecone-1lgJh": {},
                "ChatInput-TYjSN": {},
                "OpenAIEmbeddings-37WE4": {},
                "ParseData-x968k": {},
                "Prompt-qc1TI": {},
                "OpenAIModel-bygbe": {},
                "ChatOutput-TRRVE": {},
                "FirecrawlScrapeApi-Uptho": {},
                "OpenAIEmbeddings-i3XBn": {},
                "File-qpDFS": {}
            }
        }

        response = requests.post(
            "https://langflowailangflowlatest-production-74ad.up.railway.app/api/v1/run/45e1b28f-4574-43c7-99f9-98a1b248d423?stream=false",
            headers=headers,
            json=data
        )
        response_data = response.json()

        # Extrair a resposta do assistente
        assistant_message = response_data["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]

        # Exibir mensagem do assistente no chat
        with st.chat_message("assistant"):
            st.markdown(assistant_message)

        # Adicionar mensagem do assistente ao histórico de conversas
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    except Exception as e:
        st.error(f"Erro: {e}")
