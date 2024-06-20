# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:38:25 2024

@author: 91749
"""
import pickle
import streamlit as st 
load=open('Logistic.pkl','rb')
model=pickle.load(load)

def predict(Pclass,Age,SibSp,Parch,Fare,Embarked_C,Embarked_Q,Embarked_S):
    prediction=model.predict([[Pclass,Age,SibSp,Parch,Fare,Embarked_C,Embarked_Q,Embarked_S]])
    return prediction

def main():
    st.title('Predicting the Survival of Titanic Passengers :seat:')
    Pclass=st.number_input("PClass: ")
    Age=st.number_input("Age: ")
    SibSp=st.number_input("sbisp: ")
    Parch=st.number_input("Pearch: ")
    Fare=st.number_input("Fare: ")
    Embarked_C=st.number_input("Embarked_c: ")
    Embarked_Q=st.number_input("Embarked_Q: ")
    Embarked_S=st.number_input("Embarked_S: ")
    
    if st.button('predict'):
        result=predict(Pclass, Age, SibSp, Parch, Fare, Embarked_C, Embarked_Q, Embarked_S)  
        if result==0:
            st.success("NO Survived")
      
    else:
        st.success('Survived')        
  
        
if __name__ == '__main__':
    main()       



