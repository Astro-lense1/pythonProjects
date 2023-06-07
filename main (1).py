import requests
from bs4  import BeautifulSoup

#Send a get Request to request website

url = 'https://en.wikipedia.org/wiki/World_War_II'

#REplace the URL of the website of the website we want to scrape

response = requests.get(url)

#Create a bs4 object to parse the HTML content

soup = BeautifulSoup(response.content, 'html.parser')

#find and extract the specific data that we want from the website.
#replace all lines with the elements 

title = soup.find('h1').text
Paragraphs = soup.find_all('p')

#print the data extracted 

print('Title:', title)
print('Paragraphs:')
for p in Paragraphs:
    print(p.text)
