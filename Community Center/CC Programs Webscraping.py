"""
The following bit of code will open a webpage, scroll down to the very bottom and copy all the text for you

Copied text will then be saved into a json file you name
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

"""
Opens a webpage and scrolls all the way to the bottom

This function does also return the text from the webpage
"""

# Opens a webpage and scolls all the way to the bottom
#   For websites that don't allow webscraping
def scroll_down_webpage(url):
    # Set Chrome options (not headless so the browser stays visible)
    options = Options()
    options.add_experimental_option("detach", True)  # Keep browser open after script ends

    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print("Error launching ChromeDriver. Make sure it's installed and in PATH.")
        print(f"Details: {e}")
        return

    try:
        driver.get(url)
        time.sleep(2)  # Give initial load time

        # scroll_down_webpage(driver)

        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new content to load
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # input("\nPress Enter to close the browser and exit...")  # Keeps browser open until user confirms

    finally:
        # return text
        driver.quit()

# Extracts and returns text from a webpage
#   For websites that allow webscraping
def extract_full_text_with_scroll(url):
    # Set Chrome options (non-headless so content loads fully)
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(3)  # Initial load

        # Scroll down until you can't anymore
        SCROLL_PAUSE_TIME = 2
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        time.sleep(3)  # Wait to ensure all content is loaded

        # Now grab the text
        full_text = driver.find_element(By.TAG_NAME, "body").text
        return full_text

    finally:
        driver.quit()

#Specify a filename
def text_to_json(filename, text):
    # Write to a json file
    with open(filename, 'w') as write_file:
        json.dump(text, write_file, indent=4)

    json_str = json.dumps(text, indent=4)

def text_to_txt(filename, text):
    with open(filename, "w") as f:
        f.write(text)


if __name__ == "__main__":
    url = "https://anc.ca.apm.activecommunities.com/activekitchener/activity/search?onlineSiteId=0&locale=en-US&activity_select_param=2&viewMode=list"

    full_text = extract_full_text_with_scroll(url)
    text_to_json("Kitchener_CC_Programs", full_text)
