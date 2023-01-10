import requests
from bs4 import BeautifulSoup
from util import isVideoFile
from Logger import CustomLogger
import json


class OldFtp(CustomLogger):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.logger.info("starting script")

    def page(self, page: int):
        self.page = page
        return self

    def __fetchTableData(self, url) -> list[dict]:
        self.logger.info('fetching from website')
        page = requests.get(url)
        self.logger.info('fetching website done')

        soup = BeautifulSoup(page.text, features="html.parser")
        seriesElement = soup.find("div", class_="su-tabs")
        seriesContent = []
        for season in seriesElement.find_all('div', class_="su-tabs-pane"):
            seasonName = season['data-title']
            seasonData = {"seasonName": seasonName, "episode": []}

            for tableRow in season.find("table").find_all('tr')[1:]:
                tableData = tableRow.find_all("td")
                name = tableData[0].getText()
                link = tableData[1].find("a")["href"]
                seasonData["episode"].append({
                    "name": name,
                    "link": link
                })
            seriesContent.append(seasonData)
            break
        return seriesContent

    def fetchData(self):
        self.logger.info("fetching contents from api")
        allData = requests.get(f"http://circleftp.net/new-post-api/page/{self.page}").json()
        self.logger.info("done fetching content.")

        postIds: list[str] = allData.keys()
        posts = []
        count = 1
        for postId in postIds:
            self.logger.info(f"processing id: {postId} -> count: {str(count)}")
            count += 1
            tags, categories,  title, poster, downloadLink, content, url = allData[postId]
            try:
                data = None
                dataType = None
                if len(downloadLink) > 0:
                    data = downloadLink
                    dataType = 'singleVideo' if isVideoFile(downloadLink) else "singleFile"
                if 'su_tabs' in content and not "All Parts" in content:
                    data = self.__fetchTableData(url)
                    dataType = "TvSeries"
                    pass
                elif "All Parts" in content:
                    data = self.__fetchTableData(url)
                    dataType = "multipleFile"

                post = {
                    "id": postId,
                    "title": title,
                    "tags": tags,
                    "poster": poster,
                    "categories": categories.split(",")[:-1],
                    "downloadLink": downloadLink,
                    "url": url,
                    "contentType": dataType,
                    "content": data,
                }
                posts.append(post)
            except:
                self.logger.error(f"processing id: {postId} -> count: {str(count)} URl: {url}")
        self.logger.info("Done Scraping")
        return posts


if __name__ == '__main__':
    ftp = OldFtp()
    data = ftp.page(1).fetchData()
    file = open("data.json", "w")
    file.writelines(json.dumps(data, indent=2))
