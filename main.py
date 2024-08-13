import streamlit as st
st.header('currency converter')
st.subheader('choose your rate')
options=["usd-ksh",'ksh-usd']
selected_option=st.selectbox("select column",options)

# inp=st.text_input("enter")

try:
    
    inp=float(st.text_input("enter"))
    
except :
    st.header("you have enterd a string insted of a number")
    st.write("enter a number")
    inp='undifiend'
st.header(selected_option)
if selected_option == 'ksh-usd':
    
    if inp == 'undifiend':
        inp=0
        
    result=inp / 129
    result=str(result)
    st.write(f'{result} $usd')
if selected_option == "usd-ksh":
    if inp == 'undifiend':
        inp=0
    result=inp * 129
    result=str(result)
    st.write(f'{result} ksh')
else:
    result=''