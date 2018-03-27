import re


def main():
    line = "I think I understand regular expression"
    matchresult = re.match('think', line, re.M | re.I)
    if matchresult:
        print("Match Found :" + matchresult.group())
    else:
        print("No match was found")

    searchresult = re.search('think', line, re.M | re.I)
    if searchresult:
        print("Search Found :" +searchresult.group())
    else:
        print("Nothing found in search")


if __name__ == "__main__":
    main()
