import streamlit as st
from PIL import Image
#import streamlit.components.v1 as components
#import codecs
#gif = 'https://media.giphy.com/media/lXC2gmHf2ypUs/giphy.gif'

def app():

    st.write("""
    Choosing where to live in this world full of options is no easy task, 
    so we want to help you find the city that best suits you.
    """)
    portada = Image.open("images/travel-world.jpeg")
    #portada = Image.open(gif)
    st.image(portada, use_column_width=True)

    st.write("""
    # First of all, we must determine which profile fits you best. 
    """)

    st.write("""
    ## The Homey
    """)

    st.write("""
    ## The Traveler
    """)

    st.write("""
    ## The cultural
    """)