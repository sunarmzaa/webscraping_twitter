from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup

driver = webdriver.Chrome()


def HashTag(keyword):

	url = 'https://twitter.com/hashtag/' + keyword

	driver.get(url)


	page_html = driver.page_source

	data = soup(page_html, 'html.parser')

	tweetext = data.findAll('p',{'class':'TweetTextSize'})
	

	for i,tw in enumerate(tweetext):
		print(i+1)
		print(tw,Text)
HashTag('หนุ่มแว่นหัวร้อน')        