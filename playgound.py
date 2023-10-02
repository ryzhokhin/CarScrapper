# import pandas as pd
#
# dataTest = [
#     'Sold\n  ·\n$11,000\n1995 Nissan 240sx\nAlameda, CA',
#     'Sold\n  ·\n$3,000\n$3,500\n1997 Nissan 240sx\nAntioch, CA\n1.2M miles',
#     'Pending\n  ·\n$20,000\n$25,000\n1997 Nissan 240sx\nRoseville, CA\n110K miles',
#     'Sold\n  ·\n$5,500\n1995 Nissan 240sx\nCarpinteria, CA\n117K miles',
#     'Sold\n  ·\n$12,345\n1990 Nissan 240sx\nRoseville, CA\n12K miles',
#     'Sold\n  ·\n$8,000\n1996 Nissan 240sx\nReno, NV\n163K miles',
#     'Sold\n  ·\n$26,999\n1997 Nissan 240sx\nLos Angeles, CA\n144K miles',
#     'Sold\n  ·\n$4,500\n1987 Nissan 300zx\nMonterey, CA\n103K miles',
#     'Sold\n  ·\n$10,000\n1999 Mitsubishi eclipse\nFresno, CA\n120K miles',
#     'Sold\n  ·\n$26,500\n1997 Mazda rx-7\nRancho Cucamonga, CA\n82K miles'
# ]
#
#
# # Splitting data by newline character
# # split_data = [item.split('\n') for item in data]
# # print(split_data)
#
#
# def gettingTheFinalTypeDataFrame(data_subset):
#     def transform_entry(entry):
#         # Split by newline
#         split_entry = entry.split('\n')
#
#         # Check for second price value and remove if found
#         if "$" in split_entry[2] and "$" in split_entry[3]:
#             split_entry.pop(3)
#
#         # Extract year from fourth column
#         year = split_entry[3][:4]
#         split_entry.insert(3, year)
#
#         return split_entry
#
#     # Apply transformation to the data
#     transformed_data = [transform_entry(item) for item in data_subset]
#
#     def further_transform_entry(entry):
#         # Removing the first four digits (year) from the 5th column
#         entry[4] = entry[4][5:]
#         return entry
#
#     # Apply further transformation to the transformed data
#     final_transformed_data = [further_transform_entry(item) for item in transformed_data]
#     print(final_transformed_data)
#     def final_transform_entry(entry):
#         # Removing 'miles' and 'K' from the last column
#         mileage = entry[-1].replace('miles', '').replace('K', '').replace('M', '').strip()
#         # Convert mileage to integer after multiplying by 1000 if 'K' was present
#         if 'K' in entry[-1]:
#             entry[-1] = int(float(mileage) * 1000)
#         elif 'M' in entry[-1]:
#             entry[-1] = int(float(mileage) * 1000000)
#         else:
#             entry[-1] = int(float(mileage))
#         entry[2] = int(entry[2].replace('$', '').replace(',', ''))
#         return entry
#
#     # Apply final transformation to the data
#     final_data = []
#     for item in final_transformed_data:
#         if len(item) == 6:
#             print(item)
#         else:
#             final_data.append(final_transform_entry(item))
#     # final_data = [final_transform_entry(item) for item in final_transformed_data]
#
#
#     final_data_with_category = []
#     for subdata in final_data:
#         if int(subdata[2]) <= 5000:
#             subdata.append('A')
#         elif int(subdata[2]) <= 10000:
#             subdata.append('B')
#         elif int(subdata[2]) <= 15000:
#             subdata.append('C')
#         elif int(subdata[2]) <= 20000:
#             subdata.append('D')
#         elif int(subdata[2]) <= 25000:
#             subdata.append('E')
#         else:
#             subdata.append('F')
#         final_data_with_category.append(subdata)
#
#     def generateFinalTable(data):
#         df = pd.DataFrame(data)
#         df = df.drop(columns=1)
#         column_names = {
#             0: 'Contract',
#             2: 'Price',
#             3: 'Year',
#             4: 'Make&Model',
#             5: 'Location',
#             6: 'Miles',
#             7: 'Category'
#         }
#
#         df.rename(columns=column_names, inplace=True)
#
#         # df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(int)
#
#         # Convert 'Year' and 'Miles' columns to integer
#         df['Year'] = df['Year'].astype(int)
#         df['Miles'] = df['Miles'].astype(int)
#         return df
#
#     return generateFinalTable(final_data_with_category)
#
#
# def findEV(ModelMake):
#     df = gettingTheFinalTypeDataFrame(dataTest)
#     dfMake = df[(df['Make&Model'] == ModelMake)]
#     everagePrice = dfMake['Price'].mean()
#     return everagePrice
#
#
# def test(data_subset):
#     def transform_entry(entry):
#         # Split by newline
#         split_entry = entry.split('\n')
#
#         # Check for second price value and remove if found
#         if "$" in split_entry[2] and "$" in split_entry[3]:
#             split_entry.pop(3)
#
#         # Extract year from fourth column
#         year = split_entry[3][:4]
#         split_entry.insert(3, year)
#
#         return split_entry
#
#     # Apply transformation to the data
#     transformed_data = [transform_entry(item) for item in data_subset]
#
#     def further_transform_entry(entry):
#         # Removing the first four digits (year) from the 5th column
#         entry[4] = entry[4][5:]
#         return entry
#
#     # Apply further transformation to the transformed data
#     final_transformed_data = [further_transform_entry(item) for item in transformed_data]
#     for item in final_transformed_data:
#         print(len(item))
#     print(final_transformed_data)
#
# # mean = findEverage('Nissan 240sx')
# # print(df[df['Price'] < mean])
# # dfMake['Price'].plot(kind='hist')
# # print(findEV('Nissan 240sx'))
# print(gettingTheFinalTypeDataFrame(dataTest))
# # test(dataTest)

