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
    quality: str = None

    poster: bytes = None

    content: list | str | list[dict] = None
    contentType: ContentType = None

    categories: list[int] = None
    tags: str = None
    metaData: str = None

    def __init__(self, title: str, name: str, year: int | None = None):
        self.title = title
        self.name = name
        self.year = year

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

    def addQuality(self, quality: str):
        self.quality = quality
        return self

    def addPoster(self, poster: bytes):
        self.poster = poster
        return self

    def build(self) -> dict:
        return {
            "name": self.name,
            "year": self.year,
            "title": self.title,
            "watchTime": self.watchTime,
            "quality": self.quality,
            "type": self.contentType.value,
            "categories": self.categories,
            "tags": self.tags,
            "metaData": self.metaData,
            "content": self.content,
            "poster": self.poster
        }


def main():
    singlePost = Post("The Godfather", "The Godfather", 1972).addContent(
        "https://www.youtube.com/watch?v=sY1S34973zA", Post.ContentType.SINGLE_VIDEO).addCategories([1, 2, 3]).addTags(
        "The Godfather, 1972, Mafia, Crime, Drama, Thriller").addMetaDeta(
        "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.").addWatchTime(
        "2h 55m").addQuality("1080p").addPoster(open("test.jpg", "rb").read()).build()
    print(singlePost)


if __name__ == "__main__":
    main()
