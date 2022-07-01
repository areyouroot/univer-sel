

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyttsx3

# initialize Text-to-speech engine.
engine = pyttsx3.init()

text = "now we are going to automate Some of the browser functionalities this program can be helpful to test the browser which you have coded so sit back and take some snacks and enjoy"
engine.say(text)
# play the speech.
engine.runAndWait()

# convert this text to speech.
text = "now we are going to automate google search to and add the words in the existing search"
engine.say(text)
# play the speech.
engine.runAndWait()

#set chromodriver.exe path
driver = webdriver.Chrome(executable_path='C:/Users/abdul/Desktop/ppt/softy/chromedriver_win32 (1)/chromedriver.exe')
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.google.com/")
#identify search box
m = driver.find_element_by_name("q")
#enter search text
m.send_keys("BS abdur rahaman university")
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)
time.sleep(2)

m = driver.find_element_by_name("q")
#enter search text
m.send_keys(" crescent college")
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)
time.sleep(2)

m = driver.find_element_by_name("q")
#enter search text
m.send_keys(" information technology")
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)
time.sleep(5)

text = "now we are going to automate bing search "
engine.say(text)
# play the speech.
engine.runAndWait()


driver.get("https://www.bing.com/")
#identify search box
m = driver.find_element_by_name("q")
#enter search text
m.send_keys("BS abdur rahaman university")
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)
time.sleep(5)

text = "now we are going to automate the web Browsing so that we can visit some random websites"
engine.say(text)
# play the speech.
engine.runAndWait()

driver.get("https://www.youtube.com/")
time.sleep(2)

driver.get("https://crescent.education//")
time.sleep(2)

driver.get("https://www.facebook.com/")
time.sleep(2)

driver.get("https://www.github.com//")
time.sleep(2)

driver.get("https://www.amazon.in/")
time.sleep(2)

driver.get("https://theuselessweb.com/")
time.sleep(2)

driver.get("https://cant-not-tweet-this.com/")
time.sleep(2)

text = "thank you for enjoying the test "
engine.say(text)
# play the speech.
engine.runAndWait()