from selenium import webdriver
import time
import csv
file_path = 'my-cli/cli-pal/events.csv'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
 

def mark_event(file_path): 

    # Set up the driver for Chrome
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1200x600")
    # Load the login page for Google Calendar
    driver.get("https://calendar.google.com/calendar/r")

    input("Press enter after logging in...")

    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Extract the date and event from the row
            date = row[0]
            event = row[1]
            
            # Click the "Create" button to add a new event
            create_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Create')]"))
            )
            create_button.click()
            

            event_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Event')]"))
            )
            time.sleep(4)
            event_button.click()

            time.sleep(2)
            event_name_input = WebDriverWait(driver,40).until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Add title']"))
            )
            time.sleep(1)

            event_name_input.send_keys(event)
            time.sleep(3)
            startdatebutton = WebDriverWait(driver,55).until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Start date']"))
            )
            
            startdatebutton.click()
            # datebutton = WebDriverWait(driver,60).until(
            #     EC.presence_of_all_elements_located((By.XPATH, "//span[@data-date='{}']".format(date)))
            # )
            # for i in datebutton:
            #     if i.is_enabled ():
            #         i.click()
            time.sleep(3)

            save_button = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//div/span[contains(text(), 'Save')]"))
            )
            time.sleep(1)
            save_button.click()
            
            time.sleep(1)
        driver.quit()