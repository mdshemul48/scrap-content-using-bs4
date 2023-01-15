import requests
from guessit import guessit
from enum import Enum


class Post:

    class ContentType(Enum):
        SERIES = "series"
        SINGLE_VIDEO = "singleVideo"
        SINGLE_FILE = "singleFile"
        MULTI_FILE = "multiFile"
        MULTI_VIDEO = "multiFile"

    name: str = None
    year: int = None
    title: str = None
    watchTime: str = None

    poster = None

    content: list | str | list[dict] = None
    contentType: ContentType = None

    categories: list[int] = None
    tags: str = None
    metaData: str = None

    def __init__(self, title: str, name: str, year: int | None = None):
        self.title = title
        self.name = name
        self.year = year
        return self

    def addContent(self, content: list | str | list[dict], contentType: ContentType):
        self.content = content
        self.contentType = contentType
        return self

    def addCategories(self, categories: list[int]):
        self.categories = categories
        return self

    def addTags(self, tags: str):
        self.tags = tags
        return self

    def addMetaDeta(self, metaData: str):
        self.metaData = metaData
        return self

    def addWatchTime(self, watchTime: str):
        self.watchTime = watchTime
        return self


def main():
    file: list[dict] = open("data.json", "r").read()


if __name__ == "__main__":
    main()
