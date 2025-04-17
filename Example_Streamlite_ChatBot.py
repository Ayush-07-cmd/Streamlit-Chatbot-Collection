import streamlit as st

st.title("This is first application")
st.header("Hello this is streamlit app")
st.subheader("This is a subheader")
st.text("Welcome to the world of Streamlit!")

# Text input
name = st.text_input("Enter your name")

if st.button("Submit"):
    st.write("Hello", name)

# Checkbox
if st.checkbox("Show Secret Message"):
    st.write("You discovered a hidden message!")

# Selectbox
option = st.selectbox("Choose your favorite language:",
                      ["Python", "Java", "C++", "JavaScript"])
st.write("You selected:", option)

# Slider
age = st.slider("Select your age:", 1, 100, 25)
st.write("Your age is", age)