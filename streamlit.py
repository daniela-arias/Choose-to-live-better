import streamlit as st 
import pandas as pd
from PIL import Image
from multipage import MultiPage
from streamlit_pages import home
from streamlit_pages import Segundo_ejemplo



app = MultiPage()

st.title('Choose to live better...where do you fit in the world?')

app.add_page('Home', home.app)
app.add_page('Segundo_ejemplo', graphs.app)


app.run()