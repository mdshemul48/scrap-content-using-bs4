import requests

from dotenv import load_dotenv

load_dotenv()


class NewFtp:
    jsonToken: str = None

    def __init__(self, baseUrl: str,  email: str, password: str) -> None:
        self.baseUrl = baseUrl
        response = requests.post(self.requestUrl("api/auth/login"), data={"email": email, "password": password})
        if response.status_code != 202:
            raise Exception("Login failed with this user.")
        jsonData = response.json()
        self.jsonToken = jsonData["token"]

    def requestUrl(self, path: str):
        return self.baseUrl + path

    def submitPost(self, post: dict):
        headers = {
            "Authorization": "Bearer " + self.jsonToken
        }
        response = requests.post(self.requestUrl("api/posts"), data=post, headers=headers)
        if response.status_code != 201:
            raise Exception("Post submission failed.")

        return response.json()


if __name__ == "__main__":

    ftp = NewFtp("http://localhost/", "mdshemul480@gmail.com", "123456")
