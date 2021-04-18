from Contributor import Contributor

USERS = [
    "54696d21",
    "Stefan Grotz"
]

USERS2 = [
    {"user": "54696d21", "contrib": 119},
    {"user": "Stefan Grotz", "contrib": 6014},
]

USERS3 = [
    Contributor(username="54696d21", clientHash="0272ed18c2dfde45ceb61d5f0dd34fcb8026d55cb6876339dc3762c45bc58699",
                validatedClipsBeginning=11, recordedClipsBeginning=12),
    Contributor(username="Stefan Grotz", clientHash="16e3ec4bc4408cae301120760cef8d4b4aeaf07f0ca3884afdb8d04857f675af",
                validatedClipsBeginning=11, recordedClipsBeginning=12)
]
