import streamlit as st 
import pandas as pd
from PIL import Image
from multipage import MultiPage
from Pages import home
from Pages import Interests



app = MultiPage()

st.title('Choose to live better...where do you fit in the world?')

app.add_page('Home', home.app)
app.add_page('Interests', Interests.app)

app.run()