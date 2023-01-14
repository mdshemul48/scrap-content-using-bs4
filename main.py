from oldFtp import OldFtp
import json


def main():
    ftp = OldFtp()
    allData = ftp.setPage(1).fetchData()

    file = open("data.json", "w")
    file.writelines(json.dumps(allData, indent=2))


if __name__ == "__main__":
    main()
