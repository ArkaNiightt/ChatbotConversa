import streamlit as st
from utils_openai import retorna_resposta_modelo
from utils import ler_mensagens, salvar_mensagens, listar_conversas, desconverte_nome_mensagem, ler_mensagem_por_nome_arquivo, load_avatar


def initial():
    st.set_page_config(
        page_title="Chatbot com OpenAI",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    if not "mensagens" in st.session_state:
        st.session_state["mensagens"] = []
    if not "conversa_atual" in st.session_state:
        st.session_state["conversa_atual"] = ""
    if not "modelo" in st.session_state:
        st.session_state["modelo"] = "gpt-4o-mini"
    if not "api_key" in st.session_state:
        st.session_state["api_key"] = st.secrets["OPENAI_API_KEY"]


def pagina_principal():

    mensagens = ler_mensagens(st.session_state["mensagens"])

    st.header("🤖 Chatbot com OpenAI", divider=True,
              help="Converse com um assistente inteligente alimentado por OpenAI")

    for mensagem in mensagens:
        chat = st.chat_message(mensagem["role"])
        chat.markdown(mensagem["content"])

    prompt = st.chat_input("Digite sua mensagem...")
    if prompt:
        if st.session_state["api_key"] == "":
            st.error(
                "Por favor, insira sua API Key nas configurações para continuar.", icon="❌")
        else:
            try:
                nova_mensagem = {"role": "user", "content": prompt}
                chat = st.chat_message(
                    nova_mensagem["role"], avatar=load_avatar("user_image.png"))
                chat.markdown(nova_mensagem["content"])
                mensagens.append(nova_mensagem)

                chat = st.chat_message(
                    "assistant", avatar=load_avatar("assistant_image.png"))
                placeholder = chat.empty()
                resposta_completa = ""
                placeholder.markdown("▌")
                respostas = retorna_resposta_modelo(
                    mensagens=mensagens, api_key=st.session_state["api_key"], modelo=st.session_state["modelo"], stream=True)
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
            except:
                st.error(
                    "Não foi possível se conectar ao servidor da OpenAI. Por favor, tente novamente mais tarde.", icon="❌")


def seleciona_conversa(nome_arquivo):
    if nome_arquivo == '':
        st.session_state['mensagens'] = []
    else:
        mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo)
        st.session_state['mensagens'] = mensagem
    st.session_state['conversa_atual'] = nome_arquivo


def tab_conversas(tab):

    tab.button('➕ Nova conversa',
               on_click=seleciona_conversa,
               args=('', ),
               use_container_width=True)
    tab.markdown('')
    conversas = listar_conversas()
    for nome_arquivo in conversas:
        nome_mensagem = desconverte_nome_mensagem(nome_arquivo).capitalize()
        if len(nome_mensagem) >= 30:
            nome_mensagem += '...'
        tab.button(nome_mensagem,
                   on_click=seleciona_conversa,
                   args=(nome_arquivo, ),
                   disabled=nome_arquivo == st.session_state['conversa_atual'],
                   use_container_width=True)


def tab_configuracoes(tab: st):
    modelo_escolhido = tab.selectbox(
        "Selecione o modelo", ["gpt-3.5-turbo", "gpt-4o", "gpt-4o-mini"])
    st.session_state["modelo"] = modelo_escolhido
    chave = tab.text_input("API Key", type="password",
                           label_visibility="hidden", placeholder="Insira sua API Key")
    if chave != st.session_state["api_key"]:
        st.session_state["api_key"] = chave
        tab.success("API Key atualizada com sucesso!", icon="🔑")


def main():
    initial()
    pagina_principal()
    tab1, tab2 = st.sidebar.tabs(["Conversas", "Configurações"])
    tab_conversas(tab1)
    tab_configuracoes(tab2)


if __name__ == "__main__":
    main()
