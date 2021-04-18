import requests
import json
import datetime
import os
import time
from Contributor import COn

URL_VALIDATED = "https://commonvoice.mozilla.org/api/v1/de/clips/votes/leaderboard?cursor=[1,23565]"
URL_RECORDED = "https://commonvoice.mozilla.org/api/v1/de/clips/leaderboard?cursor=[1,23565]"




class Data:
    def __init__(self) -> None:
    # def __init__(self, **kwargs):
        self.validatedApiResonseContent = None
        self.recordedApiResonseContent = None

    def fetchDataFromApi(self) -> None:
        r = requests.get(URL_VALIDATED)
        self.validatedApiResonseContent = json.loads(r.content)
        for i in self.validatedApiResonseContent:
            i["avatarClipUrl"] = None
            i["avatar_url"] = None

        r = requests.get(URL_RECORDED)
        self.recordedApiResonseContent = json.loads(r.content)
        for i in self.recordedApiResonseContent:
            i["avatarClipUrl"] = None
            i["avatar_url"] = None
    


if __name__ == "__main__":
    data = Data()
    data.fetchDataFromApi()
    # print(data.recordedApiResonseContent)
    # print(data.validatedApiResonseContent)
