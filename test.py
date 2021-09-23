
"""

l_size = input("Wpisz wielkosc")
my_arr = []
for _ in range(int(l_size)):  # _ nic nie znaczy oprócz konwencji że nie będzie używane to
  my_arr += [randint(0,20)] # można tak
  # my_arr.append(randint(20)) # to samo
print(my_arr)

"""
"""
from msvcrt import getch
while True:
    print(ord(getch()))
"""
import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")


for balancedHeadline in soup.find_all(class_="balancedHeadline"): 
    if balancedHeadline.a: 
        print(balancedHeadline.a.text.replace("\n", " ").strip())
    else: 
        print(balancedHeadline.contents[0].strip())
      