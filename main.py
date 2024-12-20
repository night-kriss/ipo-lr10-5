import requests
import json
from bs4 import BeautifulSoup as bs
datas = []
url = "https://github.com/trending"
response = requests.get(url)
soup = bs(response.text, "html.parser")
count = 1
for data in soup.find_all('article', class_="Box-row"):
    rep = data.find('a', class_='Link').get_text().strip().replace(' ', '').splitlines()
    stars = data.find('a', class_='Link Link--muted d-inline-block mr-3').get_text().strip().replace(' ', '')
    reposit = rep[0]+rep[2]
    datas.append({'Repository': reposit, "Stars": stars})
    print(f"{count}. Repository: {reposit}; Stars: {stars};")
    count+=1
def savejson(datas, file="data.json"):
    with open(file,"w",encoding="utf-8")as f:
        json.dump(datas, f, ensure_ascii=False, indent=2)
savejson(datas)
def html(file="data.json", file_html="index.html"):
    with open(file,"r",encoding="utf-8")as f:
        datas=json.load(f)
    html_code ='''
<html>
    <head>
        <title>Список репозиториев</title>
        <style>
            body {
                color: #8c6f6f;
                background-color: #375954;
            }
            table {
                background: #7a4560;
            }
            th, td {
                padding: 20px;
                border: 1px solid #3b3b3b;
                text-align: center;
            }
            th {
                background-color: #3b3b3b;
                color: #000000;
            }
            h1 {
                text-align: left;
                margin-bottom: 25px;
            }
            p {
                text-align: left;
                margin-top: 25px;
            }
            a {
                color: #605967;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Коллекция репозиториев</h1>
            <table>
                <tr>
    '''
    for id, data in enumerate(datas, 1):
        html_code += f'''
        <tr>
            <td><h3>{id}</h3></td>
            <td><h3>{data["Repository"]}</h3></td>
            <td><h3>{data["Stars"]}<h3></td>
        </tr>
        '''
    html_code += '''
            </table>
            <p>
                <h2><a href="https://github.com/trending">Источник: Repositories in Trend(GitHUB)</a></h2>
            </p>
        </div>
    </body>
</html>
    '''
    with open(file_html, "w", encoding="utf-8") as f:
        f.write(html_code)
html()
