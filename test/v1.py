import sys
import json

# json_data = json.load("test/v1.json")
with open("v1.json") as json_file:
    json_data = json.load(json_file)


for item in json_data["taskDefinition"]["containerDefinitions"]:
    for env in item["environment"]:
        if env["name"] == "REVISION":
            env["value"] = "myrevision"

with open("v2.json", "w") as json_file:
    json.dump(json_data, json_file)
