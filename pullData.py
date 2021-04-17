import requests
import json
import datetime
import os
import time

utcnow = datetime.datetime.utcnow()
date_time = utcnow.strftime("%Y-%m-%d--%H-%M")
FOLDER_NAME = "datadir"
# FILE_NAME = f"{FOLDER_NAME}/data_{date_time}.json"
FILE_NAME = f"{FOLDER_NAME}/data_{date_time}.json"

url = "https://commonvoice.mozilla.org/api/v1/de/clips/votes/leaderboard?cursor=[1,23565]"

r = requests.get(url)
jsonData = json.loads(r.content)

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

# b = next(jsonData)
# b = (jsonData)
# print(b.keys())
# print(b["avatarClipUrl"])
# print(b["clientHash"])
import sys

# print(sys.getsizeof(b))
# time.sleep(1)
l = list()
# for i in range(len(b[0])):
for i in jsonData:
    # print(i)
    print(sys.getsizeof(i))
    i["avatarClipUrl"] = None
    # l.append(i)

    # print(i["avatarClipUrl"])
    # print(b[i]["username"])
    # b[i]["avatarClipUrl"] = 0

# for j in l:
    # print(i)
    # print(j["avatarClipUrl"])
# for i in b:
#     # print(i)
#     # print(type(i))
#     # i["avatarClipUrl"] = 0
#     # i["avatarClipUrl"] = 0
#     # b[]
#     # i.pop("avatarClipUrl")
#     if 'avatarClipUrl' in i:
#         del i['avatarClipUrl']

# for i in b:
#     # print(i)
#     # print(type(i))
#     # i["avatarClipUrl"] = 0
#     # i["avatarClipUrl"] = 0
#     # b[]
#     # i.pop("avatarClipUrl")
#     if 'avatarClipUrl' in i:
#         del i['avatarClipUrl']

# print(sys.getsizeof(l))


# print("sleep")
# time.sleep(1)
# for i in b:
#     print(i)

# exit(0)
# for i in jsonData:
#     nex
# print(l)

with open(FILE_NAME, "w") as f:
    # f.write(repr(jsonData))
    json.dump(jsonData, f)
