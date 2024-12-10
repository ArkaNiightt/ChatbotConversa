<p align="center">
    <img src="src\images\projeto.jpeg" align="center" width="100%">
</p>
<p align="center"><h1 align="center">CHATBOTCONVERSA</h1></p>
<p align="center">
    <em>Revolucionando as Conversas, Um Bot de Cada Vez!</em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/last-commit/ArkaNiightt/ChatbotConversa?style=default&logo=git&logoColor=white&color=3600ff" alt="último-commit">
    <img src="https://img.shields.io/github/languages/top/ArkaNiightt/ChatbotConversa?style=default&color=3600ff" alt="linguagem-principal-repo">
    <img src="https://img.shields.io/github/languages/count/ArkaNiightt/ChatbotConversa?style=default&color=3600ff" alt="contagem-linguagens-repo">
</p>
<p align="center"><!-- opção padrão, sem badges de dependência. -->
</p>
<p align="center">
    <!-- opção padrão, sem badges de dependência. -->
</p>
<br>

## 🔗 Índice

- [📍 Visão Geral](#-visão-geral)
- [👾 Funcionalidades](#-funcionalidades)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
  - [📂 Índice do Projeto](#-índice-do-projeto)
- [🚀 Começando](#-começando)
  - [☑️ Pré-requisitos](#️-pré-requisitos)
  - [⚙️ Instalação](#️-instalação)
  - [🤖 Uso](#️-uso)
  - [🧪 Testes](#️-testes)
- [📌 Roteiro do Projeto](#-roteiro-do-projeto)
- [🔰 Contribuindo](#-contribuindo)
- [🎗 Licença](#-licença)
- [🙌 Agradecimentos](#-agradecimentos)

---

## 📍 Visão Geral

ChatbotConversa é um projeto inovador de código aberto que revoluciona a comunicação digital ao aproveitar a tecnologia avançada da OpenAI. Este aplicativo de chatbot gerencia interações com usuários de forma eficiente, entregando simulações de conversas dinâmicas. Com funcionalidades como gerenciamento de conversas, configurações de configuração e manipulação de imagens, oferece uma experiência fluida para os usuários. Ideal para empresas que buscam aumentar o engajamento dos clientes ou indivíduos que desejam explorar conversas alimentadas por IA.

---

## 👾 Funcionalidades

|      | Funcionalidade    | Resumo       |
| :--- | :---:             | :---          |
| ⚙️  | **Arquitetura**   | <ul><li>Desenhado com uma abordagem modular, separando a funcionalidade principal do chatbot (`chat_bot.py`), funções utilitárias (`utils.py`) e interações com a API OpenAI (`utils_openai.py`).</li><li>Emprega um script driver para inicialização da aplicação e gerenciamento de interação com o usuário.</li><li>Utiliza módulos utilitários para manipulação de imagens, gerenciamento de dados de mensagens e respostas da API OpenAI.</li></ul> |
| 🔩 | **Qualidade do Código** | <ul><li>Escrito em `Python`, o código é limpo, conciso e fácil de entender.</li><li>Design modular melhora a legibilidade e manutenibilidade.</li><li>Uso eficaz de funções utilitárias para tarefas específicas, promovendo reutilização de código.</li></ul> |
| 📄 | **Documentação** | <ul><li>Idioma principal usado é `Python` com 3 arquivos Python no código base.</li><li>Sem documentação específica sobre gerenciadores de pacotes, containers ou uso de comandos.</li><li>Comentários no código fornecem insights sobre a funcionalidade dos módulos individuais.</li></ul> |
| 🔌 | **Integrações**  | <ul><li>Integra com a API OpenAI para simulações de conversas dinâmicas.</li><li>Usa caminhos locais ou URLs para carregar imagens de avatar.</li><li>Sem outras integrações externas identificadas.</li></ul> |
| 🧩 | **Modularidade**  | <ul><li>O código base é dividido em módulos distintos para funcionalidades específicas.</li><li>Funções utilitárias são separadas em seu próprio módulo (`utils.py`).</li><li>Interações com a API OpenAI são tratadas em um módulo separado (`utils_openai.py`).</li></ul> |
| 🧪 | **Testes**       | <ul><li>Sem comandos de teste específicos ou framework de testes identificado no projeto.</li><li>Testes podem ser realizados manualmente devido à natureza interativa do projeto.</li></ul> |
| ⚡️  | **Desempenho**   | <ul><li>O desempenho depende amplamente da eficiência da API OpenAI e do interpretador Python.</li><li>Sem otimizações específicas de desempenho ou benchmarks identificados.</li></ul> |
| 🛡️ | **Segurança**      | <ul><li>Medidas de segurança não são mencionadas explicitamente no projeto.</li><li>Depende da segurança fornecida pela API OpenAI para simulações de conversas.</li></ul> |
| 📦 | **Dependências**  | <ul><li>O projeto depende de `Python` como a principal linguagem de programação.</li><li>Sem outras dependências específicas ou gerenciadores de pacotes mencionados.</li></ul> |
| 🚀 | **Escalabilidade**   | <ul><li>A escalabilidade depende das capacidades da API OpenAI e do interpretador Python.</li><li>Design modular permite fácil adição de novas funcionalidades ou integrações.</li></ul> |

---

## 📁 Estrutura do Projeto

```sh
└── ChatbotConversa/
    └── src
        ├── chat_bot.py
        ├── images
        │   ├── assistant_image.png
        │   └── user_image.png
        ├── utils.py
        └── utils_openai.py
```

### 📂 Índice do Projeto
<details open>
    <summary><b><code>CHATBOTCONVERSA/</code></b></summary>
    <details> <!-- __root__ Submódulo -->
        <summary><b>__root__</b></summary>
        <blockquote>
            <table>
            </table>
        </blockquote>
    </details>
    <details> <!-- src Submódulo -->
        <summary><b>src</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/ArkaNiightt/ChatbotConversa/blob/master/src/chat_bot.py'>chat_bot.py</a></b></td>
                <td>- O script 'chat_bot.py' serve como o motor principal para uma aplicação de chatbot alimentada pela OpenAI<br>- Ele inicializa a aplicação, gerencia interações com o usuário e lida com as respostas do chatbot<br>- O script também fornece funcionalidades para gerenciamento de conversas e configurações de configuração, incluindo seleção de modelo e entrada de chave API.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/ArkaNiightt/ChatbotConversa/blob/master/src/utils.py'>utils.py</a></b></td>
                <td>- O módulo 'utils.py' no diretório src fornece um conjunto de funções utilitárias para manipulação de imagens e gerenciamento de dados de mensagens<br>- Inclui funcionalidades para carregar imagens de avatar de caminhos locais ou URLs, converter e reverter nomes de mensagens, salvar e ler mensagens e listar conversas<br>- Este módulo contribui significativamente para o gerenciamento geral de dados e interação com o usuário dentro do projeto.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/ArkaNiightt/ChatbotConversa/blob/master/src/utils_openai.py'>utils_openai.py</a></b></td>
                <td>- Utilizando a API OpenAI, src/utils_openai.py serve como um módulo utilitário que gera respostas do modelo GPT-4o-mini<br>- Ele recebe mensagens como entrada, processa-as e retorna a resposta do modelo<br>- Esta funcionalidade é essencial para os aspectos interativos do projeto, permitindo simulações de conversas dinâmicas.</td>
            </tr>
            </table>
        </blockquote>
    </details>
</details>

---

## 🚀 Começando

### ☑️ Pré-requisitos

Antes de começar com o ChatbotConversa, certifique-se de que seu ambiente de runtime atende aos seguintes requisitos:

- **Linguagem de Programação:** Python

### ⚙️ Instalação

Instale o ChatbotConversa usando um dos seguintes métodos:

**Construir a partir do código-fonte:**

1. Clone o repositório ChatbotConversa:
```sh
❯ git clone https://github.com/ArkaNiightt/ChatbotConversa
```

2. Navegue até o diretório do projeto:
```sh
❯ cd ChatbotConversa
```

3. Instale as dependências do projeto:

echo 'INSERIR-COMANDO-DE-INSTALAÇÃO-AQUI'

### 🤖 Uso
Execute o ChatbotConversa usando o seguinte comando:
echo 'INSERIR-COMANDO-DE-EXECUÇÃO-AQUI'

### 🧪 Testes
Execute a suíte de testes usando o seguinte comando:
echo 'INSERIR-COMANDO-DE-TREINAMENTO-AQUI'

---

## 📌 Roteiro do Projeto

- [X] **`Tarefa 1`**: <strike>Implementar a primeira funcionalidade.</strike>
- [ ] **`Tarefa 2`**: Implementar a segunda funcionalidade.
- [ ] **`Tarefa 3`**: Implementar a terceira funcionalidade.

---

## 🔰 Contribuindo

- **💬 [Participe das Discussões](https://github.com/ArkaNiightt/ChatbotConversa/discussions)**: Compartilhe suas ideias, forneça feedback ou faça perguntas.
- **🐛 [Reportar Problemas](https://github.com/ArkaNiightt/ChatbotConversa/issues)**: Relate bugs encontrados ou registre solicitações de funcionalidades para o projeto `ChatbotConversa`.
- **💡 [Enviar Pull Requests](https://github.com/ArkaNiightt/ChatbotConversa/blob/main/CONTRIBUTING.md)**: Revise PRs abertos e envie seus próprios PRs.

<details closed>
<summary>Diretrizes de Contribuição</summary>

1. **Fork o Repositório**: Comece fazendo um fork do repositório do projeto para sua conta no GitHub.
2. **Clone Localmente**: Clone o repositório forked na sua máquina local usando um cliente Git.
   ```sh
   git clone https://github.com/ArkaNiightt/ChatbotConversa
   ```
3. **Crie um Novo Branch**: Sempre trabalhe em um novo branch, dando a ele um nome descritivo.
   ```sh
   git checkout -b nova-funcionalidade-x
   ```
4. **Faça Suas Alterações**: Desenvolva e teste suas alterações localmente.
5. **Commit Suas Alterações**: Faça commit com uma mensagem clara descrevendo suas atualizações.
   ```sh
   git commit -m 'Implementada a nova funcionalidade x.'
   ```
6. **Faça Push para o GitHub**: Envie as alterações para seu repositório forked.
   ```sh
   git push origin nova-funcionalidade-x
   ```
7. **Envie um Pull Request**: Crie um PR contra o repositório original do projeto. Descreva claramente as mudanças e suas motivações.
8. **Revisão**: Uma vez que seu PR seja revisado e aprovado, ele será mesclado no branch principal. Parabéns pela sua contribuição!
</details>

<details open>
<summary>Gráfico de Contribuidores</summary>
<br>
<p align="left">
   <a href="https://github.com{/ArkaNiightt/ChatbotConversa/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ArkaNiightt/ChatbotConversa">
   </a>
</p>
</details>

---
