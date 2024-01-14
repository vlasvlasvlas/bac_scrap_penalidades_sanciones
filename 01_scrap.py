import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def navigate_to_penalidades_page():
    driver = webdriver.Chrome()
    driver.get("https://www.buenosairescompras.gob.ar/")

    try:
        # Wait for the page to load
        home_page_loaded = EC.presence_of_element_located((By.CLASS_NAME, 'home-page-link-class'))
        WebDriverWait(driver, 10).until(home_page_loaded)

        # Find and click on the specific <a> element for "Penalidades y sanciones"
        penalidades_link = driver.find_element(By.XPATH, '//a[h4[text()="Penalidades y sanciones"]]')
        penalidades_link.click()

        # Wait for the new page to load (you might need to update the condition accordingly)
        penalidades_page_loaded = EC.presence_of_element_located((By.CLASS_NAME, 'pagination-gv'))
        WebDriverWait(driver, 10).until(penalidades_page_loaded)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return driver


def scrape_table(driver, page=1):
    data_list = []

    try:
        if page == 1:
            # Construct the URL with the page parameter
            page_url = f"https://www.buenosairescompras.gob.ar/ListarPenalidadesSanciones.aspx?Page={page}"
            driver.get(page_url)

        # Wait for the table to be present on the page
        table_present = EC.presence_of_element_located((By.ID, 'ctl00_CPH1_gridSanciones'))
        WebDriverWait(driver, 10).until(table_present)

        # Extract data from the table
        table = driver.find_element(By.ID, 'ctl00_CPH1_gridSanciones')
        rows = table.find_elements(By.TAG_NAME, 'tr')[1:]  # Start from index 1 to skip the header row

        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            data = [column.text.strip() for column in columns]
            data_list.append(data)

        # Load data into a DataFrame
        current_page_df = pd.DataFrame(data_list)
        print(f"Data loaded for page {page}:\n{current_page_df}")

        # Save data to a temporary CSV file
        temp_csv_filename = f'temp_data_page_{page}.csv'
        current_page_df.to_csv(temp_csv_filename, index=False, header=False ,mode='w' if page == 1 else 'a')  # Write mode for the first page, append mode for subsequent pages

        # Save data to a temporary CSV file
        full_csv_filename = f'full_data_pages.csv'
        current_page_df.to_csv(full_csv_filename, index=False, header=False ,mode='a')  # Write mode for the first page, append mode for subsequent pages



    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return pd.DataFrame(data_list)



# ... (your existing code)

def scrape_all_pages():
    driver = navigate_to_penalidades_page()

    try:
        # Loop to handle pagination
        page = 1
        while True:

            print("------> page: ", page)

            # Get the DataFrame for the current page
            current_page_df = scrape_table(driver, page)
            print("current_page_df: ", current_page_df)

            # Break if there are no more pages or DataFrame is empty
            if current_page_df is None or current_page_df.empty:
                break

            # Increment the page for the next iteration
            page += 1

            # Click on the next page link
            try:
                next_page_link = driver.find_element(By.XPATH, f'//a[contains(@href, "Page${page + 1}")]')
                next_page_link.click()

                # Wait for the new page to load
                time.sleep(4)  # Sleep to allow the new table to render
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'pagination-gv')))
                
                # Wait for the table to render
                time.sleep(4)

            except Exception as e:
                print(f"Could not click on the next page link: {str(e)}")
                break

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the browser window
        driver.quit()

    


if __name__ == "__main__":
    final_result_df = scrape_all_pages()

    # Print the resulting DataFrame
    print(final_result_df)