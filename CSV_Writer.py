import csv
import pandas as pd


def find_by(queryText, token, type):
    df = pd.read_csv('MOCK_DATA.csv')
    dfByMake = df[(df[f'{type}'] == queryText)]
    dfByMake.to_csv(f"FilterBy{type}Tests/{queryText}-{token}.csv", index=False)
    # with open(f"FilterByMakeTests/{make}-{token}.csv", "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerows(dfByMake)


def findEverage(make):
    df = pd.read_csv('MOCK_DATA.csv')
    dfMake = df[(df['Make'] == make)]
    mean = dfMake['Price'].mean()
    return mean
    # print(dfMake[dfMake['Price'] < mean])
    # dfMake['Price'].plot(kind='hist')



findEverage('Lexus')
# print(find_by_make("Mazda"))
# make_Toyota = df[(df['make'] == "Toyota")]


# print(make_Toyota.head())
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         # [make, model]
#         ("make", "model", "year", "price", "milage",)
#     )
#
# car_data = [
#     ["Toyota", "Highlander", 2021, 45000, 32000],
#     ["Audi", "a6", 2017, 28000, 32999],
#     ["BMW", "m5", 2019, 25000, 34000],
#     ["VW", "passat", 2020, 18000, 49000]
# ]
#
# with open("data.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerows(
#         car_data
#     )
