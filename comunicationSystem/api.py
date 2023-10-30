import pandas as pd
import random as random
import requests

def requestRandomThing(df, columna):

    while True:
        id_random = random.choice(df["ID"])
        url = f"https://fortnite-api.com/v2/cosmetics/br/{id_random}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['name']


#Skin random
def requestRandomSkins():

    df = pd.read_csv('./data/skinsFortnite.csv')

    response = requestRandomThing(df, "ID")

    return response
    

#Emotes random
def requestRandomEmote():

    df = pd.read_csv('./data/emotesFortnite.csv')

    response = requestRandomThing(df, "ID")

    return response


#Glider random
def requestRandomGlider():

    df = pd.read_csv('./data/glidersFortnite.csv')

    response = requestRandomThing(df, "ID")

    return response
