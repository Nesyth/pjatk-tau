from curses import KEY_ENTER
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

url1 = "https://zalando.pl"
url2 = "https://allegro.pl"

driverFirefox = webdriver.Firefox(executable_path="geckodriver")
driverChrome = webdriver.Chrome(executable_path="chromedriver")

# Scenario 1.1
logger.info("Przechodzę na stronę zalando...")
driverChrome.get("https://zalando.pl")

logger.info("Maksymalizuje okno...")
driverChrome.maximize_window()

logger.info("Szukam powiadomienia o ciasteczekach...")
time.sleep(2)
driverChrome.find_element(by=By.XPATH, value='//*[@id="uc-btn-accept-banner"]').click()

logger.info("Przechodzę do działu dla mężczyzn...")
driverChrome.find_element(by=By.XPATH, value='//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/nav/ul/li[2]/a').click()

logger.info("Przechodzę do obuwia...")
driverChrome.find_element(by=By.XPATH, value='//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[2]/nav/ul/li[4]/span/a').click()

logger.info("Klikam dropdown...")
driverChrome.find_element(by=By.XPATH, value='//*[@id="collection_view_catalog-filters"]/div[1]/div/div/button').click()

logger.info("Wybieram nowości...")
dropdown = driverChrome.find_element(by=By.XPATH, value='//*[@id="sorting-NEW_IN"]')
driverChrome.execute_script("arguments[0].click();", dropdown)

logger.info("Sukces!")
time.sleep(4)

# Scenario 1.2
logger.info("Przechodzę na stronę zalando...")
driverChrome.get("https://zalando.pl")

logger.info("Maksymalizuje okno...")
driverChrome.maximize_window()
driverChrome.implicitly_wait(1000)

logger.info("Wpisuje email...")
driverChrome.find_element(by=By.XPATH, value='//*[@id="email-input"]').send_keys("selenium@gmail.com")
time.sleep(1)

logger.info("Zaznaczam preferencje...")
radio = driverChrome.find_element(by=By.XPATH, value='//*[@id="category-2"]')
driverChrome.execute_script("arguments[0].click();", radio)

logger.info("Zapisuje...")
submit = driverChrome.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div/div/div/div[2]/div/div/form/div/div/div[5]/button')
driverChrome.execute_script("arguments[0].click();", submit)

logger.info("Sukces!")
time.sleep(4)
driverChrome.quit()

# Scenario 2.1
logger.info("Przechodzę na stronę TMDB...")
driverFirefox.get("https://www.themoviedb.org/")

logger.info("Maksymalizuje okno...")
driverFirefox.maximize_window()
driverFirefox.implicitly_wait(1000)

logger.info("Przechodzę do sekcji logowania...")
driverFirefox.find_element(by=By.XPATH, value='/html/body/div[1]/header/div[1]/div/div[2]/ul/li[3]/a').click()

logger.info("Wpisuje email...")
driverFirefox.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys("selenium@gmail.com")

logger.info("Wpisuje hasło...")
driverFirefox.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys("Selenium@123")

logger.info("Logowanie...")
driverFirefox.find_element(by=By.XPATH, value='//*[@id="login_button"]').click()

tmdbError = driverFirefox.find_element(by=By.XPATH, value='/html/body/div[1]/main/section/div/div/div/div/div/a/h2/span').text
logger.error(tmdbError)
time.sleep(4)

# Scenario 2.2
logger.info("Przechodzę na stronę TMDB...")
driverFirefox.get("https://www.themoviedb.org/")

logger.info("Maksymalizuje okno...")
driverFirefox.maximize_window()
driverFirefox.implicitly_wait(1000)

logger.info("Wpisuje nazwe filmu...")
driverFirefox.find_element(by=By.XPATH, value='//*[@id="inner_search_v4"]').send_keys("Interstellar")

logger.info("Wyszukuję film...")
driverFirefox.find_element(by=By.XPATH, value='//*[@id="inner_search_form"]/input').click()

logger.info("Przechodzę do pierwszego filmu..")
driverFirefox.find_element(by=By.XPATH, value='/html/body/div[1]/main/section/div/div/div[2]/section/div[1]/div/div[1]/div/div[2]/div[1]/div/div/a').click()

logger.info("Odpalam zwiastun...")
driverFirefox.find_element(by=By.XPATH, value='/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/ul/li[6]/a').click()

logger.info("Sukces!")
time.sleep(4)
driverFirefox.quit()
