# 🚀 Projeto Oracle Asimov

Este projeto é um **chatbot inteligente** que utiliza o modelo **DeepSeek R1** (7B) rodando localmente com **Ollama** para responder perguntas com base em uma base de dados fornecida. O chatbot é construído com **LangChain** e utiliza embeddings locais com **SentenceTransformers** para processar e buscar informações relevantes.

---

## 🌟 Funcionalidades

✅ **Chatbot Inteligente**: Responde perguntas com base em uma base de dados local.  
✅ **Modelo Local**: Utiliza o modelo **DeepSeek R1** rodando via **Ollama**.  
✅ **Busca Semântica**: Usa embeddings gerados por **SentenceTransformers** para encontrar informações relevantes.  
✅ **Fácil Configuração**: Simples de rodar localmente.

---

## 🔧 Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes requisitos instalados:

- 🐍 **Python 3.8 ou superior**
- 🖥️ **Ollama** instalado e configurado
- 🎮 **CUDA** (opcional, mas recomendado se você tiver uma GPU compatível)
- 🔗 **Git** (para clonar o repositório)

---

## 📥 Instalação

Siga os passos abaixo para configurar e rodar o projeto.

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/oraculo_asimov_copy.git
cd oraculo_asimov_copy
```

### 2️⃣ Configurar o Ambiente Virtual

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter:

```plaintext
langchain
langchain-huggingface
sentence-transformers
ollama
python-dotenv
faiss-cpu  # ou faiss-gpu se tiver uma GPU compatível
```

### 4️⃣ Configurar o Ollama e o Modelo DeepSeek R1

```bash
ollama pull deepseek-r1
```

### 5️⃣ Preparar a Base de Dados

Coloque o arquivo `knowledge_base.csv` na raiz do projeto. Esse arquivo deve conter os dados que o chatbot irá usar para responder perguntas.

### 6️⃣ Configurar Variáveis de Ambiente (Opcional)

Crie um arquivo `.env` na raiz do projeto para configurar variáveis de ambiente, se necessário:

```plaintext
OPENAI_API_KEY=your-api-key-here  # Se for usar OpenAI em vez de Ollama
```

### 7️⃣ Executar o Projeto

```bash
python oracle.py
```

O chatbot estará pronto para responder perguntas com base na base de dados fornecida.

---

## 📂 Estrutura do Projeto

```plaintext
oraculo_asimov_copy/
├── venv/                   # Ambiente virtual
├── knowledge_base.csv      # Base de dados em formato CSV
├── oracle.py               # Script principal do chatbot
├── requirements.txt        # Dependências do projeto
├── .env                    # Variáveis de ambiente (opcional)
└── README.md               # Este arquivo
```

---

## 🎯 Exemplo de Uso

```plaintext
Pergunta: Qual o preço da trilha IA?
Resposta: O preço da trilha de aplicações de IA com Python é R$ 700.
```

---

### 💡 Dicas Extras

- Para melhor desempenho, utilize **faiss-gpu** se possuir uma GPU compatível.  
- Para rodar o projeto em containers, considere usar **Docker**.  

🚀 **Agora é só testar e aproveitar!**
