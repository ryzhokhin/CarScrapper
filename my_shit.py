import csv
from seleniumwire import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

nameOfPreferencesFile = r'C:\Users\ilyanus\PycharmProjects\pythonProject\Preferences.csv'
nameof_titles = r'C:\Users\ilyanus\PycharmProjects\pythonProject1\titles_new.csv'


def dictatePreferences(nameOfPreferencesFile):
    print("Okay, here are the new preferences: ")

    with open(nameOfPreferencesFile) as f:
        csvReader = csv.reader(f, delimiter=',')
        for line in csvReader:
            print(line)

def preferencesReader(nameOfPreferencesFile):
    with open(nameOfPreferencesFile) as f:
        keyOrValue = 0
        keys = []
        values = []
        preferencesDictionary = {}

        csvReader = csv.reader(f, delimiter=',')

        for line in csvReader:
            for entry in line:
                if (keyOrValue == 0):
                    keys.append(entry)
                    keyOrValue = 1
                else:
                    values.append(entry)
                    keyOrValue = 0

        for key in keys:
            for value in values:
                preferencesDictionary[key] = value
                values.remove(value)
                break
    return (preferencesDictionary)

def mileageChange(nameOfPreferencesFile):

    preferencesDictionary = preferencesReader(nameOfPreferencesFile)
    print("the current minimum mileage value is: ", preferencesDictionary['Minimum Mileage'])
    print("and the current maximum mileage vlue is: ", preferencesDictionary['Maximum Mileage'])

    minMileage = input("Please enter a new minimum mileage: ")

    while (not (minMileage.isdigit())):
        minMileage = input(
            "I'm sorry, but " + minMileage + " is not a valid entry.  Please enter a positive integer value")

    maxMileage = input("Please enter a new maximum Mileage: ")

    while ((not (maxMileage.isdigit())) or (int(maxMileage) < int(minMileage))):
        maxMileage = input(
            "I'm sorry, but " + maxMileage + " is not a valid entry.  Please enter a positive integer value that is larger than the minimum mileage")

    preferencesDictionary['Minimum Mileage'] = minMileage
    preferencesDictionary['Maximum Mileage'] = maxMileage

    return (preferencesDictionary)

def lengthChange(nameOfPreferencesFile):
    preferencesDictionary = preferencesReader(nameOfPreferencesFile)

    print("the current length value is: ", preferencesDictionary['Scroll Down Length'])

    length = input("Please enter a new length: ")

    while (not (length.isdigit())):
        length = input("I'm sorry, but " + length + " is not a valid entry.  Please enter a positive integer value")

    preferencesDictionary['Scroll Down Length'] = length

    return (preferencesDictionary)

def priceChange(nameOfPreferencesFile):
    preferencesDictionary = preferencesReader(nameOfPreferencesFile)

    # csvWriter.writerow([key,preferencesDictionary[key]])

    print("the current minimum price value is: ", preferencesDictionary['Minimum Price'])
    print("and the current maximum price vlue is: ", preferencesDictionary['Maximum Price'])

    minPrice = input("Please enter a new minimum price: ")

    while (not (minPrice.isdigit())):
        minPrice = input("I'm sorry, but " + minPrice + " is not a valid entry.  Please enter a positive integer value")

    maxPrice = input("Please enter a new maximum price: ")

    while ((not (maxPrice.isdigit())) or (int(maxPrice) < int(minPrice))):
        maxPrice = input(
            "I'm sorry, but " + maxPrice + " is not a valid entry.  Please enter a positive integer value that is larger than the minimum price")

    preferencesDictionary['Minimum Price'] = minPrice
    preferencesDictionary['Maximum Price'] = maxPrice

    return (preferencesDictionary)

def yearChange(nameOfPreferencesFile):
    preferencesDictionary = preferencesReader(nameOfPreferencesFile)

    print("the current minimum year value is: ", preferencesDictionary['Minimum Year'])
    print("and the current maximum year vlue is: ", preferencesDictionary['Maximum Year'])

    minYear = input("Please enter a new minimum year: ")

    while (not (minYear.isdigit())):
        minYear = input("I'm sorry, but " + minYear + " is not a valid entry.  Please enter a positive integer value")

    maxYear = input("Please enter a new maximum year: ")

    while ((not (maxYear.isdigit())) or (int(maxYear) < int(minYear))):
        maxYear = input(
            "I'm sorry, but " + maxYear + " is not a valid entry.  Please enter a positive integer value that is larger than the minimum year")

    preferencesDictionary['Minimum Year'] = minYear
    preferencesDictionary['Maximum Year'] = maxYear

    return (preferencesDictionary)

