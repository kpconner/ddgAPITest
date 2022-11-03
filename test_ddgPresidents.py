import json
import requests

presidentLastNames = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Buren',
                          'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
                          'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'McKinley',
                          'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Truman', 'Eisenhower',
                          'Kennedy', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Obama', 'Trump', 'Biden']

url_ddg = "https://api.duckduckgo.com"


def test_PresidentsList():
    lastNameList = []
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    resp_data = resp.json()
    related_topics = resp_data["RelatedTopics"]
    for entry in related_topics:
        lastNameList.append(entry["Text"].split(' -')[0].split(" ")[-1])
    for name in presidentLastNames:
        assert name in lastNameList
