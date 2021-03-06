import streamlit as st
from PIL import Image
#import streamlit.components.v1 as components
#import codecs
#gif = 'https://media.giphy.com/media/lXC2gmHf2ypUs/giphy.gif'

def app():

    st.title('Choose to live better...where do you fit in the world?')

    st.write("""
    Choosing where to live in this world full of options is no easy task, 
    so we want to help you find the city that best suits you.
    """)

    st.image(
            "https://media.giphy.com/media/lXC2gmHf2ypUs/giphy.gif", 
            width=400,
        ),

    st.write("""
    # First of all, we must determine which profile fits you best. 
    """)

    st.write("""
    ## The Innovator
    """)
    st.image(
            "https://media4.giphy.com/media/KgX7on3DWfGSKGK8eI/giphy.gif?cid=790b7611eb97da974432dc309ce665579aa3b25d8eb05987&rid=giphy.gif&ct=g", 
            width=500,
        ),
    st.write("""
    ##### The profile of the innovator is characterized by being a person who proactively seeks opportunities. 
    ##### If you have the soul of an entrepreneur and are looking for a new place that is in full growth, but where you don't have to spend a fortune on rent, this could be the group for you.
    """)

    st.write("""
    ## The Traveler
    """)
    st.image(
                "https://media1.giphy.com/media/14wXMGbHjXK2k0/giphy.gif?cid=790b761124c0b8d1e2a98d1c3bdf3d95f529be35546c7c30&rid=giphy.gif&ct=g", 
                width=400,
            ),
    st.write("""
    ##### If you are a person who loves to travel on every free weekend and are looking for a well-connected, safe place to live, this group may be for you.
    """)

    st.write("""
    ## The Posh
    """)
    st.image(
            "https://media4.giphy.com/media/YqzBnP1DqgzJqXysb1/giphy.gif?cid=790b7611473f7a597b3430267ffd75a17966ae6def587191&rid=giphy.gif&ct=g", 
            width=400,
        ),
    st.write("""
    ##### If you like the good life, luxury, and don't mind having to spend a bundle on rent this could be the group for you. Just don't forget to check the budget before you move in.
    """)

    st.write("""
    ## Do you already know which group you identify with? You can go to the "Profiles" tab to discover your cities.
    """)