import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ListOfPistols.csv")


# Oldest Pistols

# sortedByYear = df.sort_values('Year').head(7)
#
# x = sortedByYear['Name']
# y = sortedByYear['Year']
#
# plt.plot(x, y, 'ro-')
# plt.xlabel('Pistol')
# plt.ylabel('Year')
# plt.title('Oldest Pistols')
#
# plt.grid(color='k', ls='-', lw=0.53)
#
# plt.show()


# The Pistols Cartridge

# cartridgeSum = df.groupby('Cartridge').size().sort_values(ascending=False).head(8)
# bullet = cartridgeSum.index
#
# fig, ax = plt.subplots()
#
# ax.pie(cartridgeSum, labels=bullet, autopct='%1.1f%%', shadow=True, startangle=100)
# ax.set_title('The Pistols Cartridge')
#
# plt.show()


# Countries

# producer = df.groupby('Country').size().sort_values(ascending=False).head(10)
# countryName = producer.index
#
# fig, ax = plt.subplots()
#
# ax.pie(producer, labels=countryName, autopct='%1.1f%%', shadow=True, startangle=100)
# ax.set_title('Countries that produced the most pistols')
#
# plt.show()


# Manufacturer

# manufacturerSum = df.groupby('Manufacturer').size().sort_values(ascending=False).head(6)
# manufacturer = manufacturerSum.index
# bar_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:olive']
#
# fig, ax = plt.subplots()
#
# ax.bar(manufacturer, manufacturerSum, color=bar_colors, width=0.44)
# ax.set_xlabel('Manufacturer')
# ax.set_ylabel('Number of Pistol Types')
# ax.set_title('Manufacturers that Have the Most Pistol Types')
#
# plt.show()