import pandas as pd

dataTest = [
    'Sold\n  ·\n$11,000\n1995 Nissan 240sx\nAlameda, CA',
    'Sold\n  ·\n$3,000\n$3,500\n1997 Nissan 240sx\nAntioch, CA\n1.2M miles',
    'Pending\n  ·\n$20,000\n$25,000\n1997 Nissan 240sx\nRoseville, CA\n110K miles',
    'Sold\n  ·\n$5,500\n1995 Nissan 240sx\nCarpinteria, CA\n117K miles',
    'Sold\n  ·\n$12,345\n1990 Nissan 240sx\nRoseville, CA\n12K miles',
    'Sold\n  ·\n$8,000\n1996 Nissan 240sx\nReno, NV\n163K miles',
    'Sold\n  ·\n$26,999\n1997 Nissan 240sx\nLos Angeles, CA\n144K miles',
    'Sold\n  ·\n$4,500\n1987 Nissan 300zx\nMonterey, CA\n103K miles',
    'Sold\n  ·\n$10,000\n1999 Mitsubishi eclipse\nFresno, CA\n120K miles',
    'Sold\n  ·\n$26,500\n1997 Mazda rx-7\nRancho Cucamonga, CA\n82K miles'
]


# Splitting data by newline character
# split_data = [item.split('\n') for item in data]
# print(split_data)


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
    print(final_transformed_data)
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
    # final_data = [final_transform_entry(item) for item in final_transformed_data]


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

        # df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(int)

        # Convert 'Year' and 'Miles' columns to integer
        df['Year'] = df['Year'].astype(int)
        df['Miles'] = df['Miles'].astype(int)
        return df

    return generateFinalTable(final_data_with_category)


def findEV(ModelMake):
    df = gettingTheFinalTypeDataFrame(dataTest)
    dfMake = df[(df['Make&Model'] == ModelMake)]
    everagePrice = dfMake['Price'].mean()
    return everagePrice

titles = {'make&model': 'Nissan240sx', 'year': '1997'}


def soldCounter(data, make_model, year):
    df = gettingTheFinalTypeDataFrame(data)
    dfCounter = df[(df['Make&Model'] == make_model)]
    dfCounter = dfCounter[(dfCounter['Year'] == year)]
    print(dfCounter)
    counter = dfCounter.count()[0]
    # for item in df:
    #     if titles['make&model'] == df['Make&Model']:
    #         counter += 1
    #     else:
    #         pass
    return counter

# mean = findEverage('Nissan 240sx')
# print(df[df['Price'] < mean])
# dfMake['Price'].plot(kind='hist')
# print(findEV('Nissan 240sx'))


print(soldCounter(dataTest, 'Nissan 240sx', 1997))
# print(gettingTheFinalTypeDataFrame(dataTest))
# test(dataTest)
