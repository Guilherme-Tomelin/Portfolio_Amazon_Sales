import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

lista = ["um", "dois"]

category = st.sidebar.selectbox("Categoria", lista)


class DfHandler:
    def __init__(self):
        self.df =  pd.read_csv('amazon.csv')

    def get_df(self):
        self.__split_categories()
        return self.df
        
    def __split_categories(self):
        self.df['category'] = self.df['category'].str.split('|')

















# class Product:
#     def __init__(self, product_id, product_name, category, discounted_price, actual_price, discount_percentage, rating, rating_count, about_product, user_id, user_name, review_id, review_title, review_content, img_link, product_link):
#         self.product_id = product_id
#         self.product_name = product_name
#         self.category = category
#         self.discounted_price = discounted_price
#         self.actual_price = actual_price
#         self.discount_percentage = discount_percentage
#         self.rating = rating
#         self.rating_count = rating_count
#         self.about_product = about_product
#         self.user_id = user_id
#         self.user_name = user_name
#         self.review_id = review_id
#         self.review_title = review_title
#         self.review_content = review_content
#         self.img_link = img_link
#         self.product_link = product_link
