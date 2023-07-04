import streamlit
import pandas
import requests

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
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
