"""
The following bit of code will open a webpage, scroll down to the very bottom and copy all the text for you

Copied text will then be saved into a json file you name
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scroll_down_webpage(driver):
    """Scrolls to the bottom of the page to load all dynamic content."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def main(url):
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

        scroll_down_webpage(driver)

        print("\nExtracted text:\n")
        print(text)

        input("\nPress Enter to close the browser and exit...")  # Keeps browser open until user confirms

    finally:
        return url
        driver.quit()

"""
-----------------------------------------------------------
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
        # driver.quit()
        pass



if __name__ == "__main__":
    url = input("Enter the URL: ")
    text = extract_full_text(url)
    main(url)

    print("\nExtracted text:\n")
    print(text)