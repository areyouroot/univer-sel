from selenium import webdriver
from csv import reader
import time

contacts =[]
with open('contacts.csv',"r") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        contacts.append(row[0])

driver = webdriver.Chrome(executable_path='C:/Users/abdul/Desktop/ppt/softy/chromedriver_win32 (1)/chromedriver.exe')
driver.get("https://web.whatsapp.com/")

while True:
			
	for name in contacts:
		time.sleep(3)
		try:
			user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
			user.click()


			sendbtn.click()
		except Exception as e:
			# print('Keep Scrolling Your whatsapp Contacts')
			pass  
		else :
			print('Successfully msg sent to',name)
			print(len(contacts)-1, 'more msgs left to send')
			contacts.remove(name)

	if(len(contacts)==0):
		break

driver.close()

