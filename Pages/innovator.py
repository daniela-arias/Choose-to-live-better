import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

def app():

    df = pd.read_csv("Data/Innovator.csv")
    inno = df.profile_report()
    
    st_profile_report(inno)