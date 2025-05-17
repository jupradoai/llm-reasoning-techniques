from flask import Flask, request, jsonify
from decouple import config
from api.utils.gemini_client import GeminiClient
from api.utils.weather_api import WeatherAPI
import os

app = Flask(__name__)

# Configuração
gemini_client = GeminiClient()
weather_api = WeatherAPI()

# Histórico de conversas (simplificado - em produção usar banco de dados)
conversation_history = []

@app.route('/api/tool-augmented', methods=['POST'])
def tool_augmented():
    data = request.json
    query = data.get('query')
    
    # Obtém dados do tempo de Porto Alegre
    weather_data = weather_api.get_porto_alegre_weather()
    
    # Gera resposta usando Tool-Augmented Reasoning
    response = gemini_client.tool_augmented_reasoning(query, weather_data)
    
    return jsonify({"message": response})

@app.route('/api/chain-of-thought', methods=['POST'])
def chain_of_thought():
    data = request.json
    query = data.get('query')
    
    weather_data = weather_api.get_porto_alegre_weather()
    response = gemini_client.chain_of_thought(query, weather_data)
    
    return jsonify({"message": response})

@app.route('/api/rationale', methods=['POST'])
def rationale():
    data = request.json
    query = data.get('query')
    
    weather_data = weather_api.get_porto_alegre_weather()
    response = gemini_client.rationale_engineering(query, weather_data)
    
    return jsonify({"message": response})

@app.route('/api/in-context', methods=['POST'])
def in_context():
    data = request.json
    query = data.get('query')
    
    # Exemplos para In-Context Learning
    examples = [
        {
            "query": "Vai fazer calor hoje?",
            "data": {"temperature_2m_max": 32},
            "response": "Sim, vai fazer calor com máxima de 32°C."
        },
        {
            "query": "Vai chover?",
            "data": {"precipitation_probability_max": 80},
            "response": "Há uma alta probabilidade de chuva (80%)."
        }
    ]
    
    weather_data = weather_api.get_porto_alegre_weather()
    response = gemini_client.in_context_learning(query, weather_data, examples)
    
    return jsonify({"message": response})

@app.route('/api/finetuning', methods=['POST'])
def finetuning():
    data = request.json
    query = data.get('query')
    
    weather_data = weather_api.get_porto_alegre_weather()
    response = gemini_client.finetuning_simulado(query, weather_data)
    
    return jsonify({"message": response})

@app.route('/api/memory', methods=['POST'])
def memory():
    data = request.json
    query = data.get('query')
    
    # Adiciona a nova consulta ao histórico
    conversation_history.append({
        "role": "user",
        "content": query
    })
    
    weather_data = weather_api.get_porto_alegre_weather()
    response = gemini_client.memory_and_context(query, weather_data, conversation_history)
    
    # Adiciona a resposta ao histórico
    conversation_history.append({
        "role": "assistant",
        "content": response
    })
    
    return jsonify({"message": response})

@app.route('/api/protocol', methods=['POST'])
def protocol():
    data = request.json
    query = data.get('query')
    
    # Protocolo de exemplo
    protocol = {
        "format": "json",
        "rules": [
            "Sempre inclua temperatura máxima e mínima",
            "Indique probabilidade de chuva em porcentagem"
        ],
        "constraints": [
            "Resposta deve ser estruturada",
            "Use unidades métricas (°C)"
        ]
    }
    
    weather_data = weather_api.get_porto_alegre_weather()
    response = gemini_client.protocol_context(query, weather_data, protocol)
    
    return jsonify({"message": response})

@app.route('/api/all', methods=['POST'])
def all_strategies():
    data = request.json
    query = data.get('query')
    weather_data = weather_api.get_porto_alegre_weather()
    
    # Combina todas as estratégias
    responses = {
        "tool_augmented": gemini_client.tool_augmented_reasoning(query, weather_data),
        "chain_of_thought": gemini_client.chain_of_thought(query, weather_data),
        "rationale": gemini_client.rationale_engineering(query, weather_data),
        "in_context": gemini_client.in_context_learning(query, weather_data, []),
        "finetuning": gemini_client.finetuning_simulado(query, weather_data),
        "memory": gemini_client.memory_and_context(query, weather_data, conversation_history),
        "protocol": gemini_client.protocol_context(query, weather_data, {})
    }
    
    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True) 