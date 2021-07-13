class Page:
    def __init__(self, url: str) -> None:
        self.url = url
        self.links = []
        self.name = None
        self.parent = None

    def populateLinks(self) -> List[str]:
        pass

    def getName(self) -> str:
        pass
