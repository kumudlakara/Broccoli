from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

driver = webdriver.Firefox()

driver.get("https://www.flipkart.com/")


products = []
prices = []
ratings = []
details = []
reviews = []
rams = []
roms = []
displays = []
cameraQ = []
probs = []

element_temp = driver.find_element_by_class_name('_2AkmmA')
action = ActionChains(driver)
action.click(on_element = element_temp)
action.perform()



element = driver.find_element_by_class_name('LM6RPg')
action = webdriver.ActionChains(driver)
#search_str = input('Enter item to search')
element.send_keys('phone')
#element.send_keys(Keys.DOWN)
element.send_keys(Keys.ENTER)
#time delay to allow the required new page to load
time.sleep(5)

element_popular = driver.find_element_by_class_name('_1xHtJz')
action = ActionChains(driver)
action.click(on_element = element_popular)
action.perform()


for i in range(0,5000, 24):
	time.sleep(5)
	content = driver.page_source
	soup = BeautifulSoup(content, features = 'html.parser')
	for a in soup.find_all('a', href = True, attrs = {'class':'_31qSD5'}):
		name = a.find('div', attrs ={'class':'_3wU53n'})
		price = a.find('div', attrs ={'class':'_1vC4OE'})
		rating = a.find('div', attrs ={'class' : 'hGSR34'})
		review = a.find('span', attrs = {'class' : "_38sUEc"})
		details = a.find_all('li', attrs = { 'class' : 'tVe95H'})
		memory = details[0]
		if(memory.text.split()[2] != 'RAM'):
			rams.append('')
			roms.append(memory.text.split()[0])
		else:
			rams.append(memory.text.split()[0])
			roms.append(memory.text.split()[4])

		display = details[1]
		camera = details[2]
		if i <1000 :
			prob = random.uniform(0.80,1)
		elif i >=1000 and i < 2000:
			prob = random.uniform(0.60, 0.85)
		elif i >= 2000 and i < 3000:
			prob = random.uniform(0.55, 0.75)
		elif i >= 3000 and i < 4000:
			prob = random.uniform(0.40, 0.65)
		else:
			prob = random.uniform(0,0.50)

		products.append(name.text.split('(')[0])
		prices.append((price.text)[1:])
		ratings.append(rating.text)
		reviews.append(review.text.split()[0])
		displays.append(display.text.split()[0])
		cameraQ.append((camera.text.split()[0])[:2])
		probs.append(prob)

	element_scroll = driver.find_element_by_tag_name('html')
	time.sleep(3)
	for _ in range(9):
		print("in loop")
		element_scroll.send_keys(Keys.PAGE_DOWN)
		time.sleep(1)
	time.sleep(3)
	element_next = driver.find_element_by_link_text('NEXT')
	action = ActionChains(driver)
	action.click(on_element = element_next)
	action.perform()

#print('prod:', products)

df = pd.DataFrame({'Product name' : products, 'Price' : prices, 'Ratings' : ratings, 
					'No of Ratings' : reviews, 'RAM' : rams, 'ROM' : roms, 'Display(cm)' : displays,
					'cameraQ(MP)' : cameraQ, 'Label' : probs})
df.to_csv('prod_phone.csv', index = False, encoding = 'utf-8')





