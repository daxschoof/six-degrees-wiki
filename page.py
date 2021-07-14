from bs4 import BeautifulSoup
import requests


class Page:
    def __init__(self, url: str) -> None:
        self.url = url
        self.links = []
        self.name = None
        self.parent = None

    '''
        Gets all the links in the page and adds it to the array links
        In the form of /wiki/..., filtering for several things
    '''

    def populateLinks(self) -> list[str]:
        def checkIfValidLink(link: str) -> bool:
            if link and link.startswith('/wiki/'):
                if link[6:14] != 'Category':
                    return True
            return False

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        contentDiv = soup.find(id="bodyContent")
        linkArr = contentDiv.find_all("a")
        linkArr = [aTag.get('href') for aTag in linkArr]

        linkArr = filter(checkIfValidLink, linkArr)
        self.links = linkArr

    '''
        Gets the name of the page from the url
    '''

    def getName(self) -> str:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        titleBox = soup.find(id="firstHeading")
        if titleBox:
            self.name = titleBox.string