def zipChange(nameOfPreferencesFile):
    preferencesDictionary = preferencesReader(nameOfPreferencesFile)

    print("the current length value is: ", preferencesDictionary['Zip Code'])

    zip_code = input("Please enter a new length: ")

    while (not (zip_code.isdigit())):
        zip_code = input("I'm sorry, but " + zip_code + " is not a valid entry.  Please enter a positive integer value")

    preferencesDictionary['Zip Code'] = zip_code

    return (preferencesDictionary)




def preferencesFileBackupWriter(nameOfPreferencesFile):
    with open(nameOfPreferencesFile, 'w') as f:
        csvWriter = csv.writer(f, delimiter=',')

        backupDictionary = {
            'Minimum Mileage': 0,
            'Maximum Mileage': 200000,
            'Minimum Price': 250,
            'Maximum Price': 55000,
            'Minimum Year': 1995,
            'Maximum Year': 2020,
            'Scroll Down Length': 150,
            'Zip Code': 11747
        }
        for key in backupDictionary:
            csvWriter.writerow([key, backupDictionary[key]])

def preferencesAskAndWrite(nameOfPreferencesFile="Preferences.csv",
                           haveWeRunThisFunctionAtLeastOneTime=False,
                           preferencesDictionary={}):
    try:
        with open(nameOfPreferencesFile) as f:
            csvReader = csv.reader(f, delimiter=',')  # preferences safety check
    except:
        preferencesFileBackupWriter(nameOfPreferencesFile)

    if (not haveWeRunThisFunctionAtLeastOneTime):
        changePreferencesBoolean = input(
            'Would you like to change your preferences before starting the pogram?  Enter Y for yes, N for no, \nV to view the current preferences, or ? for information on what the preferences are. I am not case sensititve: ')
        haveWeRunThisFunctionAtLeastOneTime = True
    else:
        changePreferencesBoolean = input(
            'Would you like to change any preferences before starting the pogram?  Enter Y for yes,  N for no, V to view the current preferences, or ? for information on what the preferences are.  I am not case sensititve: ')

    while ((not (changePreferencesBoolean.lower() == 'y')) and (not (changePreferencesBoolean.lower() == 'n')) and not (
            changePreferencesBoolean.lower() == 'v') and (not (changePreferencesBoolean.lower() == 'z')) and (not (changePreferencesBoolean == '?'))):
        changePreferencesBoolean = input(
            "I'm sorry, but " + changePreferencesBoolean + " is not a valid input.  Please enter Y for yes, or N for no: ")

    if (changePreferencesBoolean.lower() == 'y'):

        print('Please select from the following options of preferences to change:')
        whatPreferenceToChange = input(
            'for mileage type m, for price type p, for year type ye, l for "scroll down length," which\nis how many times it will scroll down in facebook to load in more vehicles, and to cancel type c: ')

        while ((not (whatPreferenceToChange.lower() == 'm')) and (not (whatPreferenceToChange.lower() == 'p')) and (
        not (whatPreferenceToChange.lower() == 'ye')) and (not (whatPreferenceToChange.lower() == 'z')) and (not (whatPreferenceToChange.lower() == 'c')) and (
               not (whatPreferenceToChange.lower() == 'l'))):
            whatPreferenceToChange = input(
                "I'm sorry, but " + whatPreferenceToChange + " is not a valid entry.  Please enter m for mileage, p for price, or ye for year: ")
        whatPreferenceToChange = whatPreferenceToChange.lower()
        if (whatPreferenceToChange == 'c'):
            print("Cancelling preference change, and searching for a great deal with previously saved preferences")
            return preferencesReader(nameOfPreferencesFile)
        elif (whatPreferenceToChange == 'm'):
            preferencesDictionary = mileageChange(nameOfPreferencesFile)

        elif (whatPreferenceToChange == 'p'):
            preferencesDictionary = priceChange(nameOfPreferencesFile)
        elif (whatPreferenceToChange == 'ye'):
            preferencesDictionary = yearChange(nameOfPreferencesFile)
        elif (whatPreferenceToChange == 'l'):
            preferencesDictionary = lengthChange(nameOfPreferencesFile)
        elif (whatPreferenceToChange == 'z'):
            preferencesDictionary = zipChange(nameOfPreferencesFile)
        else:
            print(
                "There has been a wierd as heck error, and if you were trying to change preferences I'm sorry but that just isn't going to happen anymore, buddy.")
            return preferencesReader(nameOfPreferencesFile)

        with open(nameOfPreferencesFile, 'w') as f:
            csvWriter = csv.writer(f, delimiter=',')

            for key in preferencesDictionary:
                csvWriter.writerow([key, preferencesDictionary[key]])  # test comment

        dictatePreferences(nameOfPreferencesFile)
        preferencesAskAndWrite(nameOfPreferencesFile, True, preferencesDictionary)

    elif (changePreferencesBoolean.lower() == 'v'):
        dictatePreferences(nameOfPreferencesFile)
        preferencesAskAndWrite(nameOfPreferencesFile, True, preferencesDictionary)
    elif (changePreferencesBoolean == '?'):
        print(
            "\nThe preferences that can be changed are as follows:\nMinimum and maximum mileage.  You can set a range of mileages that are acceptable for you, and the scraper will only search for cars within that mileage range.")
        print(
            "\nMinimum and maximum prices.  You can set a range of prices that are acceptable for you, and the scraper will only search for cars within that price range")
        print(
            "\nMinimum and maximum year.  You can set a range of years that are acceptable for you, and the scraper will only search for cars within that year range")
        print(
            "\nLength:  'length' is the number of times that the scraper will scroll to the bottom of the facebook website.  The more times it does this, the more\ncars will be searched, and the longer it will take the program to run.\n")
        preferencesAskAndWrite(nameOfPreferencesFile, True, preferencesDictionary)
    preferencesDictionary = preferencesReader(nameOfPreferencesFile)
    return preferencesDictionary


