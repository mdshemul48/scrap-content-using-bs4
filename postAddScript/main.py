import json
from Post import Post
from guessit import guessit
import requests
from NewFtp import NewFtp
from Logger import CustomLogger


def main():
    jsonFile = open("data.json", "r")
    postsData: list[dict] = json.loads(jsonFile.read())

    categoriesId = json.loads(open("categories.json").read())

    ftp = NewFtp("http://localhost/", "mdshemul480@gmail.com", "123456")
    logger = CustomLogger("main.py")

    for postData in postsData:
        logger.info(f"Processing:- {postData['id']} Link: {postData['url']}")
        try:
            postTitleExtractedData = guessit(postData["title"])

            year: int = None
            if "year" in postTitleExtractedData.keys():
                if type(postTitleExtractedData["year"]) == int:
                    year = postTitleExtractedData["year"]
                else:
                    year = postTitleExtractedData["year"][0]

            post = Post(postData["title"], postTitleExtractedData["title"], year)

            contentType: post.ContentType = None
            content: str = None
            if postData["contentType"] == "TvSeries":
                contentType = post.ContentType.SERIES
                contentTemp = []
                for season in postData["content"]:
                    seasonData = {}
                    seasonData["seasonName"] = season["seasonName"]
                    seasonData["episodes"] = []
                    for episode in season["episode"]:
                        episodeData = {}
                        episodeData["title"] = episode["name"]
                        episodeData["link"] = episode["link"]
                        seasonData["episodes"].append(episodeData)
                    contentTemp.append(seasonData)
                content = json.dumps(contentTemp)

            elif postData["contentType"] == "singleVideo":
                contentType = post.ContentType.SINGLE_VIDEO
                content = json.dumps(postData["content"])
            elif postData["contentType"] == "singleFile":
                contentType = post.ContentType.SINGLE_FILE
                content = json.dumps(postData["content"])
            elif postData["contentType"] == "multipleFile":
                contentType = post.ContentType.MULTI_FILE
                content = json.dumps(postData["content"][0]["episode"]).replace("\"name\"", "\"title\"")
            else:
                raise Exception("Unknown content type")

            post.addContent(content,  contentType)

            if 'screen_size' in postTitleExtractedData.keys():
                post.addQuality(postTitleExtractedData["screen_size"])

            post.addTags([postData["tags"]])

            oldCategories = postData["categories"]
            newCategories = [categoriesId[category] for category in oldCategories]
            post.addCategories(json.dumps(newCategories))

            image = requests.get(postData["poster"]).content
            open("poster.jpg", "wb").write(image)
            ftp.submitPost(post.build(), open("poster.jpg", "rb"))

        except Exception as e:
            logger.error(f"Error while processing {postData['id']}: {e} Link: {postData['url']}")


if __name__ == "__main__":
    main()
