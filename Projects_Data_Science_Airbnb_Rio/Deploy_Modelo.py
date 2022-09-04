#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import streamlit as st
import joblib
 
x_numericos = {'host_listings_count': 0, 'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'security_deposit': 0, 'cleaning_fee': 0, 'extra_people': 0, 'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_response_rate': 0}
 
x_true_false = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Hostel', 'House', 'Loft', 'Serviced apartment', 'Outros'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'], 
            'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period'], 
            'host_response_time': ['a few days or more', 'never answered', 'within a day', 'within a few hours', 'within an hour']
           }

dicionario = {}
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0

for item in x_numericos:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format='%.5f')
    elif item == 'extra_people' or item == 'security_deposit' or item == 'cleaning_fee' or item == 'host_response_rate':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    x_numericos[item] = valor
    
for item in x_true_false:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == 'Sim':
        x_true_false[item] = 1
    else:
        x_true_false[item] = 0
    
for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[item])
    dicionario[f'{item}_{valor}'] = 1
    
botao = st.button('Prever Valor do Imóvel')

if botao:
    dicionario.update(x_numericos)
    dicionario.update(x_true_false)
    valores_x = pd.DataFrame(dicionario, index=[0])
    modelo = joblib.load('modelo.joblib')
    preco = modelo.predict(valores_x)
    st.write(preco[0])

