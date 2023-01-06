import streamlit
import requests
import snowflake.connector
import pandas
from urllib.error import URLError
my_cur=my_cnx.cursor()
streamlit.text("The fruit load list contains")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
if streamlit.button("Get fruit load list"):
    my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    streamlit.dataframe(my_data_row)


streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🍝Omega 3 & Blueberry Oatmeal")
streamlit.text("🦪🥪Avacado Toast")

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruitvice_jsonnormalized = pandas.json_normalize(fruityvice_response.json())
    return fruitvice_jsonnormalized
        
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
fruits_selected = streamlit.multiselect("Pick:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruitvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information abour?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
        back_from_function =get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
#streamlit.text(fruityvice_response.json())


streamlit.write('The user entered',fruit_choice)
fruit_sfselect = streamlit.text_input("what fruit would you like to add?",'jackfruit')
streamlit.text("Thanks for adding"+fruit_sfselect)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")