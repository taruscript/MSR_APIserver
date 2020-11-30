import requests
from .settings import accessToken
import json
from json.decoder import JSONDecodeError

url = "https://service.mimi.fd.ai"


def execRecognition(speakerGroupId: str, audioByte: bytes):
    headers = {
        "content-type": "audio/x-pcm;bit=16;rate=16000;channels=1",
        "x-mimi-srs-speaker-group-id": speakerGroupId,
        "x-mimi-process":"srs",
        "x-mimi-input-language":"ja",
        "Authorization": f"Bearer {accessToken}"
    }

    res = requests.post(url, data=audioByte, headers=headers)

    try:
        result = json.loads(res.text)
    except JSONDecodeError:
        raise(ValueError("話者識別の結果の取得に失敗しました"))
    return result