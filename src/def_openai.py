import openai
import streamlit as st


def retorna_resposta_modelo(mensagens, api_key=st.secrets["OPENAI_API_KEY"], modelo="gpt-4o-mini", temperatura=0.5, stream=False):
    client = openai.Client(api_key=api_key)
    response = client.chat.completions.create(
        messages=mensagens,
        model="gpt-4o-mini",
        temperature=0.5,
        stream=stream
    )
    return response
