import requests
from typing import Dict, Any

class WeatherAPI:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    
    @staticmethod
    def get_weather_forecast(latitude: float, longitude: float) -> Dict[str, Any]:
        """
        Obtém a previsão do tempo para uma localização específica.
        
        Args:
            latitude: Latitude da localização
            longitude: Longitude da localização
            
        Returns:
            Dict contendo os dados da previsão do tempo
        """
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_probability_max"],
            "timezone": "auto"
        }
        
        try:
            response = requests.get(WeatherAPI.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao obter previsão do tempo: {str(e)}")
    
    @staticmethod
    def get_sao_paulo_weather() -> Dict[str, Any]:
        """
        Obtém a previsão do tempo para São Paulo.
        
        Returns:
            Dict contendo os dados da previsão do tempo para São Paulo
        """
        return WeatherAPI.get_weather_forecast(-23.55, -46.63)
    
    @staticmethod
    def get_recife_weather() -> Dict[str, Any]:
        """
        Obtém a previsão do tempo para Recife.
        
        Returns:
            Dict contendo os dados da previsão do tempo para Recife
        """
        return WeatherAPI.get_weather_forecast(-8.05, -34.88)
    
    @staticmethod
    def get_porto_alegre_weather() -> Dict[str, Any]:
        """
        Obtém a previsão do tempo para Porto Alegre.
        
        Returns:
            Dict contendo os dados da previsão do tempo para Porto Alegre
        """
        return WeatherAPI.get_weather_forecast(-30.03, -51.23) 