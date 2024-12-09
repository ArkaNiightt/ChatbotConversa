import re
from unidecode import unidecode
from pathlib import Path
import pickle

BANCO_DADOS_PASTA = Path(__file__).parent / "banco_dados_mensagens"
BANCO_DADOS_PASTA.mkdir(exist_ok=True)
CACHE_DESCONVERSAO = {}


def converte_nome_mensagem(nome_mensagem):
    nome_arquivo = unidecode(nome_mensagem)
    nome_arquivo = re.sub(r"\W+", "", nome_arquivo).lower()
    return nome_arquivo


def desconverte_nome_mensagem(nome_arquivo):
    if not nome_arquivo in CACHE_DESCONVERSAO:
        nome_mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo, key="nome_mensagem")
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
    conversas = sorted(conversas, key=lambda item: item.stat().st_mtime_ns, reverse=True)
    return [c.stem for c in conversas]