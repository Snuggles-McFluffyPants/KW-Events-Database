import requests
from urllib.robotparser import RobotFileParser

def check_scraping_permission(url):
    """
    Checks if a website allows scraping based on its robots.txt file.

    Args:
        url (str): The base URL of the website (e.g., "https://www.example.com").

    Returns:
        tuple: A tuple containing:
            - bool: True if scraping is allowed for the given URL path, False otherwise.
            - str: A message indicating the result.
    """
    robots_url = f"{url}/robots.txt"
    rp = RobotFileParser()

    try:
        rp.set_url(robots_url)
        rp.read()
    except Exception as e:
        return False, f"Could not read robots.txt or an error occurred: {e}"

    # Check if a specific URL path is allowed for a user-agent (e.g., "*")
    # You can replace "*" with a specific user-agent if desired.
    path_to_check = "/"  # Check the root path, or a specific path you intend to scrape
    if rp.can_fetch("*", path_to_check):
        return True, f"Scraping appears to be allowed for '{path_to_check}' according to robots.txt."
    else:
        return False, f"Scraping for '{path_to_check}' is disallowed by robots.txt."

# # Example usage:
# website_url = "https://www.google.com"  # Replace with the target website URL
# allowed, message = check_scraping_permission(website_url)
# print(message)
#
# website_url_2 = "https://www.amazon.com"
# allowed_2, message_2 = check_scraping_permission(website_url_2)
# print(message_2)

if __name__ == "__main__":
    website_url = input("Enter website url to check for scraping permission:\n")
    allowed, message = check_scraping_permission(website_url)

    print(f"Webscraping permissions for {website_url}")
    print(message)