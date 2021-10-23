from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

hits = 0
checks = 0

with open("names.txt", "r+", encoding='utf-8') as s:
    sx = s.readlines()
    for name in sx:
        browser = webdriver.Chrome(options=options)
        browser.get("https://opensea.io/" + name)
        try:
            browser.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div[2]/div[2]/div/button[1]")
            print("[TAKEN] " + name)
            checks = checks + 1
            browser.quit()
        except:
            print("[HIT] " + name)
            open('hits.txt','a+').write("{}".format(name))
            hits = hits + 1
            checks = checks + 1
            browser.quit()
    if hits > 1:
        print("\n\ndone checking, {} hits!".format(hits))
    elif hits == 1:
        print("\n\ndone checking, {} hit!".format(hits))
    elif hits == 0:
        print("\n\n done checking, no hits tho :(")

    time.sleep(10)
