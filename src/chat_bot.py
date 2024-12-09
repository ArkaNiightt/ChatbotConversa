import streamlit as st
from def_openai import retorna_resposta_modelo
from utils import ler_mensagens, salvar_mensagens, listar_conversas, desconverte_nome_mensagem, ler_mensagem_por_nome_arquivo


def pagina_principal():

    if not "mensagens" in st.session_state:
        st.session_state.mensagens = []

    mensagens = ler_mensagens(st.session_state["mensagens"])

    st.header("🤖 Chatbot com OpenAI", divider=True)

    for mensagem in mensagens:
        chat = st.chat_message(mensagem["role"])
        chat.markdown(mensagem["content"])

    prompt = st.chat_input("Digite sua mensagem...")
    if prompt:
        nova_mensagem = {"role": "user", "content": prompt}
        chat = st.chat_message(nova_mensagem["role"])
        chat.markdown(nova_mensagem["content"])
        mensagens.append(nova_mensagem)

        chat = st.chat_message("assistant")
        placeholder = chat.empty()
        resposta_completa = ""
        placeholder.markdown("▌")
        respostas = retorna_resposta_modelo(mensagens=mensagens, stream=True)
        for resposta in respostas:
            content = resposta.choices[0].delta.content
            if content is not None:
                resposta_completa += content
                placeholder.markdown(resposta_completa + "▌")
        placeholder.markdown(resposta_completa)
        nova_mensagem = {"role": "assistant", "content": resposta_completa}
        mensagens.append(nova_mensagem)

        st.session_state["mensagens"] = mensagens
        salvar_mensagens(mensagens)


def seleciona_conversa(nome_arquivo):
    if nome_arquivo == '':
        st.session_state['mensagens'] = []
    else:
        mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo)
        st.session_state['mensagens'] = mensagem

def tab_conversas(tab):

    tab.button('➕ Nova conversa',
                on_click=seleciona_conversa,
                args=('', ),
                use_container_width=True)
    tab.markdown('')
    conversas = listar_conversas()
    for nome_arquivo in conversas:
        nome_mensagem = desconverte_nome_mensagem(nome_arquivo).capitalize()
        if len(nome_mensagem) == 30:
            nome_mensagem += '...'
        tab.button(nome_mensagem,
            on_click=seleciona_conversa,
            args=(nome_arquivo, ),
            use_container_width=True)


def main():
    pagina_principal()
    tab1, tab2 = st.sidebar.tabs(["Conversas", "Configurações"])
    tab_conversas(tab1)


if __name__ == "__main__":
    main()
