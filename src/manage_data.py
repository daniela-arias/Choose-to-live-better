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

def sn_bool(resp):
    '''
    This function transforms the answer into boolean
    '''
    if resp == "Innovator":
        return 0
    if resp == "Traveler":
        return 1
    if resp == "Posh":
        return 2

def level():
    '''
    This function allows you to choose a level 
    '''
    lv = ["Alto", "Medio", "Bajo"]
    return lv

def level_bool(resp):
    '''
    This function transforms yes or no into boolean
    '''
    if resp == "Alto":
        return 0
    if resp == "Medio":
        return 1
    if resp == "Bajo":
        return 2