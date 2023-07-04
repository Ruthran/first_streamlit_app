import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('Healthy Dinner')
streamlit.header('Breakfast')
streamlit.text('🥣 One cup of mile')
streamlit.text('🐔 Egg Omlet')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# With Filter
streamlit.dataframe(fruits_to_show)
#Full List
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# streamlit.text(fruityvice_response.json())

# Normalizing Json data with Pandas
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# creating dataframe with json data
streamlit.dataframe(fruityvice_normalized)

#Snowflake Connection
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#fruit_load_list
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The Fruit load list contains:")
streamlit.text(my_data_row)
