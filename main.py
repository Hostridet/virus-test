import src
from pprint import pprint
from pysafebrowsing import SafeBrowsing
from config import googleSafeApi


def parseStr(string):
    arr = string.split()
    return '+'.join(arr)


def createList(string):
    req = src.GoogleReq("RU", "desktop")
    req.setUrl(parseStr(string))
    return req.sendReq()


def main():
    # Create list of urls
    links = createList("brawl stars")

    # Check urls by Google Safe Browsing
    s = SafeBrowsing(googleSafeApi)
    pprint(s.lookup_urls(links))

    # Check urls by Virus Total
    vs = src.virusTotal()
    pprint(vs.sendReq(links))


if __name__ == '__main__':
    main()

