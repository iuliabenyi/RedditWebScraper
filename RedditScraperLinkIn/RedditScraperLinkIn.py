from pip._vendor import requests
import bs4
import csv
import time
import io

headers = {'User-Agent': 'Mozilla/5.0'}
next_page_link = 'https://old.reddit.com/r/datascience/'
#res = requests.get(next_page_link, headers = headers)
#print("Here again")
#soup = bs4.BeautifulSoup(res.text, 'lxml')
#domains = soup.find_all("span", class_="domain")
#for d in domains:
#    if d.text != "(self.datascience)":
#        continue 
#    biggestDiv = d.parent.parent.parent.parent
    #print(biggestDiv.text)

counter = 0
while counter <= 10:
    res = requests.get(next_page_link, headers = headers)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    #print(next_page_link)
    for post in soup.find_all('div', attrs={'class': 'thing', 'data-domain': 'self.datascience'}):
        #print(post.attrs['data-domain'])
        title = post.find('p', class_="title").text
        #print(title)
        author = post.find("a", class_="author").text
        #print(author)
        comments = post.find("a", class_="comments").text.split()[0]
        if(comments == "comment"):
            comments = 0
        #print(comments)
        upvotes = post.find("div", attrs={"class":"score likes"}).text
        if upvotes == "•":
            upvotes = None
        #print(upvotes)
        counter += 1
        postLine = [counter, title, author, upvotes, comments]
        with io.open('output.csv', 'a', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(postLine)
    #print("DONE with for")
            
    next_button = soup.find("span", class_="next-button")
    next_page_link = next_button.find("a").attrs['href']
    time.sleep(2)
    #res = requests.get(next_page_link, headers = headers)
    print("---------------")
    print(next_page_link)
    #soup = bs4.BeautifulSoup(res.text, 'lxml')

print("\nEverything works\n")
