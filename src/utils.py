import re
from unidecode import unidecode
from pathlib import Path
import pickle

from PIL import Image
import os
import requests
from io import BytesIO
import requests

import streamlit as st

BANCO_DADOS_PASTA = Path(__file__).parent / "banco_dados_mensagens"
IMAGENS_PASTA = Path(__file__).parent / "images"
BANCO_DADOS_PASTA.mkdir(exist_ok=True)
CACHE_DESCONVERSAO = {}


def load_avatar(image_source):
    """
    Carrega uma imagem de avatar a partir de um caminho local ou URL.

    :param image_source: String contendo o caminho local ou URL da imagem
    :return: Objeto PIL.Image ou None se a imagem não puder ser carregada
    """
    try:
        if image_source.startswith(("http://", "https://")):
            # Se for uma URL
            response = requests.get(image_source)
            img = Image.open(BytesIO(response.content))
        else:
            # Se for um caminho local
            local_path = IMAGENS_PASTA / image_source
            if local_path.exists():
                img = Image.open(local_path)
            else:
                raise FileNotFoundError(
                    f"Arquivo não encontrado: {local_path}")

        # Redimensiona a imagem para um tamanho padrão (opcional)
        img = img.resize((128, 128))
        return img
    except Exception as e:
        st.warning(f"Não foi possível carregar a imagem do avatar: {e}")
        return None


def converte_nome_mensagem(nome_mensagem):
    nome_arquivo = unidecode(nome_mensagem)
    nome_arquivo = re.sub(r"\W+", "", nome_arquivo).lower()
    return nome_arquivo


def desconverte_nome_mensagem(nome_arquivo):
    if not nome_arquivo in CACHE_DESCONVERSAO:
        nome_mensagem = ler_mensagem_por_nome_arquivo(
            nome_arquivo, key="nome_mensagem")
        CACHE_DESCONVERSAO[nome_arquivo] = nome_mensagem
    return CACHE_DESCONVERSAO[nome_arquivo]


def retorna_nome_mensagem(mensagens):
    nome_mensagem = ""

    for mensagem in mensagens:
        if mensagem["role"] == "user":
            nome_mensagem += mensagem["content"][:30]
            break
    return nome_mensagem


def salvar_mensagens(mensagens):
    if len(mensagens) == 0:
        return False
    nome_mensagem = retorna_nome_mensagem(mensagens)
    nome_arquivo = converte_nome_mensagem(nome_mensagem)
    arquivo_salvar = {"nome_mensagem": nome_mensagem,
                      "nome_arquivo": nome_arquivo, "mensagem": mensagens}
    with open(BANCO_DADOS_PASTA / nome_arquivo, "wb") as file:
        pickle.dump(arquivo_salvar, file)


def ler_mensagens(mensagens, key="mensagem"):
    if len(mensagens) == 0:
        return []
    nome_mensagem = retorna_nome_mensagem(mensagens)
    nome_arquivo = converte_nome_mensagem(nome_mensagem)
    with open(BANCO_DADOS_PASTA / nome_arquivo, "rb") as file:
        mensagens = pickle.load(file)
    return mensagens[key]


def ler_mensagem_por_nome_arquivo(nome_arquivo, key="mensagem"):
    with open(BANCO_DADOS_PASTA / nome_arquivo, "rb") as file:
        mensagens = pickle.load(file)
    return mensagens[key]


def listar_conversas():
    conversas = list(BANCO_DADOS_PASTA.glob("*"))
    conversas = sorted(
        conversas, key=lambda item: item.stat().st_mtime_ns, reverse=True)
    return [c.stem for c in conversas]
