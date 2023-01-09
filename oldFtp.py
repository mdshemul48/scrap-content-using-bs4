import requests


class Ftp():
    def page(self, page: int):
        self.page = page
        return self

    def fetchData(self):
        data = requests.get(f"http://circleftp.net/new-post-api/page/{self.page}").json()
        postIds: list[str] = data.keys()
        posts = []
        for postId in postIds:
            tags, categories,  title, poster, downloadLink, content = data[postId]

            post = {
                "title": title,
                "tags": tags,
                "poster": poster,
                "categories": categories.split(",")[:-1],
                "downloadLink": downloadLink,
                "content": content
            }
            posts.append(post)
        return posts


if __name__ == '__main__':
    ftp = Ftp()
    data = ftp.page(1).fetchData()
    print(data)
