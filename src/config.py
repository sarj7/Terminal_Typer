import os
import json

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
    
    def load_api_key(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as file:
                    config = json.load(file)
                    return config.get('api_key')
            except json.JSONDecodeError:
                return None
        return None
    
    def save_api_key(self, api_key):
        config = {'api_key': api_key}
        with open(self.config_file, 'w') as file:
            json.dump(config, file)