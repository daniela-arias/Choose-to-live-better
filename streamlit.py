import streamlit as st 
import pandas as pd
from PIL import Image
from multipage import MultiPage
from Pages import home
from Pages import Profile
from Pages import innovator
from Pages import Traveler
from Pages import Posh
from Pages import Cities

app = MultiPage()

app.add_page('Home', home.app)
app.add_page('Profiles', Profile.app)
#app.add_page('The Innovator', innovator.app)
#app.add_page('The Traveler', Traveler.app)
#app.add_page('The Posh', Posh.app)
#app.add_page('Yours Cities', Cities.app)


app.run()