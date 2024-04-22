import requests
from bs4 import BeautifulSoup

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1116"

html = requests.get(url).text

# print(html)

soup = BeautifulSoup(html, 'html.parser')

date = soup.find('p', {'class' : 'desc'}).text
print(date)

lottoNumber = soup.find('div', {'class' : 'num win'}).find('p').text.strip().split('\n')
print(lottoNumber)

bonusNumber = soup.find('div', {'class' : 'num bonus'}).find('p').text.strip()
print(bonusNumber)

