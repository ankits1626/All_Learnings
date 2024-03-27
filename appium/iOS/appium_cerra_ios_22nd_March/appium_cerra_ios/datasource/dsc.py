from abc import ABC, abstractmethod


class Datasource(ABC):
    @property
    @abstractmethod
    def token(self):
        pass

    @abstractmethod
    def get_dashboard_data(self):
        pass

    @abstractmethod
    def get_rewards_categories_data(self):
        pass

    @abstractmethod
    def get_reward_detail(self, reward_pk):
        pass
