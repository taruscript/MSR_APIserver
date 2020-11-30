import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import json


load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

applicationId = os.environ.get("applicationId")
clientId = os.environ.get("clientId")
clientSecret = os.environ.get("clientSecret")

# 基本的に使うUrl
baseUrl = f"https://apis.mimi.fd.ai/v1/applications/{applicationId}/clients/{clientId}"


scope_urls = [
    "https://apis.mimi.fd.ai/auth/srs/http-api-service",
    "https://apis.mimi.fd.ai/auth/srs/websocket-api-service",
    "https://apis.mimi.fd.ai/auth/srs/speaker_groups.r",
    "https://apis.mimi.fd.ai/auth/srs/speaker_groups.w",
    "https://apis.mimi.fd.ai/auth/srs/speakers.r",
    "https://apis.mimi.fd.ai/auth/srs/speakers.w",
    "https://apis.mimi.fd.ai/auth/srs/speeches.r",
    "https://apis.mimi.fd.ai/auth/srs/speeches.w",
    "https://apis.mimi.fd.ai/auth/srs/trainers.r",
    "https://apis.mimi.fd.ai/auth/srs/trainers.w"
]

# 成功したかどうか
def success_check(res: dict):
    status = res["status"]

    if status == "error":
        error = res["error"]
        return error

    elif status == "success":
        return

def getAccessToken():
    url = 'https://auth.mimi.fd.ai/v2/token'
    scope = ",".join(scope_urls).replace(",", ";")
    data = {
        'grant_type': 'https://auth.mimi.fd.ai/grant_type/client_credentials',
        'client_id': f'{applicationId}:{clientId}',
        'client_secret': clientSecret,
        'scope': scope
    }

    # リクエスト
    res = requests.post(url, json=data)
    values = json.loads(res.text)

    if success_check(values) is not None:
        raise(ValueError(f"アクセストークンをゲットしようとしましたが失敗しました。error: {success_check(values)}"))
    
    accessToken = values["accessToken"]
    return accessToken

accessToken = getAccessToken()