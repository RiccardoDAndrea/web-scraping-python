from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_largest_German_companies'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
fortune_list_2023_soup = soup.find_all('table')[0]

## Another way to find the table
fortune_list_2023_soup_2 = soup.find('table', class_='wikitable sortable') # another way to find the table


th_columns = fortune_list_2023_soup.find_all('th')
df_columns = [th.text.strip() for th in th_columns]
df = pd.DataFrame(columns = df_columns)


column_data = fortune_list_2023_soup.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data


## Second example to retrive data
url_french = 'https://en.wikipedia.org/wiki/List_of_largest_French_companies'
response_for_french = requests.get(url_french)
soup_france = BeautifulSoup(response_for_french.text, 'html.parser')
fortunue_french_list_html = soup_france.find_all('table')[0]

th_columns_for_french = fortunue_french_list_html.find_all('th')
df_columns_for_french = [columns_french_df.text.strip() for columns_french_df in th_columns_for_french]
df_for_french = pd.DataFrame(columns = df_columns_for_french)

column_data_french = fortunue_french_list_html.find_all('tr')
for row_french in column_data_french[1:]:
    row_data_fench = row_french.find_all('td')
    individual_row_data_french = [data_french.text.strip() for data_french in row_data_fench]
    length_for_franch = len(df_for_french)
    df_for_french.loc[length_for_franch] = individual_row_data_french
print(df_for_french)


#### 3
url = 'https://ecommercegermany.com/blog/top-100-companies-in-germany'
response_ger = requests.get(url)
soup_ger = BeautifulSoup(response_ger.text, 'html.parser')
fortune_list_2023_soup_ger_html = soup_ger.find_all('table')[0]
#fortune_list_2023_soup_ger = soup.find('figure', class_='wp-block-table') # another way to find the table
fortune_list_2023_soup_ger_html = fortune_list_2023_soup_ger_html.find_all('td')

df_columns_ger = [th_ger.text.strip() for th_ger in fortune_list_2023_soup_ger_html]
df_ger = pd.DataFrame(columns = df_columns_ger)
print(df_ger)
# for row_ger in fortune_list_2023_soup_ger_html[1:]:
#     row_data_ger = row_ger.find_all('td')
#     individual_row_data_ger = [data_ger.text.strip() for data_ger in row_data_ger]
#     length = len(df)
#     df.loc[length] = individual_row_data