print (preferencesAskAndWrite(nameOfPreferencesFile))


# --------------------------------------------------------------------------------------------------


def linkGrabber(htmlSegment):
    splitSegment = htmlSegment.split('"')
    return ("https://www.facebook.com" + splitSegment[3])


def url_modifier():
    titles = {'make': 'Nissan', 'model': '180sx', 'year': '1997'}
    a_string = str(titles['model'])
    matches = [" ", "  "]

    if any([x in a_string for x in matches]):
        model_mod = str(titles['model']).split()
        facebookMarketUrl1 = 'https://www.facebook.com/marketplace/category/search?availability=out%20of%20stock'
        facebookMarketUrl2 = '&' + 'daysSinceListed=1' + '&'
        facebookMarketUrl3 = 'query=' + str(titles['make']) + '%20' + model_mod[0] + '%20' + model_mod[1] + '%20'\
                             + str(titles['year'])
        facebookMarketUrl4 = '&' + 'exact=' + 'false'
    else:
        # url = 'https://www.facebook.com/marketplace/category/search?availability=out%20of%20stock&query=tesla%20model%203&exact=false'
        facebookMarketUrl1 = 'https://www.facebook.com/marketplace/sanfrancisco/search?availability=out%20of%20stock'
        facebookMarketUrl2 = '&'
        facebookMarketUrl3 = 'query=' + str(titles['make']) + '%20' + str(titles['model']) + '%20' + str(titles['year'])
        facebookMarketUrl4 = '&' + 'exact=' + 'false'

    fb_url = facebookMarketUrl1 + facebookMarketUrl2 + facebookMarketUrl3 + facebookMarketUrl4

    return fb_url


