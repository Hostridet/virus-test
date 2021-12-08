import requests
import re
from config import rapidKey


class GoogleReq:
    __proxy = "US"
    __agent = "desktop"
    __headers = ""
    __url = ""

    def __init__(self, proxy, agent):
        self.__proxy = proxy
        self.__agent = agent
        self.__headers = {
            'x-user-agent': self.__agent,
            'x-proxy-location': self.__proxy,
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': rapidKey
        }

    # Set what we will try to find
    def setUrl(self, string):
        self.__url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={string}&num=100"

    # Trying to send a request
    def sendReq(self):
        try:
            request = requests.request("Get", self.__url, headers=self.__headers)
            data = request.json()
            data = data['results']
            return self.__createArr(data)
        except Exception as ex:
            return ex

    # Creating list of links
    def __createArr(self, data):
        arr = []
        for i in range(len(data)):
            arr.append(data[i]['link'])
        return self.__parseStr(arr)

    # Removing extra characters from a link
    def __parseStr(self, arr):
        new_arr = []
        for i in range(len(arr)):
            new_arr.append("".join(re.split(r'(?:[()])',arr[i])))
        return new_arr

