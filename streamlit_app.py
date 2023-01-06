import streamlit
import requests
import snowflake.connector

my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains")
streamlit.dataframe(my_data_row)
streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🍝Omega 3 & Blueberry Oatmeal")
streamlit.text("🦪🥪Avacado Toast")
import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
fruits_selected = streamlit.multiselect("Pick:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruitvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information abour?','Kiwi')
streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
fruitvice_jsonnormalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.text(fruityvice_response.json())
streamlit.dataframe(fruitvice_jsonnormalized)
