import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

def app():
    
    df = pd.read_csv("Data/Posh.csv")
    pos = df.profile_report()

    st_profile_report(pos)