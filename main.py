from oldFtp import OldFtp
import json


def main():
    file = json.loads(open("info.json", "r").read())
    print(file)
    for i in range(file["current"], file["end"]+1):
        allData = json.loads(open("data.json", "r").read())
        ftp = OldFtp()
        allData += ftp.setPage(i).fetchData()
        open("data.json", "w").writelines(json.dumps(allData, indent=2))
        file["current"] = i+1
        open("info.json", "w").writelines(json.dumps(file, indent=2))


if __name__ == "__main__":
    main()
