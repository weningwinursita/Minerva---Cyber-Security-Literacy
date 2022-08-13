import json
import requests

import streamlit as st
from streamlit_lottie import st_lottie #ini harus diinstal pip install streamlit-lottie dulu

#memuat animasi lottie dari file folder
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f :
        return json.load(f)

#memuat animasi langsung dari webnya
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()