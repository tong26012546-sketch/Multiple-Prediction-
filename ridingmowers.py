import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
 
#import model
loan_model = pickle.load(open("loan_model.sav",'rb'))
heart_model = pickle.load(open("heartmodel.sav",'rb'))
Riding_model = pickle.load(open("RidingMowers.sav"'rb'))
 
with st.sidebar:
    selcted = option_menu('Loan and heart prediction',
                          ['Loan','heart','RidingMowers'],
                          default_index=0)
if(selcted == 'RidingMowers'):
    st.title("RidingMowers Prediction")
    #input data
    Incoms = st.text_input('Incoms')
    Lotsize = st.text_input('Lotsize')
    #predict
    RidingMowers = ''
    if st.button('RidingMowers Owner/nonOwner test'):
        RidingMowers_accept = Riding_model.predict([[
            float(Incoms),
            float(Lotsize)
 
        ]])
        if(RidingMowers[0]== 0):
            RidingMowers = 'not accept'
        else:
            RidingMowers = 'Accept'
    st.success(RidingMowers)
if(selcted == 'heart'):
    st.title('Heart Prediction')
    age = st.text_input('age')
    sex = st.text_input('sex')
    cp = st.text_input('cp')
    trestbps = st.text_input('trestbps')
    chol = st.text_input('chol')
    fbs = st.text_input('fbs')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
    #predict
    heart_predict = ''
    if st.button('Heart Prediction'):
        heart_predict = heart_model.predict([[
            float(age),
            float(sex),
            float(cp),
            float(trestbps),
            float(chol),
            float(fbs),
            float(restecg),
            float(thalach),
            float(exang),
            float(oldpeak),
            float(slope),
            float(ca),
            float(thal)
        ]])
        if(heart_predict[0]== 0):
            heart_predict = 'not have heart Disease'
        else:
            heart_predict = 'You have haert Disease'
    st.success(heart_predict)