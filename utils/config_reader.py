import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "testsetting.json")
            with open (config_path, 'r') as file:
                ConfigReader._config = json.load(file)
        return ConfigReader._config
    
    @staticmethod
    def get_base_url():
        return ConfigReader.load_config()["base_url"]
    
    @staticmethod
    def get_user_name():
        return ConfigReader.load_config()["credentials"]["username"]
    
    @staticmethod
    def get_password():
        return ConfigReader.load_config()["credentials"]["password"]
    
    @staticmethod
    def get_invalid_user_name():
        return ConfigReader.load_config()["invalid_credentials"]["username"]
    
    @staticmethod
    def get_invalid_password():
        return ConfigReader.load_config()["invalid_credentials"]["password"]
    
    @staticmethod
    def get_vacancy_name():
        return ConfigReader.load_config()["vacancy_name"]
    
    @staticmethod
    def get_description():
        return ConfigReader.load_config()["description"]

    @staticmethod
    def get_number_of_positions():
        return ConfigReader.load_config()["number_of_positions"]    