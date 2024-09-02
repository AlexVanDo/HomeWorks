from pprint import pprint
import requests
from bs4 import BeautifulSoup
import fake_headers
import re
import json

headers = fake_headers.Headers(browser="chrome", os="win")

main_html = requests.get(
    "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2", headers=headers.generate()
).text
main_soup = BeautifulSoup(main_html, features="lxml")

main_vacancy_serp_content = main_soup.find("main", class_="vacancy-serp-content")

titles = main_vacancy_serp_content.find_all("div", class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")

parsed_data = []
Dj = "Django"
Fk = "Flask"
for vacansy in titles:
    header = vacansy.find("a", class_="bloko-link").text.strip()
    link = vacansy.find('a').get('href')
    company_name = vacansy.find('span', class_="company-info-text--vgvZouLtf8jwBmaD1xgp").text.strip()
    city = vacansy.find('div', class_="info-section--N695JG77kqwzxWAnSePt").find('div',
                                                                                  class_="wide-container--lnYNwDTY2HXOzvtbTaHf").find('span', class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni").text.strip()
    salary = vacansy.find("div", class_="wide-container--lnYNwDTY2HXOzvtbTaHf").find('span', class_="bloko-text")
    if salary :
        salary = salary.text
        salary = str(salary)
        salary = re.sub('[^\d,^–,^$,^₽]', '', salary)
    else:
        salary = 'Не указана'

    if (Dj in header or Fk in header):
        parsed_data.append({
            "header": header,
            'link':link,
            'salary':salary,
            'company_name':company_name,
            'city':city
            })
pprint(parsed_data)

with open('new_vacansy.json', 'w', encoding="utf-8") as nv:
    json.dump(parsed_data, nv, ensure_ascii=False)