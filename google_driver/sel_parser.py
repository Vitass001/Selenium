from selenium import webdriver
from timer import timer
import time

url = "https://www.binance.com/ru/nft/marketplace?currency=BUSD&tradeType=0&keyword=Mobox+Avatar&page=1&rows=16&order=list_time%40-1"
driver = webdriver.Chrome(executable_path="C:\\Solenium\\google_driver\\chromedriver.exe", )

try:
    driver.get(url=url)
    timer(1, 40)


    def buy():
        try:
            # driver.get(url='https://www.binance.com/en/nft/goods/detail?productId=42578882&isProduct=1')
            time.sleep(1.5)
            buy_nft = driver.find_element_by_css_selector("div.css-1ate4o7").click()
            time.sleep(1)
            confirm = driver.find_element_by_css_selector("div.css-6xx5k5").click()
            time.sleep(4)
            driver.get(url=url)
        except:
            driver.get(url=url)
            pass
        finally:
            search_href_and_money()
            pass


    def search_href_and_money():
        pererva = 0
        while True:
            lich = 0
            money = driver.find_elements_by_class_name("css-rjqmed")
            href = [my_elem.get_attribute("href") for my_elem in
                    driver.find_elements_by_css_selector("div.css-vurnku > a")]
            zipped = zip(money, href)
            zipped_list = list(zipped)
            for mon, hrefs in zipped_list:

                lich += 1
                mon = (mon.text.strip().replace(',', '')[:-5])
                print(mon, hrefs)

                if float(mon) >= 2 and float(mon) <= 11.8:
                    driver.get(url=hrefs)
                    buy()

                elif lich == 16:
                    pererva += 1

                    if pererva == 40:
                        print('PERERVA\n------------------------------------------------')
                        time.sleep(30)
                        pererva = 0
                        driver.refresh()

                    driver.find_element_by_class_name('css-9z01gk').click()


    search_href_and_money()


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
