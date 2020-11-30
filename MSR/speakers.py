import requests
from .settings import accessToken, baseUrl
import json
from json.decoder import JSONDecodeError
from .audio_convert import wavToRaw

# 話者グループ一覧
def getSpeakerGroup():
    url = f"{baseUrl}/srs/speaker_groups"
    headers = {"Authorization": f"Bearer {accessToken}"}
    # リクエスト
    res = requests.get(url, headers=headers)
    speakerGroup = json.loads(res.text)
    return speakerGroup


#　myhouseグループの取得
def getSpeakerGroupId():
    pass

# user学習開始
def learn_start(speakerId: str):
    url = f"{baseUrl}/srs/speakers/{speakerId}/trainer/commit"
    headers = {"Authorization": f"Bearer {accessToken}"}
    # リクエスト
    res = requests.post(url, headers=headers)
    print(res.text)


# curl -X POST https://apis.mimi.fd.ai/v1/applications/<applicationId>/clients/<clientId>/srs/speakers/<speakerId>/speeches \
# --data-binary @/path/to/audio.raw  \
# -H "Authorization: Bearer <accessToken>"

# user詳細
def speakerDescription(speakerId: str) -> list:
    url = f"{baseUrl}/srs/speakers/{speakerId}"

    headers = {"Authorization": f"Bearer {accessToken}"}
    # リクエスト
    res = requests.get(url, headers=headers)
    try:
        speaker = json.loads(res.text)
    except json.decoder.JSONDecodeError:
        raise(ValueError("話者の詳細の取得に失敗しました"))
    return speaker

if __name__ == "__main__":
    speakerId =  "de1f81f684184a74ac6e3a9b63841a18"
    speakerDescription(speakerId)

