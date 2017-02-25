import xml.etree.ElementTree
import json


def parse_logs(log_file_path, user_name):
    print("Parsing chat logs of user " + user_name)
    root = xml.etree.ElementTree.parse(log_file_path).getroot()

    data = []

    for thread in root[1][1][1]:
        for i in range(len(thread) - 1, 0, -2):  # chat logs are sorted by the newest first, so iterate backward
            name = thread[i - 1][0][0].text
            text = thread[i].text
            next_name = thread[i - 3][0][0].text
            next_text = thread[i - 2].text
            if not name == user_name and next_name == user_name:
                data.append({"message": text, "response": next_text})

    file = open('data.json', 'w', encoding="utf-8")
    json.dump(data, file, ensure_ascii=False)
    file.close()
