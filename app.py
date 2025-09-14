import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ListOfPistols.csv")

def oldest_pistols():
    sortedByYear = df.sort_values('Year').head(6)
    plt.plot(sortedByYear['Name'], sortedByYear['Year'], 'ro-')
    plt.xlabel('Pistol')
    plt.ylabel('Year')
    plt.title('Oldest Pistols')
    plt.grid(color='k', ls='-', lw=0.53)
    plt.show()

def pistols_cartridge():
    cartridgeSum = df.groupby('Cartridge').size().sort_values(ascending=False).head(8)
    plt.pie(cartridgeSum, labels=cartridgeSum.index, autopct='%1.1f%%', shadow=True, startangle=100)
    plt.title('The Pistols Cartridge')
    plt.show()

def countries():
    producer = df.groupby('Country').size().sort_values(ascending=False).head(10)
    plt.pie(producer, labels=producer.index, autopct='%1.1f%%', shadow=True, startangle=100)
    plt.title('Countries that produced the most pistols')
    plt.show()

def manufacturers():
    manufacturerSum = df.groupby('Manufacturer').size().sort_values(ascending=False).head(6)
    bar_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:olive']
    plt.bar(manufacturerSum.index, manufacturerSum, color=bar_colors, width=0.44)
    plt.xlabel('Manufacturer')
    plt.ylabel('Number of Pistol Types')
    plt.title('Manufacturers with Most Pistol Types')
    plt.show()

options = {
    "1": oldest_pistols,
    "2": pistols_cartridge,
    "3": countries,
    "4": manufacturers
}

choice = input("Choose a chart:\n1. Oldest Pistols\n2. Pistols Cartridge\n3. Countries\n4. Manufacturers\n> ")
if choice in options:
    options[choice]()
else:
    print("Invalid choice")
