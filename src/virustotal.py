import json

import requests
from config import virusTotalApi


class virusTotal:
    __url = "https://www.virustotal.com/vtapi/v2/url/scan"
    __headers = ""
    __payload = ""

    def __init__(self):
        self.__headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-host': "VirusTotaldimasV1.p.rapidapi.com",
            'x-rapidapi-key': "6690731a75msh2e95013e7f1d611p12ff9djsn41bda956f3c4"
        }

    def setPayLoad(self):
        self.__payload = "domain=dlandroid.com%2Fbrawl-stars-apk-mod%2F&apikey}"

    def sendReq(self, urls):
        site = "https://www.trukocash.com/de/brawl-stars"
        url = "https://www.virustotal.com/vtapi/v2/file/report"
        headers = {'apikey': virusTotalApi, 'resource': site}
        request = requests.post(url, params=headers)
        data = request.json()
        return data
