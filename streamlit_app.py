import streamlit

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🍝Omega 3 & Blueberry Oatmeal")
streamlit.text("🦪🥪Avacado Toast")
import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
streamlit.multiselect("Pick:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
