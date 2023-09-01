from seleniumwire import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv


def linkGrabber(htmlSegment):
    splitSegment = htmlSegment.split('"')
    return ("https://www.facebook.com" + splitSegment[3])


def link_modifier():

    makers = ["Acura",
              "Alfa_Romeo",
              # "Aston_Martin",
              # "Audi",
              # "BMW",
              # "Bentley",
              # "Bmw_Alpina",
              # "Buick",
              # "Cadillac",
              # "Chevrolet",
              # "Chrysler",
              # "Citroen",
              # "Daimler",
              # "Dodge",
              # "Daihatsu",
              # "Ferrari",
              # "Fiat",
              # "Ford",
              # "Gmc",
              # "Hino",
              # "Hummer",
              # "Hyundai",
              # "Infiniti",
              # "Jaguar",
              # "Jeep",
              # "Kawasaki",
              # "Komatsu",
              # "Kubota",
              # "Lamborghini",
              # "Lancia",
              # "Land_Rover",
              # "Lexus",
              # "Lincoln",
              # "Lotus",
              # "Mazda",
              # "Mitsubishi",
              # "Maserati",
              # "Mercedes-Benz",
              # "Mg",
              # "Mini",
              # "Mitsuoka",
              # "Nissan_Diesel_%28ud%29",
              # "Opel",
              # "Peugeot",
              # "Porsche",
              # "Renault",
              # "Rolls Royce",
              # "Nissan",
              # "Rover",
              # "Saab",
              # "Smart",
              # "Sumitomo",
              # "Tesla",
              # "VW",
              # "Volvo",
              # "Yamaha",
              # "Honda",
              # "Isuzu",
              # "Subaru",
              # "Suzuki",
              # "Toyota",
              "Yanmar"]
    url = "http://japexp.jthing.com/browse/auction/all/"
    url_list = []
    for make in makers:
        url1 = str(url) + make
        url_list.append(url1)
    return url_list

def maker_grabber():
    if __name__ == '__main__':

        url = "http://japexp.jthing.com/browse/auction/all/"
        linkes = link_modifier()
        candidates = []
        containerSplit = []
        tempLinkHolder = []
        package = []
        packages = []

        options = webdriver.ChromeOptions()
        # options.add_argument('--proxy-server=185.130.105.109:10017')

        browser = uc.Chrome(
            options=options,
        )

        browser.get(url)

        # browser.find_elements(By.XPATH, "//input[contains(@autofocus, 'autofocus')]").send_keys('tsurikawa')
        # // input[contains( @ style, 'width:125px; font-size:14px' )]

        time.sleep(30)

        for link in linkes:
            browser.get(link)

            containers = browser.find_elements(By.XPATH, "//a[contains(@title, 'Cars models that begin with ')]")
            # browser.find_elements(By.XPATH, "//a[contains(@title, 'See all models ')]")

            for container in containers:
                tempLinkHolder.append(container.get_attribute("innerHTML"))

            for container in containers:
                candidates.append(container.text)

            i = 0

            for containerText in candidates:
                containerSplit.append(containerText.split())
                for dataPlural in containerSplit:
                    i += 1
                    j = 0
                    recognized = False
                    package.append(dataPlural)
                    package[len(package) - 1].append(tempLinkHolder[i - 1])
                i = 0
            i = 0
            return package

            i = 0
            packages.append(package)

        return packages

        browser.close()

print(maker_grabber())