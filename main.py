from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time

def take_partial_screenshots(url):
    # Set up the Chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the webpage
        driver.get(url)
        time.sleep(2)  # Wait for the page to load (adjust as needed)

        # Get the height of the entire webpage
        total_height = driver.execute_script("return document.body.scrollHeight")

        # Set the viewport width and height
        viewport_width = 1200
        viewport_height = 800

        # Take partial screenshots
        scroll_position = 0
        screenshot_index = 1

        while scroll_position < total_height-900:
            # Set the dimensions of the viewport to capture
            driver.set_window_size(viewport_width, viewport_height)

            # Scroll to the current position
            driver.execute_script(f"window.scrollTo(0, {scroll_position});")

            # Wait briefly for content to settle
            time.sleep(1)

            # Capture screenshot of the current viewport
            screenshot_path = f"screenshot_{screenshot_index}.png"
            driver.save_screenshot(screenshot_path)

            # Increment scroll position
            scroll_position += viewport_height - 100

            # Increment screenshot index
            screenshot_index += 1

    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    # Ask user for the website URL
    url = input("Enter the URL of the website: ").strip()

    # Check if the URL is valid
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url  # Prepend "http://" if missing

    # Take partial screenshots
    take_partial_screenshots(url)

    print("Screenshots saved successfully.")

