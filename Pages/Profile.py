import streamlit as st
import pandas as pd
from PIL import Image
import src.manage_data as dat
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import folium_static

def app():

    st.title("""
    Congratulations! You are now closer to finding the place that best suits you. Let's keep digging into your interests.
    Complete the following options:
    """)

    Prof = st.selectbox("""
    Select your profile:
    """, dat.profiles_chooice())
    st.write(f"{Prof}")

    st.title("""
    When it comes to emigrating, there are many factors to take into account, and we should always prioritize some over others. 
    Next, you will have to select how relevant the categories are in relation to the country you are going to. 
    """)

    Educ = st.selectbox("""
    What level of education should the country where you will live offer you?:
    """, dat.level())
    st.write(f"{Educ}")

    Tol = st.selectbox("""
    The country's culture in relation to LGBT tolerance is for many a must, how relevant is this aspect in your choice?:
    """, dat.level())
    st.write(f"{Tol}")

    Sun = st.selectbox("""
    We know that the weather is important in our day to day life, how frequent should be the sunny days?:
    """, dat.level())
    st.write(f"{Sun}")

    #Empezamos a usar las respuestas del usuario
    mydf = dat.copia_sn_bool(Prof)
    final_match_df = dat.ciudades_match(mydf,Educ,Tol,Sun)

    st.write('''
        These are the cities that best suit you:
    ''')
    try:
        Cities = st.dataframe(final_match_df.Cities)
    except:
        st.write("""
        Sorry, we have not found any cities matching your search. Try changing some parameters.
        """)

    Final_City = st.selectbox("""
    Learn more about each city.
    """, list(final_match_df.Cities.unique()))

    folium_static(dat.mapa_city(Final_City))

    #st.write(f"{Final_City}")    

    #st.dataframe(final_match_df)