def facebookScraper(fb_url,scrollDownLength=25):
    if __name__ == '__main__':
        candidates = []
        containerSplit = []
        tempLinkHolder = []
        package = []

        PATH = 'C:\\Users\\ilyanus\\.wdm\\drivers\\chromedriver\\win32\\114.0.5735.90\\chromedriver.exe'

        options = webdriver.ChromeOptions()
        # options.add_argument('--proxy-server=185.130.105.109:10013')

        driver = uc.Chrome(
            options=options,
        )

        driver.get(url_modifier())
        # url = "https://2ip.ru"
        # driver.get(url)

        time.sleep(15)

        email = 'molokic228@hotmail.com'
        password = 'Facebook_huy228'

        pref_dict = preferencesReader(nameOfPreferencesFile)

        zipcode = pref_dict['Zip Code']
        pricemin = pref_dict['Minimum Price']
        pricemax = pref_dict['Maximum Price']

        if EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'submit')]")) == True:
            driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Email')]").send_keys(email)
            driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Password')]").send_keys(password)
            time.sleep(5)
            driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
            time.sleep(10)
            driver.get(url_modifier())
        else:
            pass

        # if EC.visibility_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Enter ZIP Code')]")):
        #     driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Enter ZIP Code')]").send_keys(zipcode)
        #     WebDriverWait(driver, 20).until(
        #         EC.visibility_of_element_located((By.XPATH, "//ul[contains(@aria-label, '1 suggested search')]")))
        #     driver.find_element(By.XPATH, "//ul[contains(@aria-label, '1 suggested search')]").click()
        #
        #     time.sleep(2)
        #     driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Shop local')]").click()
        # else:
        #     pass



        time.sleep(13)

        driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Minimum Range')]").send_keys(pricemin)
        driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Maximum Range')]").send_keys(pricemax)

        time.sleep(10)


        for i in range(int(scrollDownLength)):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)

        containers = driver.find_elements(By.CLASS_NAME, "x3ct3a4")

        for container in containers:
                tempLinkHolder.append(linkGrabber(container.get_attribute("innerHTML")))

        for container in containers:
                # print(container.text)
                candidates.append(container.text)

        i = 0

        def gettingTheFinalTypeDataFrame(data_subset):
            def transform_entry(entry):
                # Split by newline
                split_entry = entry.split('\n')

                # Check for second price value and remove if found
                if "$" in split_entry[2] and "$" in split_entry[3]:
                    split_entry.pop(3)

                # Extract year from fourth column
                year = split_entry[3][:4]
                split_entry.insert(3, year)

                return split_entry

            # Apply transformation to the data
            transformed_data = [transform_entry(item) for item in data_subset]

            def further_transform_entry(entry):
                # Removing the first four digits (year) from the 5th column
                entry[4] = entry[4][5:]
                return entry

            # Apply further transformation to the transformed data
            final_transformed_data = [further_transform_entry(item) for item in transformed_data]

            def final_transform_entry(entry):
                # Removing 'miles' and 'K' from the last column
                mileage = entry[-1].replace('miles', '').replace('K', '').replace('M', '').strip()
                # Convert mileage to integer after multiplying by 1000 if 'K' was present
                if 'K' in entry[-1]:
                    entry[-1] = int(float(mileage) * 1000)
                elif 'M' in entry[-1]:
                    entry[-1] = int(float(mileage) * 1000000)
                else:
                    entry[-1] = int(float(mileage))
                entry[2] = int(entry[2].replace('$', '').replace(',', ''))

                return entry

            # Apply final transformation to the data
            final_data = []
            for item in final_transformed_data:
                if len(item) == 6:
                    print(item)
                else:
                    final_data.append(final_transform_entry(item))

            final_data_with_category = []
            for subdata in final_data:
                if int(subdata[2]) <= 5000:
                    subdata.append('A')
                elif int(subdata[2]) <= 10000:
                    subdata.append('B')
                elif int(subdata[2]) <= 15000:
                    subdata.append('C')
                elif int(subdata[2]) <= 20000:
                    subdata.append('D')
                elif int(subdata[2]) <= 25000:
                    subdata.append('E')
                else:
                    subdata.append('F')
                final_data_with_category.append(subdata)

            def generateFinalTable(data):
                df = pd.DataFrame(data)
                df = df.drop(columns=1)
                column_names = {
                    0: 'Contract',
                    2: 'Price',
                    3: 'Year',
                    4: 'Make&Model',
                    5: 'Location',
                    6: 'Miles',
                    7: 'Category'
                }

                df.rename(columns=column_names, inplace=True)

                # Convert 'Year' and 'Miles' columns to integer
                df['Year'] = df['Year'].astype(int)
                df['Miles'] = df['Miles'].astype(int)
                return df

            return generateFinalTable(final_data_with_category)

        split_data = gettingTheFinalTypeDataFrame(candidates)
        driver.close()
        return split_data

        time.sleep(60)


        i = 0
# нет ты пидор

data_package = facebookScraper(url_modifier(),scrollDownLength=4 )

data_package.to_csv('out14888.csv', index=False)