import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
house_url = 'YOUR_ZILLOW_PROPERTY_URL_GOES_HERE'

r = requests.get(house_url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')

desc = soup.find('meta', property='zillow_fb:description')['content']
desc1 = desc.split('$')[1]
desc2 = desc1.split('.')[0]
house_value = desc2.replace(',', '')

headers = {'Authorization': 'Bearer YOUR_LUNCH_MONEY_API_KEY_GOES_HERE'}

r = requests.get('https://dev.lunchmoney.app/v1/assets', headers=headers)

payload = {'balance': house_value}

r = requests.put("https://dev.lunchmoney.app/v1/assets/YOUR_LUNCH_MONEY_ASSET_ID_GOES_HERE", data = payload, headers=headers)
