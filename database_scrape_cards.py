import time
import urllib.request  # Optional for image downloading

from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PokeLoader:
    url_filename = None
    url = None
    driver = None
    cards = []
    filter = ["code-card"]

    def __init__(self, create_dirs=True):
        self.url_filename = "poke_urls.txt"
        self.url = "https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&view=grid&ProductTypeName=Cards"

        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={UserAgent().random}")
        #chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def write_to_file(self):
        with open("links.txt", "w") as f:
            for result in self.cards:
                f.write(result + "\n")

    def link_in_filter(self, link):
        return any(string in link for string in self.filter)

    def scrape_pages(self, pages=1):
        for i in range(pages):
            self.scrape_links(i+1)
        self.write_to_file()

    def scrape_links(self, page=1):
        cards = []
        url = self.url.replace("page=1", "page={}".format(page))
        try:
            # Navigate to URL with a wait
            self.driver.get(url)
            try:
                element = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='search-result']"))
                )
                search_results = self.driver.find_elements(By.XPATH, "//div[@class='search-result']")
            except TimeoutException:
                print("Element not found")

            for result in search_results:
                link_element = result.find_element(By.TAG_NAME, "a")
                link = link_element.get_attribute("href")
                if not self.link_in_filter(link):
                    self.cards.append(link)

        except Exception as e:
            print(f"Error encountered: {e}")  # Handle potential errors

    def scrape_cards_from_links(self, load_from_txt=True):
        if load_from_txt:
            with open("links.txt", "r") as f:
                for line in f:
                    self.cards.append(line.strip())

        for card in self.cards:
            self.scrape_card(card)

    def scrape_card(self, link):
        try:
            self.driver.get(link)
            try:
                element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-details-container']")))
                # Card-Beschreibung (Name) extrahieren
                time.sleep(3)
                name = self.driver.find_element(By.XPATH, "//h1[@class='product-details__name']").text.replace('/'," ") #class="product-details__name"
                print(name)
                # Reihe und Nummer extrahieren
                number = self.driver.find_element(By.XPATH, "//ul[@class='product__item-details__attributes']/li[1]/div/span").text.replace('/'," ")
                print(number)
                img_link = self.driver.find_element(By.XPATH, "//div[@class='lazy-image__wrapper']/img").get_attribute("srcset")
                links = img_link.split(",")
                img_wide_link = links[len(links)-1].split(" ")[0]
                print(img_wide_link)
                filename = f"pokemon_cards/{name}##{number}.jpg"
                urllib.request.urlretrieve(img_wide_link, filename)
                print(f"Image saved: {filename}")

            except TimeoutException:
                print("Element not found")

        # app > div > div > section.marketplace__content > section > div.product-details-container > div.product-details__product > div > h1
        except Exception as e:
            print(f"Error encountered: {e}")  # Handle potential errors


if __name__ == "__main__":
    pokeloader = PokeLoader()
    #pokeloader.scrape_pages(1)
    pokeloader.scrape_cards_from_links(True)
