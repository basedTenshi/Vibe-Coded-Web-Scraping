import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

df = pd.DataFrame([{'title': 'A Light in the Attic', 'price': '£51.77', 'rating': 'Three'}, {'title': 'Tipping the Velvet', 'price': '£53.74', 'rating': 'One'}, {'title': 'Soumission', 'price': '£50.10', 'rating': 'One'}, {'title': 'Sharp Objects', 'price': '£47.82', 'rating': 'Four'}, {'title': 'Sapiens: A Brief History of Humankind', 'price': '£54.23', 'rating': 'Five'}, {'title': 'The Requiem Red', 'price': '£22.65', 'rating': 'One'}, {'title': 'The Dirty Little Secrets of Getting Your Dream Job', 'price': '£33.34', 'rating': 'Four'}, {'title': 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull', 'price': '£17.93', 'rating': 'Three'}, {'title': 'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics', 'price': '£22.60', 'rating': 'Four'}, {'title': 'The Black Maria', 'price': '£52.15', 'rating': 'One'}, {'title': 'Starving Hearts (Triangular Trade Trilogy, #1)', 'price': '£13.99', 'rating': 'Two'}, {'title': "Shakespeare's Sonnets", 'price': '£20.66', 'rating': 'Four'}, {'title': 'Set Me Free', 'price': '£17.46', 'rating': 'Five'}, {'title': "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)", 'price': '£52.29', 'rating': 'Five'}, {'title': 'Rip it Up and Start Again', 'price': '£35.02', 'rating': 'Five'}, {'title': 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', 'price': '£57.25', 'rating': 'Three'}, {'title': 'Olio', 'price': '£23.88', 'rating': 'One'}, {'title': 'Mesaerion: The Best Science Fiction Stories 1800-1849', 'price': '£37.59', 'rating': 'One'}, {'title': 'Libertarianism for Beginners', 'price': '£51.33', 'rating': 'Two'}, {'title': "It's Only the Himalayas", 'price': '£45.17', 'rating': 'Two'}])
df_sorted = df.sort_values(by='price', ascending=False)

plt.figure(figsize=(8,5))
plt.scatter(df_sorted['price'], df_sorted['title'], color='teal')
plt.ylabel('Price')
plt.xlabel('Title')
plt.title('Books from Highest to Lowest Price')
plt.xticks(rotation=45)
plt.show()

