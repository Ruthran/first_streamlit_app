import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
#streamlit.dataframe(my_fruit_list)

def get_fruityvice_data(this_fruit_choise):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choise)
    # Normalizing Json data with Pandas
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # creating dataframe with json data
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get the information");
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  Streamlit.error()
  
#  streamlit.write('The user entered ', fruit_choice)
#  streamlit.text(fruityvice_response.json())

# streamlit.stop();


#Snowflake Connection
streamlit.header("The Fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        #fruit_load_list
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
#What fruit would you like to add?

def insert_row_snowflake():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')") 
        return "Thanks for adding " + new_fruit
add_my_fruits = streamlit.text_input('What fruit would you like to add?')
if streamlit.Button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake (add_my_fruit)
    streamlit.text(back_from_function)
    
streamlit.header("Fruityvice Fruit Advice!")
streamlit.write('Thanks for adding ', add_my_fruits)

#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')");
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruits)
