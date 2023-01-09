import requests


class Ftp():
    def page(self, page: int):
        self.page = page
        return self

    def __getContent(self, oldContent: str) -> list[dict]:
        print(oldContent)

    def fetchData(self):
        data = requests.get(f"http://circleftp.net/new-post-api/page/{self.page}").json()
        postIds: list[str] = data.keys()
        posts = []
        for postId in postIds:
            print(data[postId])
            tags, categories,  title, poster, downloadLink, content, url = data[postId]
            self.__getContent(content)
            post = {
                "id": postId,
                "title": title,
                "tags": tags,
                "poster": poster,
                "categories": categories.split(",")[:-1],
                "downloadLink": downloadLink,
                "content": content,
                "url": url
            }
            posts.append(post)
            break
        return posts


if __name__ == '__main__':
    ftp = Ftp()
    data = ftp.page(2).fetchData()
    # print(data)
