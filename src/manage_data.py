from os import get_inheritable
import pandas as pd
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import streamlit as st
from streamlit_folium import folium_static


datitos_coord = pd.read_csv("data/user_coord.csv")
user_data = pd.read_csv("Data/Data_clean_user.csv")
user_data.drop("Unnamed: 0", axis=1, inplace=True)

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
    '''
    This function shows the map of the selected city. 
    '''
    row_city = datitos_coord[(datitos_coord['Cities'] == f"{resp}")]
    lat = row_city["lat"]
    long = row_city["long"]
    #latlong = row_city["Coordenadas"][0]
    fig = folium.Map(location=(lat,long), zoom_start=15)
    return fig

def info_city(resp):
    row_info = user_data[(user_data["Cities"] == f"{resp}")]
    st.subheader("The city")
    st.write(row_info['Cities'])
    st.write(row_info['Description'])
    st.write(row_info['Poblacion'])
    st.write(row_info['Climate'])
    st.subheader("The economy")
    st.write(row_info['Growth_percentage'])
    st.write(row_info['GDP_per_capita'])
    st.write(row_info['Unemployment_percentage'])
    st.write(row_info['VAT_Sales_Tax'])
    st.write(row_info['Currency_for_urban_area'])
    st.subheader("Tolerance")
    st.write(row_info['Homosexuality_acceptance'])
    st.write(row_info['LGBT_adoption_rights'])
    st.write(row_info['LGBT_homosexuality_rights'])
    st.write(row_info['LGBT_marriage_rights'])
    st.subheader("Culture")
    st.write(row_info['Art_galleries'])
    st.write(row_info['Concert_venues'])
    st.write(row_info['Museums'])
    st.write(row_info['Sport_venues'])
    st.subheader("Connectivity")
    st.write(row_info['Monthly_Fitness_Club_Membership'])
    st.write(row_info['Beer'])
    st.write(row_info['Lunch'])
    st.subheader("Daily cost of living")
    st.write(row_info['Airport_hub'])
    st.write(row_info['Intercity_train_connectivity'])
    st.subheader("Safety")
    st.write(row_info['Gun_related_deaths'])
    st.write(row_info['Guns_per_residents'])
    st.subheader("Education")
    st.write(row_info['Pisa_ranking'])
    st.write(row_info['Best_university'])
    st.subheader("Housing")
    st.write(row_info['Large_apartment'])
    st.write(row_info['Medium_apartment'])
    st.write(row_info['Small_apartment'])
    return row_info


    
        