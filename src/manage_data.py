import pandas as pd

#data = pd.read_csv("data/user_limpio.csv")
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

def copia_sn_bool(resp):#pseudocodigo Sonia revisar importacion de csv en streamlit
    '''
    This function transforms the answer into boolean
    '''
    data = pd.read_csv(f"data/{resp}.csv")
    return data

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
    rslt_df = dataframe[(dataframe['Escala_de_Educacion'] == f"{educ}") &
            (dataframe['Escala_de_Tolerancia'] == f"{tol}") & 
            (dataframe['Escala_de_Sunshine'] == f"{sun}")]
    
    Cities_match = rslt_df
    return Cities_match

def mapa():
    pass
