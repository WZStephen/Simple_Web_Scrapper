import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class Review:
	def __init__(self, date, role, gotOffer, experience, difficulty, length, details, questions):
		self.date = date
		self.role = role
		self.gotOffer = gotOffer
		self.experience = experience
		self.difficulty = difficulty
		self.length = length
		self.details = details
		self.questions = questions

username = "wzhao42@asu.edu" # your email here
password = "choushabi123" # your password here

# Manual options for the company, num pages to scrape, and URL
pages = 10
companyName = "microsoft"
companyURL = "https://www.glassdoor.com/Interview/Microsoft-Software-Development-Engineer-Interview-Questions-EI_IE1651.0,9_KO10,39.htm"

def obj_dict(obj):
	return obj.__dict__

def json_export(data):
	jsonFile = open(companyName + ".json", "w")
	jsonFile.write(json.dumps(data, indent=4, separators=(',', ': '), default=obj_dict))
	jsonFile.close()

def init_driver():
	#driver = webdriver.Chrome(executable_path = "chromedriver.exe") # Windows
	driver = webdriver.Chrome(executable_path = "/Users/weichizhao/Projects/Simple_Web_Scrapper/chromedriver") # MacOS
	driver.wait = WebDriverWait(driver, 10)
	return driver

def login(driver, username, password):
	driver.get("http://www.glassdoor.com/profile/login_input.htm")
	try:
		user_field = driver.wait.until(EC.presence_of_element_located((By.NAME, "username")))
		pw_field = driver.find_element_by_id("userPassword")
		login_button = driver.find_element_by_class_name("gd-ui-button")
		user_field.send_keys(username)
		user_field.send_keys(Keys.TAB)
		time.sleep(1)
		pw_field.send_keys(password)
		time.sleep(1)
		login_button.click()
	except TimeoutException:
		print("TimeoutException! Username/password field or login button not found on glassdoor.com")

def parse_reviews_HTML(reviews, data):
	for review in reviews:
		length = "-"
		gotOffer = "-"
		experience = "-"
		difficulty = "-"
		date = review.find("time", { "class" : "date" }).getText().strip()
		role = review.find("span", { "class" : "reviewer"}).getText().strip()
		outcomes = review.find_all("div", { "class" : ["tightLt", "col"] })
		if (len(outcomes) > 0):
			gotOffer = outcomes[0].find("span", { "class" : "middle"}).getText().strip()
		if (len(outcomes) > 1):
			experience = outcomes[1].find("span", { "class" : "middle"}).getText().strip()
		if (len(outcomes) > 2):
			difficulty = outcomes[2].find("span", { "class" : "middle"}).getText().strip()
		appDetails = review.find("p", { "class" : "applicationDetails"})
		if (appDetails):
			appDetails = appDetails.getText().strip()
			tookFormat = appDetails.find("took ")
			if (tookFormat >= 0):
				start = appDetails.find("took ") + 5
				length = appDetails[start :].split('.', 1)[0]
		else:
			appDetails = "-"
		details = review.find("p", { "class" : "interviewDetails"})
		if (details):
			s = details.find("span", { "class" : ["link", "moreLink"] })
			if (s):
				s.extract() # Remove the "Show More" text and link if it exists
			details = details.getText().strip()
		questions = []
		qs = review.find_all("span", { "class" : "interviewQuestion"})
		if (qs):
			for q in qs:
				s = q.find("span", { "class" : ["link", "moreLink"] })
				if (s):
					s.extract() # Remove the "Show More" text and link if it exists
				questions.append(q.getText().encode('utf-8').strip())
		r = Review(date, role, gotOffer, experience, difficulty, length, details, questions)
		data.append(r)
	return data

def get_data(driver, URL, startPage, endPage, data, refresh):
	if (startPage > endPage):
		return data
	print("\nPage " + str(startPage) + " of " + str(endPage))
	currentURL = URL + "_IP" + str(startPage) + ".htm"
	time.sleep(2)
	if (refresh):
		driver.get(currentURL)
		print("Getting " + currentURL)
	time.sleep(2)
	HTML = driver.page_source
	soup = BeautifulSoup(HTML, "html.parser")
	reviews = soup.find_all("li", { "class" : ["empReview", "padVert"] })
	if (reviews):
		data = parse_reviews_HTML(reviews, data)
		print ("Page " + str(startPage) + " scraped.")
		if (startPage % 10 == 0):
			print("\nTaking a breather for a few seconds ...")
			time.sleep(10)
		get_data(driver, URL, startPage + 1, endPage, data, True)
	else:
		print("Waiting ... page still loading or CAPTCHA input required")
		time.sleep(3)
		get_data(driver, URL, startPage, endPage, data, False)
	return data

if __name__ == "__main__":
	driver = init_driver()
	time.sleep(3)
	print ("Logging into Glassdoor account ...")
	login(driver, username, password)
	time.sleep(5)
	print ("\nStarting data scraping ...")
	data = get_data(driver, companyURL[:-4], 1, pages, [], True)
	print ("\nExporting data to " + companyName + ".json")
	json_export(data)
	driver.quit()