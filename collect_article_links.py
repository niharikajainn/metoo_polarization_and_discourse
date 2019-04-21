from selenium import webdriver
import time
import pickle

#Open initial URL with test browser
browser = webdriver.Chrome()
login_url = '[url_to_begin_search]'
browser.get(login_url)
time.sleep(1)

#login to library service
username = browser.find_element_by_id('siUsername_0')
username.send_keys('[your_username]')
password = browser.find_element_by_id('siPassword_0')
password.send_keys('[your_password]')
submit = browser.find_element_by_id('signInSubmitButton')
submit.click()
time.sleep(3)

#create a search query with word "#MeToo"
search = browser.find_element_by_xpath('//*[@id="product-level-nav"]/li[1]/a')
search_link = search.get_attribute('href')
browser.get(search_link)
search_term = browser.find_element_by_id('searchTerm')
search_term.send_keys('"#MeToo"')
submit = browser.find_element_by_id('expandedSearch')
submit.click()

#filter to only include news articles (i.e. no editorials)
browser.find_element_by_xpath('//*[@id="objectype-header"]').click()
time.sleep(1)
news = browser.find_element_by_xpath('//*[@id="filter_objectype"]')
news.click()

#loop through all results pages and save links to articles
for i in range(6):
    titles = browser.find_elements_by_class_name('previewTitle')
    links = [i.get_attribute('href') for i in titles]
    websites += links

    curr_url = browser.current_url
    next_url = curr_url[:-16] + str(i+2) + curr_url[-15:]
    browser.get(next_url)
    browser.quit()

    print(websites)
    with open("links_metoo.txt", "wb") as f:
    pickle.dump(websites, f)
    f.close()
