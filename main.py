import json
import os
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from chat_parser import parse_logs


def load_dataset():
    messages = []
    responses = []
    with open('data.json', 'r', encoding="utf8") as openfileobject:
        data = json.load(openfileobject)
        for pair in data:
            if pair.get("message") is None or pair.get("response") is None:
                continue
            messages.append(pair.get("message"))
            responses.append(pair.get("response"))
    print("Loading dataset of size " + str(len(messages)))
    return [messages, responses]


# Convert facebook chat logs into json and load it
if not os.path.exists("data.json"):
    if len(sys.argv) == 2:
        user_name = sys.argv[1]
        parse_logs("messages.htm", user_name)
    else:
        print("You must enter the username.Start program by:\n'main.py \"John Smith\"'\nfor example.")
        quit()
[messages, responses] = load_dataset()

sklearn_tfidf = TfidfVectorizer(norm='l2')
sklearn_representation = sklearn_tfidf.fit_transform(messages)

print("I am ready! Let's chat.")
for line in sys.stdin:
    input = sklearn_tfidf.transform([line])
    similarities = cosine_similarity(input, sklearn_representation)
    response = responses[similarities.argmax()]
    print(response)
