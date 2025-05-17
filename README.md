# LLM Reasoning Techniques

Este projeto demonstra diferentes técnicas de raciocínio usando Large Language Models (LLMs), especificamente o Gemini Flash 2.0.

## Técnicas Implementadas

1. Tool-Augmented Reasoning
2. Chain-of-Thought
3. Justificativas (Rationale Engineering)
4. In-Context Learning
5. Finetuning Simulado
6. Memória e Contexto
7. Protocolo de Contexto

## Estrutura do Projeto

```
llm-reasoning-techniques/
├── api/                    # Endpoints Flask
├── strategies/            # Implementações das estratégias
│   ├── tool_augmented/
│   ├── chain_of_thought/
│   ├── rationale/
│   ├── in_context/
│   ├── finetuning/
│   ├── memory/
│   └── protocol/
├── frontend/             # Interface Streamlit
├── tests/               # Testes unitários
└── utils/              # Funções auxiliares
```

## Configuração

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
- Crie um arquivo `.env` na raiz do projeto
- Adicione sua chave API do Gemini:
```
GEMINI_API_KEY=sua_chave_aqui
```

## Executando o Projeto

1. Inicie o servidor Flask:
```bash
python api/app.py
```

2. Inicie a interface Streamlit:
```bash
streamlit run frontend/app.py
```

## API OpenMeteo

O projeto utiliza a API OpenMeteo para dados meteorológicos:
```
https://api.open-meteo.com/v1/forecast
```

## Endpoints

- `/api/tool-augmented`: Testes de Tool-Augmented Reasoning
- `/api/chain-of-thought`: Testes de Chain-of-Thought
- `/api/rationale`: Testes de Rationale Engineering
- `/api/in-context`: Testes de In-Context Learning
- `/api/finetuning`: Testes de Finetuning Simulado
- `/api/memory`: Testes de Memória e Contexto
- `/api/protocol`: Testes de Protocolo de Contexto
- `/api/all`: Endpoint combinando todas as estratégias 