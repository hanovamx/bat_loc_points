import streamlit as st
import pandas as pd

# URL of the Excel file in the GitHub repository
excel_url = 'https://github.com/hanovamx/bat_loc_points/raw/main/Brands%20Week%20Bank.xlsx'

def leer_datos(url):
    return pd.read_excel(url, sheet_name="Bank", index_col="Pers.No.", engine='openpyxl')

def validacion(bank, no_empleado):
    return no_empleado in bank.index

def mostrar_balance(bank, no_empleado):
    return bank.loc[no_empleado, "Balance"]

# Streamlit app starts here
st.set_page_config(page_title="Brands Week Bank", page_icon=":bank:", layout="wide")
st.title("Brands Week Bank")

#logo_url = "https://raw.githubusercontent.com/hanovamx/bat_loc_points/main/logo.png"
#st.image(logo_url, width=200)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        .main {
            background-color: #f0f0f0;
            font-family: 'Roboto', sans-serif;
        }
        .stButton>button {
            color: white;
            background-color: #4CAF50;
        }
        .stTextInput>div>div>input {
            color: blue;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Brands Week Bank</h1>", unsafe_allow_html=True)


# Read the Excel file from the GitHub repository
bank = leer_datos(excel_url)
st.success("Data loaded successfully!")

#st.sidebar.image(logo_url, width=150)
st.sidebar.markdown("<h2 style='color: #4CAF50;'>Brands Week Bank</h2>", unsafe_allow_html=True)
st.sidebar.write("Welcome to the Brands Week Bank app. Use this app to check your points balance.")


# Input for employee number
no_empleado = st.number_input("Enter your employee number:", min_value=1)

if st.button("Check Balance"):
    if validacion(bank, no_empleado):
        balance = mostrar_balance(bank, no_empleado)
        st.write(f"Your balance is: {balance} points")
    else:
        st.error("Invalid employee number, please try again.")
