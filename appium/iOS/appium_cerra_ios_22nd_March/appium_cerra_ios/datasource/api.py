import os.path

import requests
import configparser

from datasource.dsc import Datasource
from datasource.models.reward_models import RewardCategory, Reward
from utility.configReader import read_config
from utility.logger import setup_logger
from utility.misc import get_project_folder_path

logger = setup_logger()


class APIDatasource(Datasource):

    def __init__(self):
        self._server_url = None
        self._token = None

    @property
    def token(self):
        if self._token is None:
            self._fetch_token()
        return self._token

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
            logger.error(f"Error fetching data from {url}: {e}")
            return None

    def _fetch_token(self):
        # Read username and password from conf.ini
        print('<<<<< fetching token')
        logger.info('fetching token')
        config_file_path = os.path.join(get_project_folder_path(), 'conf.ini')
        config = configparser.ConfigParser()
        config.read(config_file_path)
        self._server_url = read_config('api', 'server_url')
        username = read_config('credentials', 'username')
        password = read_config('credentials', 'password')

        login_url = f"{self._server_url}/profiles/api/token-auth/"
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
            self._token = token_data.get("token")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error logging in: {e}")
            self._token = None

    def __validate_token(self):
        if not self.token:
            raise ValueError("Token not available. Please log in first.")

    def get_dashboard_data(self):
        self.__validate_token()
        logger.info('fetching dashboard data')
        dashboard_url = f"{self._server_url}/events/api/dashboard_data/"
        return self.__request_data(dashboard_url)

    def get_rewards_categories_data(self):
        self.__validate_token()
        categories_url = f"{self._server_url}/rewards/api/browse_reward_categories/"
        data = self.__request_data(categories_url)
        if data:
            raw_reward_categories = data.get('results', [])
            return [RewardCategory(**raw_reward_category) for raw_reward_category in raw_reward_categories]
        return None

    def get_reward_detail(self, reward_pk):
        self.__validate_token()
        reward_detail_url = f"{self._server_url}/rewards/api/rewards/{reward_pk}/"
        data = self.__request_data(reward_detail_url)
        if data:
            return Reward(**data)
        return None


# test
# api_dsc = APIDatasource()
# print(api_dsc.token)
# print(api_dsc.get_dashboard_data())
