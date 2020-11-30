import json
import os

class SetupClass:
    def __init__(self, path: str):
        self.path = path

    # configファイルの読み込み
    def loadConfigJSON(self):
        json_open = open(self.path, 'r')
        json_load = json.load(json_open)
        return json_load

    # 読み込んだファイルから環境変数に定義
    def set_environment_variable(self):
        allowed_key = ["clientId", "clientSecret", "applicationId"]
        json_load = self.loadConfigJSON()
        for key in allowed_key:
            try:
                os.environ[key] = json_load[key]
            except KeyError:
                raise KeyError(f" {key} が確認できませんでした。config.jsonを確認してください")

def setup(config_path: str):
    setup_object = SetupClass(config_path)
    setup_object.set_environment_variable()

if __name__ == "__main__":
    config_path = "../config.json"
    setup(config_path) 