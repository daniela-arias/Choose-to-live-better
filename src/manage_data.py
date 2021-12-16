from os import get_inheritable
import pandas as pd
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import streamlit as st
from streamlit_folium import folium_static



datitos_coord = pd.read_csv("data/user_coord.csv")
#data.drop("Unnamed: 0", axis=1, inplace=True)

#-------------------------------------------------
#Profile
#-------------------------------------------------

def profiles_chooice():
    '''
    This function let you choose between your profiles
    '''
    sn = ["Innovator", "Traveler", "Posh"]
    return sn

def copia_sn_bool(resp):
    '''
    This function transforms the answer into boolean
    '''
    data = pd.read_csv(f"data/{resp}.csv")
    return data

def cargadataframe(resp):
    data_pk = pd.read_pickle(f"data/{resp}_pk.pkl")
    return data_pk

def level():
    '''
    This function allows you to choose a level 
    '''
    lv = ["Alto", "Medio", "Bajo"]
    return lv

def ciudades_match(dataframe,educ,tol,sun):
    '''
    This function give us the cities that match with the profile
    '''
    try:
        rslt_df = dataframe[(dataframe['Escala_de_Educacion'] == f"{educ}") &
                (dataframe['Escala_de_Tolerancia'] == f"{tol}") & 
                (dataframe['Escala_de_Sunshine'] == f"{sun}")]
        return rslt_df
    except:
        return ("Sorry, we have not found any cities matching your search. Try changing some parameters.")

def mapa_city(resp):
    row_city = datitos_coord[(datitos_coord['Cities'] == f"{resp}")]
    lat = row_city["lat"]
    long = row_city["long"]
    #latlong = row_city["Coordenadas"][0]
    fig = folium.Map(location=(lat,long), zoom_start=15)
    return fig

#def info_city(resp):
    #row_city_description = datitos_coord[(datitos_coord['Cities'] == f"{resp}")]
    #st.write(type("mi print",row_city.iloc[0]["Coordenadas"])
    #st.write()
    #pass


    
        