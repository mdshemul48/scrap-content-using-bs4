from oldFtp import OldFtp
import json


def main():
    ftp = OldFtp()
    allData = []
    for i in range(1, 10+1):
        allData += ftp.setPage(i).fetchData()

    file = open("data.json", "w")
    file.writelines(json.dumps(allData, indent=2))


if __name__ == "__main__":
    main()
