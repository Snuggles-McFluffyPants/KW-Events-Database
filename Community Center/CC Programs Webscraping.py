"""
The following bit of code will open a webpage, scroll down to the very bottom and copy all the text for you

Copied text will then be saved into a json file you name
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

"""
Opens a webpage and scrolls all the way to the bottom

This function does also return the text from the webpage
"""
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

        print("\nExtracted text:\n")
        print(text)

        # input("\nPress Enter to close the browser and exit...")  # Keeps browser open until user confirms

    finally:
        return url
        driver.quit()

"""
Returns text from a webpage
"""
def extract_full_text(url):
    # Set up Chrome in headless mode
    options = Options()
    options.headless = True

    # Start the driver
    driver = webdriver.Chrome(options=options)

    try:
        # Load the page
        driver.get(url)

        # Wait for JavaScript to load (increase if necessary)
        time.sleep(5)

        # Extract visible text
        text = driver.find_element("tag name", "body").text
        return text
    finally:
        driver.quit()
        pass



if __name__ == "__main__":
    # url = input("Enter the URL: ")

    # Full list of community center programs
    # url = "https://anc.ca.apm.activecommunities.com/activekitchener/activity/search?onlineSiteId=0&locale=en-US&activity_select_param=2&viewMode=list"

    # Partial list of community center programs
    url = "https://anc.ca.apm.activecommunities.com/activekitchener/activity/search?onlineSiteId=0&locale=en-US&activity_select_param=2&center_ids=2&center_ids=129&center_ids=4&center_ids=9&center_ids=158&center_ids=81&viewMode=list"
    text = extract_full_text(url)
    scroll_down_webpage(url)

    # file_name = input("Enter json filename: ")
    file_name = "Kitchener_CC_Programs"

    with open(file_name,'w') as write_file:
        json.dump(text, write_file,indent=4)

    json_str = json.dumps(text, indent=4)

    print("\nHere's your text you bastard\n")
    print(text)