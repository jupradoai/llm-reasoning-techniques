# LLM Reasoning Techniques

Demonstração de diferentes técnicas de raciocínio usando o modelo Gemini Flash 2.0 para previsão do tempo.

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

1. Crie um arquivo `.env` na raiz do projeto:
```
GEMINI_API_KEY=sua_chave_aqui
FLASK_ENV=development
FLASK_APP=api/app.py
```

## Executando

1. Inicie a API:
```bash
python -m api.app
```

2. Em outro terminal, inicie a interface:
```bash
streamlit run frontend/app.py
```

## Técnicas de Raciocínio

### 1. Tool-Augmented Reasoning
**Objetivo**: Usar ferramentas externas (API do tempo) para enriquecer o raciocínio.
**Teste**: "Qual a temperatura máxima prevista para hoje?"
```bash
curl -X POST http://localhost:5000/api/tool-augmented -H "Content-Type: application/json" -d '{"query":"Qual a temperatura máxima prevista para hoje?"}'
```

### 2. Chain-of-Thought
**Objetivo**: Mostrar o passo a passo do raciocínio de forma explícita.
**Teste**: "Vai fazer calor e chover hoje?"
```bash
curl -X POST http://localhost:5000/api/chain-of-thought -H "Content-Type: application/json" -d '{"query":"Vai fazer calor e chover hoje?"}'
```

### 3. Rationale Engineering
**Objetivo**: Fornecer justificativas explícitas para cada conclusão.
**Teste**: "Devo levar guarda-chuva?"
```bash
curl -X POST http://localhost:5000/api/rationale -H "Content-Type: application/json" -d '{"query":"Devo levar guarda-chuva?"}'
```

### 4. In-Context Learning
**Objetivo**: Aprender com exemplos anteriores para formatar respostas.
**Teste**: "Como está o clima?"
```bash
curl -X POST http://localhost:5000/api/in-context -H "Content-Type: application/json" -d '{"query":"Como está o clima?"}'
```

### 5. Finetuning Simulado
**Objetivo**: Simular um modelo fine-tuned com regras predefinidas.
**Teste**: "Qual a previsão para hoje?"
```bash
curl -X POST http://localhost:5000/api/finetuning -H "Content-Type: application/json" -d '{"query":"Qual a previsão para hoje?"}'
```

### 6. Memória e Contexto
**Objetivo**: Manter histórico da conversa para respostas contextualizadas.
**Teste**: "E amanhã, como vai estar?"
```bash
curl -X POST http://localhost:5000/api/memory -H "Content-Type: application/json" -d '{"query":"E amanhã, como vai estar?"}'
```

### 7. Protocolo de Contexto
**Objetivo**: Seguir um formato específico de resposta com regras definidas.
**Teste**: "Me dê um resumo do tempo"
```bash
curl -X POST http://localhost:5000/api/protocol -H "Content-Type: application/json" -d '{"query":"Me dê um resumo do tempo"}'
```

### Testando Todas as Estratégias
Para ver todas as estratégias em ação:
```bash
curl -X POST http://localhost:5000/api/all -H "Content-Type: application/json" -d '{"query":"Como está o tempo hoje?"}'
```

## Dados Meteorológicos
O projeto usa a API OpenMeteo para dados meteorológicos:
- Temperatura máxima e mínima
- Probabilidade de precipitação
- Dados para Porto Alegre, São Paulo e Recife

## Interface Web
Acesse http://localhost:8501 para usar a interface Streamlit e testar todas as estratégias de forma interativa. 