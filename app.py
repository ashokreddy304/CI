import streamlit as st
st.title('Power Calcuator')
st.write('Enter a number to calculater its aquare, cube, and fith power.')

#get user input
n = st.number_input('Enter an integer',value=1,step=1)

#calculate results
square = n**2
cube = n**3
fifth_power = n**5

# Display results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")