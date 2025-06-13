import streamlit as st

st.title("Power Calculator")

st.write("Enter a number to calculate its square, cube and fifth power")

n=st.number_input("Enter an integer",value=1,step=1)

#Calculate the results

st.write("The Square of the number is ", n**2)
st.write("The Cube of the number is ", n**3)
st.write("The 5th power of the number is ", n**5)