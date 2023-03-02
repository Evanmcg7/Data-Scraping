import requests
import pandas as pd
from bs4 import BeautifulSoup
from csv import writer

# Scraping HTML Content from Webpage
Base_URL = "https://cryptopunks.app/cryptopunks/details/"
PunkNo_URL = '11'
page = requests.get(Base_URL + PunkNo_URL)

soup = BeautifulSoup(page.content, "html.parser")

# Locating Attributes
results = soup.find(id="punkDetails")
print(results.prettify)
attrbs = soup.find("div", class_="col-md-10 col-md-offset-1")
print(attrbs.prettify)

# Isolating 'Attributes', 'CryptoPunk Title' and 'CryptoPunk Description'
with open(r'C:\Users\Evan Mc Garry\Desktop\FDS\Homework1\CryptoPunk.csv', 'w', encoding='utf8', newline='') as f:
    cp_writer = writer(f)
    header = ['Title', 'Description', 'Attribute No.', 'Attributes']
    cp_writer.writerow(header)
    title = results.find('h1', style="margin-top: 0px; margin-bottom: 5px;").text
    desc = results.find('h4', style="margin-top: 0px;").text
    attr_no = results.find('p', style="margin-top: 0px;").text
    attributes_3 = attrbs.find('div', class_="row").text

    data = [title, desc, attr_no, attributes_3]
    cp_writer.writerow(data)

df = pd.read_csv(r"C:\Users\Evan Mc Garry\Desktop\FDS\Homework1\CryptoPunk.csv")
print(df.to_latex(index=False))