import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Replace with the URL of the product you want to scrape
product_url = "https://www.flipkart.com/samsung-galaxy-s22-5g-green-128-gb/product-reviews/itm92c75094f3b93?pid=MOBGGG2YKYPWPCNP&lid=LSTMOBGGG2YKYPWPCNPJQJIS6&marketplace=FLIPKART"
# Initialize the Selenium webdriver with your chosen browser driver
driver = webdriver.Chrome(executable_path="C:\\Users\\LENOVO\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

# Open the product URL
driver.get(product_url)

# Scroll down to load more reviews (change the range according to the number of reviews you want)
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)  # Wait for the page to load

# Get the page source after loading all reviews
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the review elements using BeautifulSoup
review_elements = soup.find_all('div', {'class': '_1AtVbE'})

# Extract and print the reviews
for review in review_elements:
    try:
        review_text = review.find('div', {'class': 't-ZTKy'}).text
        print(review_text)
    except AttributeError:
        print(" ")

# Close the browser
driver.quit()
