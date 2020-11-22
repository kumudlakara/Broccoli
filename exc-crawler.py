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

element_temp = driver.find_element_by_class_name('_2KpZ6l')
action = ActionChains(driver)
action.click(on_element = element_temp)
action.perform()



element = driver.find_element_by_class_name('_3704LK')
action = webdriver.ActionChains(driver)
#search_str = input('Enter item to search')
element.send_keys('phone')
#element.send_keys(Keys.DOWN)
element.send_keys(Keys.ENTER)
#time delay to allow the required new page to load
time.sleep(5)

element_popular = driver.find_element_by_class_name('_10UF8M')
action = ActionChains(driver)
action.click(on_element = element_popular)
action.perform()


for i in range(0,840, 24):
	time.sleep(5)
	content = driver.page_source
	soup = BeautifulSoup(content, features = 'html.parser')
	for a in soup.find_all('a', href = True, attrs = {'class':'_1fQZEK'}):
		name = a.find('div', attrs ={'class':'_4rR01T'})
		print(name.text)
		namestr = name.text
		if "Guru" in namestr :
			products.append(name.text.split('(')[0])
			prices.append('0')
			ratings.append('0')
			reviews.append('0')
			displays.append('0')
			cameraQ.append('0')
			probs.append(-1)
			roms.append('0')
			rams.append('0')
		elif "Lava" in namestr :
			products.append(name.text.split('(')[0])
			prices.append('0')
			ratings.append('0')
			reviews.append('0')
			displays.append('0')
			cameraQ.append('0')
			probs.append(-1)
			roms.append('0')
			rams.append('0')
		elif "Nokia" in namestr :
			products.append(name.text.split('(')[0])
			prices.append('0')
			ratings.append('0')
			reviews.append('0')
			displays.append('0')
			cameraQ.append('0')
			probs.append(-1)
			roms.append('0')
			rams.append('0')
		elif "Kechaoda" in namestr :
			products.append(name.text.split('(')[0])
			prices.append('0')
			ratings.append('0')
			reviews.append('0')
			displays.append('0')
			cameraQ.append('0')
			probs.append(-1)
			roms.append('0')
			rams.append('0')
		elif "Chilli" in namestr :
			products.append(name.text.split('(')[0])
			prices.append('0')
			ratings.append('0')
			reviews.append('0')
			displays.append('0')
			cameraQ.append('0')
			probs.append(-1)
			roms.append('0')
			rams.append('0')
		elif "Easyfone" in namestr :
			products.append(name.text.split('(')[0])
			prices.append('0')
			ratings.append('0')
			reviews.append('0')
			displays.append('0')
			cameraQ.append('0')
			probs.append(-1)
			roms.append('0')
			rams.append('0')
		elif "Eco" in namestr :
			products.append(name.text.split('(')[0])
			prices.append('0')
			ratings.append('0')
			reviews.append('0')
			displays.append('0')
			cameraQ.append('0')
			probs.append(-1)
			roms.append('0')
			rams.append('0')
		elif "JIVI" in namestr :
			products.append(name.text.split('(')[0])
			prices.append('0')
			ratings.append('0')
			reviews.append('0')
			displays.append('0')
			cameraQ.append('0')
			probs.append(-1)
			roms.append('0')
			rams.append('0')

		else:
			price = a.find('div', attrs ={'class':'_30jeq3'})
			rating = a.find('div', attrs ={'class' : '_3LWZlK'})
			review = a.find('span', attrs = {'class' : '_2_R_DZ'})
			details = a.find_all('li', attrs = { 'class' : 'rgWa7D'})
			memory = details[0]
			if(memory.text.split()[2] != 'RAM'):
				rams.append('')
				roms.append(memory.text.split()[0])
			elif memory.text.split()[1] != 'GB':
				rams.append(float(memory.text.split()[0])/1000)
				roms.append(float(memory.text.split()[4])/1000)
			else:
				rams.append(memory.text.split()[0])
				roms.append(memory.text.split()[4])

			display = details[1]
			camera = details[2]
			if i <120 :
				prob = random.uniform(0.80,1)
			elif i >=120 and i < 360:
				prob = random.uniform(0.60, 0.85)
			elif i >= 360 and i < 576:
				prob = random.uniform(0.55, 0.75)
			elif i >= 576 and i < 696:
				prob = random.uniform(0.40, 0.65)
			else:
				prob = random.uniform(0, 0.50)

			products.append(name.text.split('(')[0])
			prices.append((price.text)[1:])
			if(not rating):
				ratings.append('0')
			else:
				ratings.append(rating.text)
			if(not review):
				reviews.append('0')
			else:
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
	for _ in range(4):
		element_scroll.send_keys(Keys.DOWN)
		element_scroll.send_keys(Keys.DOWN)
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

print('File saved!')




