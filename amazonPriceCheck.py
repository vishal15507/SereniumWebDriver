import smtplib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path="D:\\softwares\\Development chrome driver\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")

driver.get("https://www.amazon.com/Surround-Headphones-Omni-Directional-Reduction-Microphone/dp/B095NZ7ZGP/ref=sr_1_1_sspa?keywords=gaming+headsets&pd_rd_r=87699987-acd6-47a1-9c7b-ff3a38d3c601&pd_rd_w=Coc8G&pd_rd_wg=qrvwr&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=WYGPJJEHCBFYPDD6AF19&qid=1644672250&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFYVU1LU0cyWUpUVzcmZW5jcnlwdGVkSWQ9QTAxMTQ3OTczRVkzVzEzOE1YNlBYJmVuY3J5cHRlZEFkSWQ9QTA3NDEyMjgzT1QwTEdJVTVNNzAxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
priceText=(driver.find_element(By.ID,"price_inside_buybox").text)
price=float(priceText.split("$")[1])
print(price)
# check lowest price from camelcamelcamel.com
price=20
if price <=22:
    print("price less than 22")

else:
    print("price still high: ",price)



driver.close()