import datetime
import json
import contributorsCompetition
BASELINE = "datadir/data_2021-04-16--22-50.json"
LATEST = "datadir/data_2021-04-16--22-56.json"

# sum = (0.5*valdierungszahl) + aufnahmezahl

HTML_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<ul>
"""

HTML_MIDDLE = """</ul>
</body>
</html>"""

with open(BASELINE) as json_file:
    data = json.load(json_file)
    # print(data)
    o = list()
    for i in data:
        user = i["username"]
        if user in contributorsCompetition.USERS:
            # user contributorsCompetition.USERS2[user]
            for j in contributorsCompetition.USERS2:
                if j["user"] == user:
                    oldContrib = j["contrib"]
                    delta = i["total"] - oldContrib
                    o.append({'user': user, 'delta': delta})
    # print(o)
    # print(sorted(o, key=o.delta))
                    print(sorted(o, key=lambda o: o['delta'], reverse=True))
                    top20 = o[0:20]
                    with open("out.html", "w") as htmlout:
                        htmlout.write(HTML_TOP)
                        for idx, val in enumerate(o):
                            # print(idx+1)
                            # htmlout.write(f"{idx+1}. {val['user']}<br>\n")
                            htmlout.write(f"<li>{idx+1}. {val['user']}</li>\n")
                        htmlout.write(HTML_MIDDLE)
                        utcnow = datetime.datetime.utcnow()
                        date_time = utcnow.strftime("%d.%m.%y %H:%M")
                        htmlout.write(f"""<footer>
  <p>last updated: {date_time} UTC</p>
</footer>""")


    # print(j[])
    # print(contributorsCompetition.USERS2[user])
    # print(USERS2[0]["54696d21"])

    # o.append(i)
    # print(i)
    # print()
    # print(o)
    # print(i["avatarClipUrl"])
    # exit(0)
    # print(i)
    # print("------")
    # for user in contributorsCompetition.USERS:
    #     print(user)
