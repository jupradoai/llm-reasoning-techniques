import google.generativeai as genai
from decouple import config
from typing import Dict, Any, List

class GeminiClient:
    def __init__(self):
        """Inicializa o cliente Gemini com as configurações necessárias."""
        self.api_key = config('GEMINI_API_KEY')
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
    def tool_augmented_reasoning(self, query: str, weather_data: Dict[str, Any]) -> str:
        """
        Implementa o raciocínio aumentado por ferramentas.
        Usa a API do tempo como ferramenta externa.
        """
        prompt = f"""
        Você está usando a estratégia Tool-Augmented Reasoning.
        Dados meteorológicos disponíveis: {weather_data}
        
        Consulta do usuário: {query}
        
        Use os dados meteorológicos para responder à consulta de forma precisa.
        Explique como você está usando os dados para chegar à conclusão.
        """
        return self._generate_response(prompt)
    
    def chain_of_thought(self, query: str, weather_data: Dict[str, Any]) -> str:
        """
        Implementa o raciocínio em cadeia de pensamento.
        Quebra o raciocínio em etapas explícitas.
        """
        prompt = f"""
        Você está usando a estratégia Chain-of-Thought.
        Dados meteorológicos: {weather_data}
        
        Consulta: {query}
        
        Vamos resolver isso passo a passo:
        1. Primeiro, identifique os dados relevantes
        2. Depois, analise cada informação
        3. Por fim, chegue a uma conclusão
        
        Mostre cada passo do seu raciocínio.
        """
        return self._generate_response(prompt)
    
    def rationale_engineering(self, query: str, weather_data: Dict[str, Any]) -> str:
        """
        Implementa o raciocínio com justificativas explícitas.
        """
        prompt = f"""
        Você está usando a estratégia Rationale Engineering.
        Dados meteorológicos: {weather_data}
        
        Consulta: {query}
        
        Forneça uma resposta estruturada:
        1. Dados considerados:
           - Liste os dados relevantes
        2. Justificativa:
           - Explique por que esses dados são importantes
        3. Conclusão:
           - Apresente a resposta final com base nas justificativas
        """
        return self._generate_response(prompt)
    
    def in_context_learning(self, query: str, weather_data: Dict[str, Any], examples: List[Dict]) -> str:
        """
        Implementa o aprendizado em contexto com exemplos.
        """
        examples_text = "\n".join([
            f"Exemplo {i+1}:\n" +
            f"Pergunta: {ex['query']}\n" +
            f"Dados: {ex['data']}\n" +
            f"Resposta: {ex['response']}"
            for i, ex in enumerate(examples)
        ])
        
        prompt = f"""
        Você está usando a estratégia In-Context Learning.
        
        Exemplos anteriores:
        {examples_text}
        
        Dados atuais: {weather_data}
        Nova consulta: {query}
        
        Use os exemplos acima como referência para formatar sua resposta.
        """
        return self._generate_response(prompt)
    
    def finetuning_simulado(self, query: str, weather_data: Dict[str, Any]) -> str:
        """
        Simula um modelo fine-tuned com mapeamentos específicos.
        """
        prompt = f"""
        Você está usando a estratégia Finetuning Simulado.
        
        Mapeamentos conhecidos:
        - Se temperatura > 30°C: "Vai fazer muito calor"
        - Se temperatura < 15°C: "Vai fazer frio"
        - Se probabilidade de chuva > 70%: "Alta chance de chuva"
        
        Dados atuais: {weather_data}
        Consulta: {query}
        
        Use os mapeamentos para gerar uma resposta apropriada.
        """
        return self._generate_response(prompt)
    
    def memory_and_context(self, query: str, weather_data: Dict[str, Any], conversation_history: List[Dict]) -> str:
        """
        Implementa raciocínio com memória e contexto.
        """
        history_text = "\n".join([
            f"{msg['role']}: {msg['content']}"
            for msg in conversation_history
        ])
        
        prompt = f"""
        Você está usando a estratégia Memory and Context.
        
        Histórico da conversa:
        {history_text}
        
        Dados atuais: {weather_data}
        Nova consulta: {query}
        
        Use o histórico da conversa para contextualizar sua resposta.
        """
        return self._generate_response(prompt)
    
    def protocol_context(self, query: str, weather_data: Dict[str, Any], protocol: Dict[str, Any]) -> str:
        """
        Implementa raciocínio baseado em protocolo.
        """
        prompt = f"""
        Você está usando a estratégia Protocol Context.
        
        Protocolo atual:
        - Formato: {protocol.get('format', 'padrão')}
        - Regras: {protocol.get('rules', [])}
        - Restrições: {protocol.get('constraints', [])}
        
        Dados: {weather_data}
        Consulta: {query}
        
        Siga o protocolo especificado ao gerar sua resposta.
        """
        return self._generate_response(prompt)
    
    def _generate_response(self, prompt: str) -> str:
        """
        Método interno para gerar respostas usando o Gemini Flash 2.0
        """
        try:
            # Gerando resposta usando o modelo Gemini
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=1024,
                    top_p=0.8,
                    top_k=40
                )
            )
            
            return response.text
            
        except Exception as e:
            return f"Erro ao gerar resposta: {str(e)}" 