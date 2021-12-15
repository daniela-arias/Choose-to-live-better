import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import src.manage_data as dat

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
    Cities = st.dataframe(final_match_df.Cities)

    st.write("These are the cities that best suit you:")
    st.write(f"{Cities}")

    st.dataframe(final_match_df)