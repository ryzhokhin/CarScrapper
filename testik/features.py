import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')  # or can use 'TkAgg', whatever you have/prefer
# from tester import carsJson
carsJson = {"Acura": ["Cl"], "Alfa_Romeo": ["Stelvio", "Sportwagon", "159", "Giulietta", "Mito", "Brera", "155", "Spider", "156", "147", "Gt"], "Audi": ["Tt", "Rs3", "S8", "Rs", "Ttcoupe", "A4", "A1", "A5", "A6", "S1", "S4", "80", "S6", "A3", "Q2", "A8", "Q7", "Rs5", "Q5", "Sq5", "Tts", "A7", "Q3", "Sq2", "S5", "S3"], "BMW": ["3", "M6", "7", "5", "X5", "8", "M4", "X4", "X1", "2", "1", "4", "6", "I3", "X2", "M3", "Z4", "X3", "X6", "Mini", "Z3", "X7"], "Bentley": ["BENTLEY", "-", "Continental", "Navy"], "Bmw_Alpina": ["Xd3"], "Cadillac": ["Xt4", "Sts", "Eldorado", "Cade", "Srx", "Concourse"], "Chevrolet": ["Sonic", "Astro", "Blazer", "Camaro", "Cvl"], "Chrysler": ["Ypsilon", "Pt", "Durango", "300c", "Voyager", "300", "Grand", "Ram"], "Citroen": ["Ds4", "Berlingo", "C5", "Grand", "Ds3", "Saxo", "C6", "C4", "C3", "Ds7"], "Dodge": ["Nitro", "Magnum", "Te."], "Daihatsu": ["Wake", "Hijet", "Be", "Storia", "Atrai", "Delta", "Sonica", "Naked", "Max", "Gran", "Coo", "Copen", "Mira", "Opti", "Terios", "Esse", "Midget", "Move", "Boon", "Tanto", "Cast", "Rocky", "Thor", "Taft"], "Ferrari": ["Roma", "F430"], "Fiat": ["500", "New", "Panda", "500x", "Abarth"], "Ford": ["Ecosport", "Focus", "Festiva", "FORD", "Expedition", "Escape", "Fiesta", "Explorer", "Fo", "Mustang", "Lincoln", "Kuga"], "Gmc": ["GMC", "Express", "Chevrolet", "Cadillac", "Yukon"], "Hino": ["Profia", "HINO", "Dutro", "Dutoro", "Ranger", "Blue", "Liesse"], "Hummer": ["H3"], "Infiniti": ["G37", "In", "Fx35"], "Jaguar": ["X", "E-pace", "F-pace", "Xf", "Xk", "F-type", "Xe", "Xj6"], "Jeep": ["Renegade", "Commander", "Compass", "Cherokee", "Wrangler", "Patriot", "Grand"], "Komatsu": ["KOMATSU"], "Lamborghini": ["Murcielago", "Gayarusp4w"], "Lancia": ["Dedra"], "Land_Rover": ["Range", "Defender", "Freelander", "Lr", "Discovery"], "Lexus": ["LX", "CT", "LC", "RC", "HS", "UX", "ES", "NX", "SC", "RX", "GS", "IS", "LS"], "Lincoln": ["Navigation"], "Mazda": ["Cx-5", "Efini", "Bongo", "Verisa", "Cx-8", "Cx-60", "Rx-8", "Mazda2", "Mazda6", "Az", "Flair", "Spiano", "Demio", "Rx-7", "Scrum", "Cx-30", "Premacy", "Mx-30", "Eunos", "Mpv", "Carol", "Proceed", "Speed", "Mazda3", "Porter", "Cx-3", "Atenza", "Titan", "Roadster", "Capella", "Cx-7", "Familia", "Biante", "Axela"], "Mitsubishi": ["Delica", "Fto", "Galant", "Combine", "Toppo", "Jeep", "Airtrek", "Wheel", "Mirage", "Ek", "Town", "Grandis", "Triton", "I", "Legnum", "Chariot", "Bulldozer", "Diamante", "I-miev", "G", "Canter", "Outlander", "Proudia", "Lancer", "Rvr", "Fuso", "Minica", "Pajero", "Dion", "Eclipse", "Colt", "Gto", "Minicab"], "Maserati": ["Levante", "Ghibli", "Quattroporte", "Gran"], "Mercedes-Benz": ["Eqc", "Slc", "E", "Eqb", "Benz", "Gle", "Mb", "C", "Slk", "R", "Sl", "Glb", "Cla", "Cls", "G", "Cl", "Clk", "V", "Glk", "M", "S", "Amg", "Viano", "A", "Gla", "B", "Glc", "Gls", "E-class"], "Mg": ["Rv8"], "Mini": ["Yuatsu", "Mini"], "Mitsuoka": ["Galue", "Viewt", "Ryoga"], "Nissan_Diesel_%28ud%29": ["Condor"], "Peugeot": ["3008", "308", "406", "5008", "Rifter", "208", "Rcz", "207", "407", "508", "2008", "307", "1007", "E-208"], "Porsche": ["Macan", "718", "Cayenne", "Boxster", "911", "PORSCHE", "944", "Panamera"], "Renault": ["Megane", "Captur", "Kangoo", "Twingo", "Lutecia"], "Rolls Royce": ["Phantom", "Rolls"], "Nissan": ["Nv100", "Dayz", "X-trail", "Caravan", "Condor", "E-nv200", "Juke", "Laurel", "Sylphy", "Wingroad", "Pulsar", "Infiniti", "Teana", "Fuga", "Figaro", "Gloria", "Homy", "Note", "Nt450", "Rasheen", "Presage", "Atlas", "Stagea", "Cima", "Liberty", "Bluebird", "Micra", "Skyline", "Vanette", "Leopard", "Avenir", "Pino", "Sunny", "Bassara", "Be-1", "Cube", "Gt-r", "Sakura", "Kicks", "Lafesta", "Primera", "Roox", "180sx", "Nv350", "Latio", "Kix", "Elgrand", "Expert", "K", "Tino", "Cefiro", "Datsun", "Safari", "March", "Ud", "Clipper", "President", "Serena", "Fairlady", "Leaf", "Silvia", "Nv150", "Aura", "Terrano", "Moco", "Otti", "Nv200", "Civilian", "S-cargo", "Dualis", "Nt100", "Murano", "Ad", "Tiida", "Cedric"], "Rover": ["Mini"], "Saab": ["9-5x"], "Smart": ["Fortwo", "Fourfour", "Coupe", "K", "Roadster"], "VW": ["European", "T-cross", "Sirocco", "Bus", "New", "Polo", "Beetle", "Golf", "Vanagon", "Type", "Up", "Touareg", "The", "Tiguan", "Arteon", "Lupo", "Up!", "Jetta", "T-roc", "Sharan", "Passat"], "Volvo": ["S60", "V90", "Xc60", "240", "Xc90", "V60", "S40", "960", "S90", "Xc70", "850", "Xc40", "V50", "V70", "V40", "C70"], "Honda": ["Freed", "Acty", "N-wgn", "Cr-v", "Airwave", "Freed+", "Inspire", "Fit", "S660", "Live", "N", "E", "Accord", "Z", "Capa", "Hr-v", "Avancier", "Jade", "Zr-v", "Stream", "Zest", "Today", "Edix", "Thats", "Element", "Vezel", "N-van", "Prelude", "Crossroad", "Shuttle", "Civic", "Legend", "Electrical", "Grace", "Cr-z", "Odyssey", "Elysion", "Lagreat", "Mobilio", "Stepwgn", "Integra", "Saber", "Vamos", "Gyro", "N-one", "Street", "N-box", "Insight", "Torneo", "Life", "Domani", "Nsx", "Beat", "Logo", "S2000"], "Isuzu": ["Coaster", "Bighorn", "ISUZU", "Gemini", "Bus", "Elf", "Forward", "Giga", "Como", "Fargo", "Journey", "Wizard"], "Subaru": ["R2", "Lucra", "Outback", "Trezia", "Wrx", "Stella", "Forester", "Alcyone", "Pleo", "Sambar", "Exiga", "Levorg", "Dias", "Impreza", "Xv", "Dex", "Brz", "Leone", "R1", "Chiffon", "Vivio", "Legacy"], "Suzuki": ["Splash", "Every", "Twin", "Cervo", "Super", "Baleno", "Cruze", "Landy", "Palette", "Mr", "Carry", "Mrwagon", "Jimny", "Aerio", "Ignis", "Solio", "Kei", "Mw", "Cappuccino", "Spacia", "Swift", "Lapin", "Sx4", "Alto", "Wagon", "Hustler", "Xbee", "Escudo"], "Toyota": ["Starlet", "Prius", "Gr", "Fj", "Granace", "Premio", "Avensis", "Wish", "Allex", "Brevis", "Townace", "Corona", "Markx", "Vellfire", "Bb", "Succeed", "Celica", "Celsior", "Kluger", "S", "Sprinter", "Grand", "Isis", "Rush", "Vitz", "Porte", "Ractis", "Toyoace", "Alphard", "Gaya", "Camroad", "Platz", "Yaris", "Town", "Caldina", "Sequoia", "Copen", "Roomy", "Lite", "Special", "Soarer", "Raize", "Ipsum", "Mirai", "Aristo", "Hilux", "TOYOTA", "Noah", "Tank", "Battery", "Raum", "Voxy", "Esquire", "Estima", "Granvia", "Corolla", "Century", "Sai", "Forklift", "Mr-s", "Pixis", "Probox", "Cresta", "Sparky", "Mr2", "Quick", "Shovel", "Fun", "Verossa", "Cami", "Rav4", "Opa", "Chaser", "Sienta", "Cynos", "Crown", "Blade", "Ist", "Aqua", "Tundra", "Supra", "Belta", "86", "Progres", "Hiace", "Allion", "Will", "Li-chi", "Dyna", "Windom", "Carina", "Coaster", "Spade", "Mark", "Vanguard", "Tercel", "Regius", "Passo", "Auris", "Land", "Altezza", "Iq", "Camry", "Vista", "Harrier", "C-hr", "Coms", "Tacoma"]}
carsJson4test = {"Acura": ["Cl"], "Alfa_Romeo": ["Stelvio", "Sportwagon", "159", "Giulietta", "Mito", "Brera", "155", "Spider", "156", "147", "Gt"], "Audi": ["Tt", "Rs3", "S8", "Rs", "Ttcoupe", "A4", "A1", "A5", "A6", "S1", "S4", "80", "S6", "A3", "Q2", "A8", "Q7", "Rs5", "Q5", "Sq5", "Tts", "A7", "Q3", "Sq2", "S5", "S3"], "BMW": ["3", "M6", "7", "5", "X5", "8", "M4", "X4", "X1", "2", "1", "4", "6", "I3", "X2", "M3", "Z4", "X3", "X6", "Mini", "Z3", "X7"], "Bentley": ["BENTLEY", "-", "Continental", "Navy"], "Bmw_Alpina": ["Xd3"], "Cadillac": ["Xt4", "Sts", "Eldorado", "Cade", "Srx", "Concourse"], "Chevrolet": ["Sonic", "Astro", "Blazer", "Camaro", "Cvl"], "Chrysler": ["Ypsilon", "Pt", "Durango", "300c", "Voyager", "300", "Grand", "Ram"], "Citroen": ["Ds4", "Berlingo", "C5", "Grand", "Ds3", "Saxo", "C6", "C4", "C3", "Ds7"], "Dodge": ["Nitro", "Magnum", "Te."], "Daihatsu": ["Wake", "Hijet", "Be", "Storia", "Atrai", "Delta", "Sonica", "Naked", "Max", "Gran", "Coo", "Copen", "Mira", "Opti", "Terios", "Esse", "Midget", "Move", "Boon", "Tanto", "Cast", "Rocky", "Thor", "Taft"], "Ferrari": ["Roma", "F430"], "Fiat": ["500", "New", "Panda", "500x", "Abarth"], "Ford": ["Ecosport", "Focus", "Festiva", "FORD", "Expedition", "Escape", "Fiesta", "Explorer", "Fo", "Mustang", "Lincoln", "Kuga"], "Gmc": ["GMC", "Express", "Chevrolet", "Cadillac", "Yukon"], "Hino": ["Profia", "HINO", "Dutro", "Dutoro", "Ranger", "Blue", "Liesse"], "Hummer": ["H3"], "Infiniti": ["G37", "In", "Fx35"], "Jaguar": ["X", "E-pace", "F-pace", "Xf", "Xk", "F-type", "Xe", "Xj6"], "Jeep": ["Renegade", "Commander", "Compass", "Cherokee", "Wrangler", "Patriot", "Grand"], "Komatsu": ["KOMATSU"], "Lamborghini": ["Murcielago", "Gayarusp4w"], "Lancia": ["Dedra"], "Land_Rover": ["Range", "Defender", "Freelander", "Lr", "Discovery"], "Lexus": ["LX", "CT", "LC", "RC", "HS", "UX", "ES", "NX", "SC", "RX", "GS", "IS", "LS"], "Lincoln": ["Navigation"], "Mazda": ["Cx-5", "Efini", "Bongo", "Verisa", "Cx-8", "Cx-60", "Rx-8", "Mazda2", "Mazda6", "Az", "Flair", "Spiano", "Demio", "Rx-7", "Scrum", "Cx-30", "Premacy", "Mx-30", "Eunos", "Mpv", "Carol", "Proceed", "Speed", "Mazda3", "Porter", "Cx-3", "Atenza", "Titan", "Roadster", "Capella", "Cx-7", "Familia", "Biante", "Axela"], "Mitsubishi": ["Delica", "Fto", "Galant", "Combine", "Toppo", "Jeep", "Airtrek", "Wheel", "Mirage", "Ek", "Town", "Grandis", "Triton", "I", "Legnum", "Chariot", "Bulldozer", "Diamante", "I-miev", "G", "Canter", "Outlander", "Proudia", "Lancer", "Rvr", "Fuso", "Minica", "Pajero", "Dion", "Eclipse", "Colt", "Gto", "Minicab"], "Maserati": ["Levante", "Ghibli", "Quattroporte", "Gran"], "Mercedes-Benz": ["Eqc", "Slc", "E", "Eqb", "Benz", "Gle", "Mb", "C", "Slk", "R", "Sl", "Glb", "Cla", "Cls", "G", "Cl", "Clk", "V", "Glk", "M", "S", "Amg", "Viano", "A", "Gla", "B", "Glc", "Gls", "E-class"], "Mg": ["Rv8"], "Mini": ["Yuatsu", "Mini"], "Mitsuoka": ["Galue", "Viewt", "Ryoga"], "Nissan_Diesel_%28ud%29": ["Condor"], "Peugeot": ["3008", "308", "406", "5008", "Rifter", "208", "Rcz", "207", "407", "508", "2008", "307", "1007", "E-208"], "Porsche": ["Macan", "718", "Cayenne", "Boxster", "911", "PORSCHE", "944", "Panamera"], "Renault": ["Megane", "Captur", "Kangoo", "Twingo", "Lutecia"], "Rolls Royce": ["Phantom", "Rolls"], "Nissan": ["Nv100", "Dayz", "X-trail", "Caravan", "Condor", "E-nv200", "Juke", "Laurel", "Sylphy", "Wingroad", "Pulsar", "Infiniti", "Teana", "Fuga", "Figaro", "Gloria", "Homy", "Note", "Nt450", "Rasheen", "Presage", "Atlas", "Stagea", "Cima", "Liberty", "Bluebird", "Micra", "Skyline", "Vanette", "Leopard", "Avenir", "Pino", "Sunny", "Bassara", "Be-1", "Cube", "Gt-r", "Sakura", "Kicks", "Lafesta", "Primera", "Roox", "180sx", "Nv350", "Latio", "Kix", "Elgrand", "Expert", "K", "Tino", "Cefiro", "Datsun", "Safari", "March", "Ud", "Clipper", "President", "Serena", "Fairlady", "Leaf", "Silvia", "Nv150", "Aura", "Terrano", "Moco", "Otti", "Nv200", "Civilian", "S-cargo", "Dualis", "Nt100", "Murano", "Ad", "Tiida", "Cedric"], "Rover": ["Mini"], "Saab": ["9-5x"], "Smart": ["Fortwo", "Fourfour", "Coupe", "K", "Roadster"], "VW": ["European", "T-cross", "Sirocco", "Bus", "New", "Polo", "Beetle", "Golf", "Vanagon", "Type", "Up", "Touareg", "The", "Tiguan", "Arteon", "Lupo", "Up!", "Jetta", "T-roc", "Sharan", "Passat"], "Volvo": ["S60", "V90", "Xc60", "240", "Xc90", "V60", "S40", "960", "S90", "Xc70", "850", "Xc40", "V50", "V70", "V40", "C70"], "Honda": ["Freed", "Acty", "N-wgn", "Cr-v", "Airwave", "Freed+", "Inspire", "Fit", "S660", "Live", "N", "E", "Accord", "Z", "Capa", "Hr-v", "Avancier", "Jade", "Zr-v", "Stream", "Zest", "Today", "Edix", "Thats", "Element", "Vezel", "N-van", "Prelude", "Crossroad", "Shuttle", "Civic", "Legend", "Electrical", "Grace", "Cr-z", "Odyssey", "Elysion", "Lagreat", "Mobilio", "Stepwgn", "Integra", "Saber", "Vamos", "Gyro", "N-one", "Street", "N-box", "Insight", "Torneo", "Life", "Domani", "Nsx", "Beat", "Logo", "S2000"], "Isuzu": ["Coaster", "Bighorn", "ISUZU", "Gemini", "Bus", "Elf", "Forward", "Giga", "Como", "Fargo", "Journey", "Wizard"], "Subaru": ["R2", "Lucra", "Outback", "Trezia", "Wrx", "Stella", "Forester", "Alcyone", "Pleo", "Sambar", "Exiga", "Levorg", "Dias", "Impreza", "Xv", "Dex", "Brz", "Leone", "R1", "Chiffon", "Vivio", "Legacy"], "Suzuki": ["Splash", "Every", "Twin", "Cervo", "Super", "Baleno", "Cruze", "Landy", "Palette", "Mr", "Carry", "Mrwagon", "Jimny", "Aerio", "Ignis", "Solio", "Kei", "Mw", "Cappuccino", "Spacia", "Swift", "Lapin", "Sx4", "Alto", "Wagon", "Hustler", "Xbee", "Escudo"], "Toyota": ["Starlet", "Prius", "Gr", "Fj", "Granace", "Premio", "Avensis", "Wish", "Allex", "Brevis", "Townace", "Corona", "Markx", "Vellfire", "Bb", "Succeed", "Celica", "Celsior", "Kluger", "S", "Sprinter", "Grand", "Isis", "Rush", "Vitz", "Porte", "Ractis", "Toyoace", "Alphard", "Gaya", "Camroad", "Platz", "Yaris", "Town", "Caldina", "Sequoia", "Copen", "Roomy", "Lite", "Special", "Soarer", "Raize", "Ipsum", "Mirai", "Aristo", "Hilux", "TOYOTA", "Noah", "Tank", "Battery", "Raum", "Voxy", "Esquire", "Estima", "Granvia", "Corolla", "Century", "Sai", "Forklift", "Mr-s", "Pixis", "Probox", "Cresta", "Sparky", "Mr2", "Quick", "Shovel", "Fun", "Verossa", "Cami", "Rav4", "Opa", "Chaser", "Sienta", "Cynos", "Crown", "Blade", "Ist", "Aqua", "Tundra", "Supra", "Belta", "86", "Progres", "Hiace", "Allion", "Will", "Li-chi", "Dyna", "Windom", "Carina", "Coaster", "Spade", "Mark", "Vanguard", "Tercel", "Regius", "Passo", "Auris", "Land", "Altezza", "Iq", "Camry", "Vista", "Harrier", "C-hr", "Coms", "Tacoma"]}

