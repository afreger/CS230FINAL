import pandas as pd

# 1) Read the file and print the DataFrame
df = pd.read_csv('C:/Users/andre/Downloads/EcarSalesByCountryAndYear.csv')
print("1) Original DataFrame:")
print(df)

# 2) Re-read the file using 'Country' as the index and print the DataFrame
df = pd.read_csv('C:/Users/andre/Downloads/EcarSalesByCountryAndYear.csv', index_col='Country')
print("\n2) DataFrame with Country as Index:")
print(df)

# 3) Calculate sales growth between 2021 and 2020 and add as a new column
df['Growth'] = (df['Sales2021'] - df['Sales2020']) / df['Sales2020']
print("\n3) DataFrame with Growth column:")
print(df)

# 4) Convert the 'Growth' column to a percentage and print the DataFrame
df['Growth'] *= 100
print("\n4) Growth column as a percentage:")
print(df)

# 5) Round the 'Growth' column to 1 decimal place and print the DataFrame
df['Growth'] = df['Growth'].round(1)
print("\n5) Growth column rounded to 1 decimal place:")
print(df)

# 6) Sort the DataFrame by 'Growth' from high to low and print
df = df.sort_values(by='Growth', ascending=False)
print("\n6) DataFrame sorted by Growth (high to low):")
print(df)

# 7) Create a new DataFrame `dfRecent` with only Sales2021 and Sales2020
dfRecent = df[['Sales2021', 'Sales2020']]
print("\n7) dfRecent with Sales2021 and Sales2020:")
print(dfRecent)

# 8) Filter dfRecent for only 'United States' and 'Canada' and print
dfFiltered = dfRecent.loc[['Canada', 'United States']]
print("\n8) dfRecent filtered for United States and Canada:")
print(dfFiltered)

# 9) Display total sales across countries for 2020 and 2021
total_sales = dfRecent.sum()
print("\n9) Total sales across countries for 2020 and 2021:")
print(total_sales)

# 10) Calculate and display sales by continent by year
# Assuming we have a mapping of countries to continents
continent_mapping = {
    'Canada': 'AMERICA', 'United States': 'AMERICA',
    'China': 'ASIA', 'Japan': 'ASIA',
    'France': 'EUROPE', 'Germany': 'EUROPE',
    'United Kingdom': 'EUROPE'
    # Add other countries as needed
}
df['Continent'] = df.index.map(continent_mapping)
continent_sales = df.groupby('Continent').sum()
print("\n10) Sales by Continent by Year:")
print(continent_sales)

# 11) Calculate 2021 vs 2020 growth in electric car sales, by continent
continent_sales['Growth'] = ((continent_sales['Sales2021'] - continent_sales['Sales2020']) / continent_sales['Sales2020'] * 100).round(1)
print("\n11) 2021 vs 2020 growth by continent:")
print(continent_sales['Growth'])
