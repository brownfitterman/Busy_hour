#Importing libraries 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time 
import string
import openpyxl
import os

#Loading Selenium Webdriver 
driver= webdriver.Firefox()
wait = WebDriverWait(driver, 5)

#Opening Google maps 
driver.get("https://www.google.com/maps")
time.sleep(3)

#Closing the google consent form 
widget=driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(widget)
button=driver.find_element_by_xpath('.//*[@id="introAgreeButton"]')
button.click()

#Finding the search box 
driver.switch_to_default_content()
searchbox=driver.find_element_by_id('searchboxinput')
location= "Málaga"
searchbox.send_keys(location)
searchbox.send_keys(Keys.ENTER)
time.sleep(2)
cancelbut=driver.find_element_by_class_name('gsst_a')
cancelbut.click()
searchbox.send_keys("seguro")
searchbox.send_keys(Keys.ENTER)
time.sleep(3)

#Locating the results section 
entries=driver.find_elements_by_class_name('section-result')


#Prepare the excel file using the Openpyxl  
wb= openpyxl.load_workbook("comapnies.xlsx")
sheetname=wb.get_sheet_names()[0]
sheet=wb[sheetname]
sheet.title ="companies"


#Extracting the information from the results  
for entry in entries:
    #Empty list 
    labels=[]
    #Extracting the Name, adress, Phone, and website:
    
    name= entry.get_attribute("aria-label")
    adress= entry.find_element_by_class_name('section-result-location').text
    phone = entry.find_element_by_class_name('section-result-hours-phone-container').text.split(' · ')[-1]
    try:
        webcontainer= entry.find_element_by_class_name('section-result-action-container')
        website=entry.find_element_by_tag_name('a').get_attribute("href")
    except NoSuchElementException:
        website="No website could be found"
    print (name)
    print (website)
       

    #Try/except  to write the extracted info in the Excel file pass if doessn't exist 
    try:
        sheet.append([location,name,adress,phone,website])
    except IndexError:
        pass

 
#saving the excel file 
wb.save("companies.xlsx")