# collects only models below 1999 year made
def final_filter(make, model):
    f = open('Testicle/attempts.txt', 'r')
    # atmptNum = int(f.readline()) - 1
    atmptNum = int(f.readline()) - 1
    f.close()
    df = pd.read_csv(f'Testicle/out_{make}_{model}_{atmptNum}.csv')
    df = df[df['Year'] <= 1999]
    # print(df)
    return getDeepSell(df)


# Metric that counts depth sales based on model and make provided by user, for the latest scrap
def getDeepSell(df):
    return df.count()[0]





def getting_graph_for_makes(x, models_y):
    output_y = []
    curr = 0
    for i in x:
        currModelCounter = 0
        for j in models_y[curr]:
            try:
                currModelCounter += final_filter(i,j)
            except:
                pass
        output_y.append(currModelCounter)
        curr += 1
    return x, output_y


def getNumOfSalesForAllMakes(data): #Считает продажи по автомобилям котрые мы передаем в Json структуре
    maker_count = []
    for i in data:
        df_counter = 0
        for j in data[i]:
            try:
                df_counter += final_filter(i, j)
            except:
                pass
        maker_count.append(df_counter)
    return maker_count


def get_models_for_make(x_tmp): #вставляешь массив марок возвращает модели
    models = []
    for i in x_tmp:
        models.append(carsJson[i])
    return models

