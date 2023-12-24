from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def main():
    
    driver = webdriver.Chrome()
    url = "https://pokemondb.net/pokedex/all"

    driver.get(url)
    table = driver.find_element(By.CLASS_NAME, "data-table")

    # Extract the table header
    header_elements = table.find_elements(By.TAG_NAME, "th")
    header = [header_element.text for header_element in header_elements]

    # Create an empty list to store rows
    rows = []

    # Extract table data rows
    data_rows = table.find_elements(By.TAG_NAME, "tr")
    for row_element in data_rows[1:]:
        data_cells = row_element.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in data_cells]
        rows.append(row_data)

    # Create a DataFrame from the rows
    df = pd.DataFrame(rows, columns=header)
    df.to_csv("Pokemon.csv",index=False)

    # Close the browser
    driver.close()

    # Print or manipulate the DataFrame as needed
    print(df)
    
    return

if __name__ == "__main__":
    main()
