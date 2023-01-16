import json
from Post import Post
from guessit import guessit





def main():
    jsonFile = open("data.json", "r")
    postsData: list[dict] = json.loads(jsonFile.read())

    categoriesId = json.loads(open("categories.json").read())

    for postData in postsData:
        # print(postData)
        postTitleExtractedData = guessit(postData["title"])
        print(postTitleExtractedData)

        year: int = None
        if "year" in postTitleExtractedData.keys():
            if type(postTitleExtractedData["year"]) == int:
                year = postTitleExtractedData["year"]
            else:
                year = postTitleExtractedData["year"][0]

        post = Post(postData["title"], postTitleExtractedData["title"], year)

        contentType: post.ContentType = None
        if postData["contentType"] == "TvSeries":
            contentType = post.ContentType.SERIES
        elif postData["contentType"] == "singleVideo":
            contentType = post.ContentType.SINGLE_VIDEO
        elif postData["contentType"] == "singleFile":
            contentType = post.ContentType.SINGLE_FILE
        elif postData["contentType"] == "multipleFile":
            contentType = post.ContentType.MULTI_FILE
        else:
            raise Exception("Unknown content type")

        post.addContent(json.dumps(postData["content"]).replace("name", "title"), contentType)

        if 'screen_size' in postTitleExtractedData.keys():
            post.addQuality(postTitleExtractedData["screen_size"])

        post.addTags([postData["tags"]])

        oldCategories = postData["categories"]
        newCategories = [categoriesId[category] for category in oldCategories]
        post.addCategories(newCategories)

        print(post.build())
        break


if __name__ == "__main__":
    main()
