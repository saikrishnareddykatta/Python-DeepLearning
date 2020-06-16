from bs4 import BeautifulSoup
import requests

# URL used for web scrapping
html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(html.content, "html.parser")
# printing the title of the given URL
print(soup.title.String)
# printing all the anchor tags in given URL
print(soup.find_all('a'))
# opening a file
file2 = open("output.txt", 'a+', encoding='utf-8')
# finding all the links in anchor tag in URL
for link in soup.find_all('a'):
    # printing the href's in anchor tags
    print(link.get('href'))
    # writing the data into the file
    file2.write(str(link.get('href')))
    file2.write('\n')

file2.close()

