import logging

import requests

from Datasource.TestDataModels import RewardCategory, Reward
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def __get_headers(self, should_include_token=True):
        headers = {
            "User-Agent": "Skor/12 iOS | Simulator | 17.2 | 2.2",
            "Content-Type": "application/json"
        }
        if should_include_token and self.token:
            headers["Authorization"] = f"Token {self.token}"
        return headers

    def __request_data(self, url):
        try:
            response = requests.get(
                url,
                headers=self.__get_headers()
            )
            response.raise_for_status()  # Raise an error for non-2xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            log.logger.error(f"Error fetching data from {url}: {e}")
            return None

    def __validate_token(self):
        if not self.token:
            raise ValueError("Token not available. Please log in first.")

    def login(self, username, password):
        login_url = f"{self.base_url}/profiles/api/token-auth/"
        data = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(
                login_url,
                headers=self.__get_headers(should_include_token=False),
                json=data
            )
            response.raise_for_status()  # Raise an error for non-2xx status codes
            token_data = response.json()
            self.token = token_data.get("token")
        except requests.exceptions.RequestException as e:
            log.logger.error(f"Error logging in: {e}")
            self.token = None

    def get_dashboard_data(self):
        self.__validate_token()
        dashboard_url = f"{self.base_url}/events/api/dashboard_data/"
        return self.__request_data(dashboard_url)

    def get_rewards_categories_data(self):
        self.__validate_token()
        categories_url = f"{self.base_url}/rewards/api/browse_reward_categories/"
        data = self.__request_data(categories_url)
        if data:
            raw_reward_categories = data.get('results', [])
            return [RewardCategory(**raw_reward_category) for raw_reward_category in raw_reward_categories]
        return None

    def get_reward_detail(self, reward_pk):
        self.__validate_token()
        reward_detail_url = f"{self.base_url}/rewards/api/rewards/{reward_pk}/"
        data = self.__request_data(reward_detail_url)
        if data:
            return Reward(**data)
        return None


# Usage example
api_client = APIClient("https://tom.skordev.com")
api_client.login("ankit@gmail.com", "pass")
print(f"Token: {api_client.token}")
dashboard_data = api_client.get_dashboard_data()
print(f"Dashboard data: {dashboard_data}")
reward_category_data = api_client.get_rewards_categories_data()
print(f"reward category data: {reward_category_data}")
