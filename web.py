
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of disease Outbreaks",
                   layout='wide',
                   page_icon=":doctor:")

diabetes_model = pickle.load(open(r"diabetes_model.sav", "rb"))
heart_disease_model=pickle.load(open(r"heart_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"parkinsons_model.sav",'rb'))

with st.sidebar:
    selected=option_menu("Prediction of disease outbreak system",
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected=='Diabetes Prediction':
    st.title("Diabetes Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input("Number of Pregnancies")
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        Bloodpressure=st.text_input("Blood Pressure value")
    with col1:
        SkinThickness=st.text_input("Skin Thickness value")
    with col2:
        Insulin=st.text_input("Insulin level")
    with col3:
        BMI=st.text_input("BMI value")
    with col1:
        DiabetesPedigreefunction=st.text_input("Diabetes Pedigree Function")
    with col2:
        Age=st.text_input("Age of the Person")

    diab_diagnosis = ''
    if st.button("Diabetes Test Result"):
        user_input=[Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,
                BMI,DiabetesPedigreefunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis="The Person is diabetic"
        else:
            diab_diagnosis="The Person is not diabetic"
    st.success(diab_diagnosis)

elif selected=='Heart Disease Prediction':
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.text_input("Age of the Person")
    with col2:
        Sex=st.text_input('Sex of the Person')
    with col3:
        CP=st.text_input("Chest Pain value")
    with col1:
        Trestbps=st.text_input("Resting Blood Pressure value")
    with col2:
        Chol=st.text_input("Cholesterol level")
    with col3:
        Fbs=st.text_input("Fasting Blood Sugar value")
    with col1:
        Restecg=st.text_input("Resting electrocardiographic result")
    with col2:
        Thalach=st.text_input("Max heart rate achieved")
    with col3:
        Exang=st.text_input("Exercise induced angina")
    with col1:
        Oldpeak=st.text_input("Oldpeak value")
    with col2:
        Slope=st.text_input("Slope")
    with col3:
        Ca=st.text_input("Number of major vessels")
    with col1:
        Thal=st.text_input(" Thalassemia")

    heart_diagnosis = ''
    if st.button("Heart Disease Test Result"):
        user_input=[Age,Sex,CP,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal]
        user_input=[float(x) for x in user_input]
        heart_prediction=heart_disease_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis="The Person has Heart Disease"
        else:
            heart_diagnosis="The Person has not Heart Disease"
    st.success(heart_diagnosis)

elif selected=='Parkinsons Prediction':
    st.title("Parkinsons Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        MDVPFo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVPFhi=st.text_input("MDVP:Fhi(Hz)")
    with col3:
        MDVPFlo=st.text_input("MDVP:Flo(Hz)")
    with col1:
        MDVPJitter=st.text_input("MDVP:Jitter(%)")
    with col2:
        MDVPJitterAbs=st.text_input("MDVP:Jitter(Abs)")
    with col3:
        MDVPRAP=st.text_input("MDVP:RAP")
    with col1:
        MDVPPPQ=st.text_input("MDVP:PPQ")
    with col2:
        JitterDDP=st.text_input("Jitter:DDP")
    with col3:
        MDVPShimmer=st.text_input("MDVP:Shimmer")
    with col1:
        MDVPShimmerdB=st.text_input("MDVP:Shimmer(dB)")
    with col2:
        ShimmerAPQ3=st.text_input("Shimmer:APQ3")
    with col3:
        ShimmerAPQ5=st.text_input("Shimmer:APQ5")
    with col1:
        MDVPAPQ=st.text_input("MDVP:APQ")
    with col2:
        ShimmerDDA=st.text_input("Shimmer:DDA")
    with col3:
        NHR=st.text_input("Noise-to-harmonics ratio")
    with col1:
        HNR=st.text_input("Harmonics-to-noise ratio")
    with col2:
        RPDE=st.text_input("RPDE")
    with col3:
        DFA=st.text_input("DFA")
    with col1:
        spread1=st.text_input("Spread1")
    with col2:
        spread2=st.text_input("Spread2")
    with col3:
        D2=st.text_input("D2")
    with col1:
        PPE=st.text_input("Pitch Period Entropy")

    parkinsons_diagnosis = ''
    if st.button("Parkinsons Disease Test Result"):
        user_input=[MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitterAbs,
                MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmer,ShimmerAPQ3,ShimmerAPQ5,
                MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input=[float(x) for x in user_input]
        parkinsons_prediction=parkinsons_model.predict([user_input])
        if parkinsons_prediction[0]==1:
            parkinsons_diagnosis="The Person has Parkinsons disease"
        else:
            parkinsons_diagnosis="The Person has not Parkinsons disease"
    st.success(parkinsons_diagnosis)