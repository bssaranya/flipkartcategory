from bs4 import BeautifulSoup
import requests
import re
import json

r = requests.get('https://www.flipkart.com/')

src=r.text
soup = BeautifulSoup(src,'lxml')


main_categories = {}

diclist = []
maindiv = soup.select('._1GTrm1')

url = 'https://www.flipkart.com/'

for div in maindiv:
    for x in div.select('._2oyLgr'):
        headlist=[]
        head = x.text+'\n'
        headlist.append(head)
        # print(headlist)
       

    for x in div.select('._3CuAg8'):
        products = []
        productlink = x.attrs['href']
        full_link = url + str(productlink)
        products.append(full_link)
        # print(products)


        main_categories={
            'head':head,
            'productlink':full_link
        }
        diclist.append(main_categories)
        print(main_categories)


json_text = json.dumps(diclist,indent=4)
with open('flipkartcategory.json', 'w') as json_file:
    json_file.write(json_text)
