import requests
import json
import datetime
import os
import logging
import time
from Contributor import Contributor
from contributorsCompetition import USERS3

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

    def buildDashboard(self) -> None:
        pass
        # print('ok')
        for contributor in USERS3:
            # print(i.username)
            # repr(i)
            for j in self.recordedApiResonseContent:
                # print(i)
                if j["username"] == contributor.username:
                    # print(j["username"])
                    contributor.currentRecordedClips = j.get("total")
            for j in self.validatedApiResonseContent:
                        # print(i)
                if j["username"] == contributor.username:
                    # print(j["username"])
                    contributor.currentValidatedClips = j.get("total")
                    # i.currentValidatedClips
                    # i.currentValidatedClips
            contributor.populateDeltas()
            contributor.populateScore()
            # for i in data:
            # user = i["username"]
            # if user in contributorsCompetition.USERS:
            #     # user contributorsCompetition.USERS2[user]
            #     for j in contributorsCompetition.USERS2:
            #         if j["user"] == user:
            #             oldContrib = j["contrib"]
            #             delta = i["total"] - oldContrib
            #             o.append({'user': user, 'delta': delta})

    def buildRanking(self) -> None:
        # sorted()
        # print(sorted(USERS3, key=lambda USERS3.: o['delta'], reverse=True))
        sortedList = sorted(USERS3, key=lambda contributor: contributor.competitionScore, reverse=True)
        print(sortedList)



if __name__ == "__main__":
    data = Data()
    data.fetchDataFromApi()
    data.buildDashboard()
    # for user in USERS3:
    #     print(user.username)
    #     print(user.currentRecordedClips)
    #     print(user.currentValidatedClips)
    #     print("-----")
    data.buildRanking()
    # print(data.recordedApiResonseContent)
    # print(data.validatedApiResonseContent)
