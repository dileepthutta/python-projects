import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/100-greatest-world-cinema-films/"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")


#To Extract Data from the website of Top 100 Movies.
movies_list = []
for span in soup.find_all("span",class_="content_content__i0P3p"):
    h2 = span.find("h2")
    if h2:
        movies_list.append(h2.text)


#To Add the Data into the text File.
for i in movies_list[::-1]:
    try:
        with open("movies.txt","a") as file:
            file.write(i)
            file.write("\n")
    except FileExistsError:
        with open("movies.txt","w") as data:
            data.write(i)
            data.write("\n")

print("Data added into a new file.")