x_all_models_for_use = ['BMW','Toyota', 'Honda', 'Jeep']
# x,y = getting_graph_for_makes(x_all_models_for_use, get_models_for_make(x_all_models_for_use))

# print(graphing_makes(carsJson4test))
#
def delete_makes_with_zero(data, makeCount): #возвращает чистый джейсон в котором хранятся только  те марки и модели прождажи которых больше нуля
    outputData = {'ZeroItem':0, 'ZeroItemTwo':0, }
    counter = 0
    for i in data:
        if makeCount[counter] != 0:
            outputData[i] = data[i]
        counter += 1
    outputData.pop('ZeroItem')
    outputData.pop('ZeroItemTwo')

    return outputData

# print(delete_makes_with_zero(carsJson4test,graphing_makes(carsJson4test) ))

print(getNumOfSalesForAllMakes(carsJson4test))
newCarsJson = delete_makes_with_zero(carsJson4test,getNumOfSalesForAllMakes(carsJson4test) )


print(getNumOfSalesForAllMakes(newCarsJson))

print("<<<---->>>")
print("<<<---->>>")
print("<<<---->>>")


# print(getting_graph_for_makes(carsJson4test, get_models_for_make(carsJson4test)))
# print(graphing_makes(newCarsJson))

# x,y = dropping_zeroes(getNumOfSalesForAllMakes(carsJson), carsJson4test)
x = newCarsJson
y = getNumOfSalesForAllMakes(newCarsJson)

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], x[i])


