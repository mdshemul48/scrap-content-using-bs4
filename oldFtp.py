import requests
from bs4 import BeautifulSoup


class Ftp():
    def page(self, page: int):
        self.page = page
        return self

    def __getContent(self, oldContent: str) -> list[dict]:
        print(oldContent)

    def __fetchSeries(self, url):
        print(url)
        page = requests.get(url)

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

        return seriesContent

    def fetchData(self):
        data = requests.get(f"http://circleftp.net/new-post-api/page/{self.page}").json()
        postIds: list[str] = data.keys()
        posts = []
        for postId in postIds:
            tags, categories,  title, poster, downloadLink, content, url = data[postId]
            # self.__getContent(content)

            series: list[dict] = None
            if ('su_tabs' in content):
                series = self.__fetchSeries(url)
            post = {
                "id": postId,
                "title": title,
                "tags": tags,
                "poster": poster,
                "categories": categories.split(",")[:-1],
                "downloadLink": downloadLink,
                "content": series if series else content,
                "url": url
            }
            posts.append(post)
            break
        return posts


if __name__ == '__main__':
    ftp = Ftp()
    data = ftp.page(1).fetchData()
    # print(data)
