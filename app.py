import streamlit as st
import pandas as pd
import requests
from datetime import datetime


# URL of the Excel file in the GitHub repository
excel_url = 'https://github.com/hanovamx/bat_loc_points/raw/main/Brands%20Week%20Bank.xlsx'

def leer_datos(url):
    return pd.read_excel(url, sheet_name="Bank", index_col="Pers.No.", engine='openpyxl')

def validacion(bank, no_empleado):
    return no_empleado in bank.index

def mostrar_balance(bank, no_empleado):
    return bank.loc[no_empleado, "Balance"]

def get_github_file_last_modified(repo_owner, repo_name, file_path):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits?path={file_path}"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        if commits:
            last_commit = commits[0]
            last_modified_date = last_commit['commit']['committer']['date']
            return datetime.strptime(last_modified_date, "%Y-%m-%dT%H:%M:%SZ")
    return None

# Streamlit app starts here
st.set_page_config(page_title="Brands Week Bank", page_icon=":bank:", layout="wide")
#st.title("Brands Week Bank")

logo_url = "https://github.com/hanovamx/bat_loc_points/blob/main/brandsweek_logo.png"
st.image(logo_url, width=200)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        .main {
            background-color: #f0f0f0;
            font-family: 'Roboto', sans-serif;
        }
        .stButton>button {
            color: white;
            background-color: #E72582;
        }
        .stTextInput>div>div>input {
            color: blue;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #E72582;'>Brands Week Bank</h1>", unsafe_allow_html=True)


# Read the Excel file from the GitHub repository
bank = leer_datos(excel_url)
#st.success("Data loaded successfully!")

repo_owner = 'hanovamx'
repo_name = 'bat_loc_points'
file_path = 'Brands%20Week%20Bank.xlsx'
last_modified_date = get_github_file_last_modified(repo_owner, repo_name, file_path)
if last_modified_date:
    st.write(f"Last updated: {last_modified_date.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.write("Last updated: End of yesterday")

st.sidebar.image(logo_url, width=150)
st.sidebar.markdown("<h2 style='color: #E72582;'>Brands Week Bank</h2>", unsafe_allow_html=True)
st.sidebar.write("Welcome to the Brands Week Bank app. Use this app to check your coins balance.")


# Input for employee number
no_empleado = st.number_input("Enter your employee number:", min_value=1)

if st.button("Check Balance"):
    if validacion(bank, no_empleado):
        balance = mostrar_balance(bank, no_empleado)
        st.write("Welcome "+ str(bank.loc[no_empleado, "Name"]) + ", ")
        st.write(f"Your balance is: {balance} coins")
    else:
        st.error("Invalid employee number, please try again or reach out to Karla Gomez.")
