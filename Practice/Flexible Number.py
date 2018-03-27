from urllib import request

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=5&e=23&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv"


def download_info(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r"goog.csv"
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download_info(goog_url)