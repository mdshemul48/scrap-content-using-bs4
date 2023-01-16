import json


def getAllTheCategories(fileJson: list[dict]):
    allCategories = set()
    for post in fileJson:
        allCategories = allCategories | set(post["categories"])
    return list(allCategories)


if __name__ == "__main__":
    file = open("data.json", "r").read()
    fileJson = json.loads(file)
    categories = getAllTheCategories(fileJson)

    categoriesDist = {}
    for category in categories:
        categoriesDist[category] = 0
    print(categoriesDist)
