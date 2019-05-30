import requests  # Module imported Sucessfully.
import bs4
# These Lines Fetch And Save The Wikipedia Article
topic = input("Topic: ")
while True:
    try:
        response = requests.get('https://en.wikipedia.org/wiki/' + topic)
        break
    except:
        print("Topic Not Found")
        topic = input("Topic: ")
    response.status_code
r = requests.post('https://facebook.com/post', data={'key': 'value'})
soup_obj = bs4.BeautifulSoup(response.text, 'lxml')
# The soup_obj will us to fetch the our required results
# To make our previous data more understandable we will use prettify() on soup_obj
soup_obj.prettify()
soup_obj.select('title')[0].getText()
links = soup_obj.find_all('p')
# find_all() will help to fetch all the details of the selected tag.
topicfile = open(topic + ".txt", "a+")
topicfile.write(str(links))
