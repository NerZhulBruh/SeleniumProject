from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

def scrape_exhibitions():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-extensions")

    url = 'https://www.hermitagemuseum.org/wps/portal/hermitage/what-s-on/?lng=ru'

    with webdriver.Chrome(options=options) as driver:
        try:
            driver.get(url)

            wait = WebDriverWait(driver, 10)
            exhibitions = []

            while True:
                exhibition_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'her-list-item')))

                for item in exhibition_items:
                    try:
                        title = item.find_element(By.TAG_NAME, 'h3').text
                        date = item.find_element(By.CLASS_NAME, 'her-list-date').text
                        description = item.find_element(By.TAG_NAME, 'p').text
                        exhibitions.append({
                            'Title': title,
                            'Date': date,
                            'Description': description
                        })
                    except Exception as e:
                        print(f"Error extracting data: {e}")

                try:
                    next_button = driver.find_element(By.CLASS_NAME, 'next-page')
                    if next_button.is_enabled():
                        next_button.click()
                    else:
                        break
                except Exception as e:
                    print(f"No next button found: {e}")
                    break

            with open('hermitage_exhibitions.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Title', 'Date', 'Description']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for exhibition in exhibitions:
                    writer.writerow(exhibition)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_exhibitions()