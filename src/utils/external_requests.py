import requests
from src.config import WEATHER_API_KEY


class API:
    def __init__(self):
        """
        Инициализирует класс
        """
        self.session = requests.Session()

    @staticmethod
    def get_weather_url(city):
        """
        Генерирует url включая в него необходимые параметры
        Args:
            city: Город
        Returns:

        """
        url = 'https://api.openweathermap.org/data/2.5/weather'
        url += '?units=metric'
        url += '&q=' + city
        url += '&appid=' + WEATHER_API_KEY
        return url


class GetWeatherRequest(API):
    """
    Выполняет запрос на получение текущей погоды для города
    """
    @staticmethod
    def get_weather_from_response(response):
        """
        Достает погоду из ответа
        Args:
            response: Ответ, пришедший с сервера
        Returns:

        """
        data = response.json()
        return data['main']['temp']

    def get_weather(self, city):
        """
        Делает запрос на получение погоды
        Args:
            city: Город
        Returns:

        """
        url = self.get_weather_url(city)
        response = self.session.get(url)
        if response.status_code != 200:
            response.raise_for_status()
        else:
            weather = self.get_weather_from_response(response)
            return weather


class CheckCityExisting(API):
    """
    Проверка наличия города (запросом к серверу погоды)
    """
    def check_existing(self, city):
        """
        Проверяет наличие города
        Args:
            city: Название города
        Returns:

        """
        url = self.get_weather_url(city)
        response = self.session.get(url)
        if response.status_code == 404:
            return False
        if response.status_code == 200:
            return True


