from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def main():
    driver=webdriver.Chrome()
    url="https://pokemondb.net/pokedex/all"
    driver.get(url)
    table=driver.find_element(By.CLASS_NAME,"data-table")
    header=table.find_elements(By.TAG_NAME,"th")
    header_data=[headers.text for headers in header]
    
    rows=[]
    data_rows=table.find_elements(By.TAG_NAME,"tr")
    for row_element in data_rows[1:]:
        data_cells=row_element.find_elements(By.TAG_NAME,"td")
        row_data=[cell.text for cell in data_cells]
        rows.append(row_data)
        
    df=pd.DataFrame(rows,columns=header_data)
    df.to_csv("Pokemon.csv",index=False)
    print(df)
    
    # time.sleep(10)
    driver.close()
    return

if __name__=="__main__":
    main()