plt.bar(y,x)

# calling the function to add value labels
addlabels(y, x)

# giving title to the plot
plt.title("Cars and their sales")

# giving X and Y labels
plt.xlabel("models")
plt.ylabel("Number of sales")

# visualizing the plot
# plt.show()


# print("Danylo")
# # print(x)
# print(y)
# print('Ilya')
# print(graphing_makes(carsJson))
#
#
# print(final_filter('BMW', '3'))




# Data
# groups = ['G1', 'G2', 'G3', 'G4', 'G5']
# values1 = [54, 19, 14, 27, 16]
# values2 = [21, 30, 15, 17, 20]
# values3 = [35, 13, 21, 14, 26]
# values4 = [12, 0, 0, 0, 0]
#
# width = 0.25
#
# fig, ax = plt.subplots()
#
# # Stacked bar chart
# ax.bar(groups, values4, width = width, )
# ax.bar(groups, values3, width = width, )
# ax.bar(groups, values2, width = width,)
# ax.bar(groups, values1, width = width)
#
# plt.show()


# import numpy as np
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])
#
# # Construct arrays for the anchor positions of the 16 bars.
# xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
# xpos = xpos.ravel()
# ypos = ypos.ravel()
# zpos = z
#
# # Construct arrays with the dimensions for the 16 bars.
# dx = dy = 0.5 * np.ones_like(zpos)
# dz = hist.ravel()
#
# ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
#
# plt.show()
#
# print(dropping_zeroes(graphing_makes(carsJson), carsJson4test))


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import RadioButtons
#
#
# t = np.arange(0.0, 2.0, 0.01)
# s0 = np.sin(2*np.pi*t)
# s1 = np.sin(4*np.pi*t)
# s2 = np.sin(8*np.pi*t)
#
# fig, ax = plt.subplots()
# l, = ax.plot(t, s0, lw=2, color='red')
# fig.subplots_adjust(left=0.3)
#
# axcolor = 'lightgoldenrodyellow'
# rax = fig.add_axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
# radio = RadioButtons(rax, ('1 Hz', '2 Hz', '4 Hz'),
#                      label_props={'color': 'cmy', 'fontsize': [12, 14, 16]},
#                      radio_props={'s': [16, 32, 64]})
#
#
# def hzfunc(label):
#     hzdict = {'1 Hz': s0, '2 Hz': s1, '4 Hz': s2}
#     ydata = hzdict[label]
#     l.set_ydata(ydata)
#     fig.canvas.draw()
# radio.on_clicked(hzfunc)
#
# rax = fig.add_axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
# radio2 = RadioButtons(
#     rax, ('red', 'blue', 'green'),
#     label_props={'color': ['red', 'blue', 'green']},
#     radio_props={
#         'facecolor': ['red', 'blue', 'green'],
#         'edgecolor': ['darkred', 'darkblue', 'darkgreen'],
#     })
#
#
# def colorfunc(label):
#     l.set_color(label)
#     fig.canvas.draw()
# radio2.on_clicked(colorfunc)
#
# rax = fig.add_axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
# radio3 = RadioButtons(rax, ('-', '--', '-.', ':'))
#
#
# def stylefunc(label):
#     l.set_linestyle(label)
#     fig.canvas.draw()
# radio3.on_clicked(stylefunc)
#
# plt.show()