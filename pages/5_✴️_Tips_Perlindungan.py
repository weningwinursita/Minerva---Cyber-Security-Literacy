import streamlit as st
import Frontend.interface as i
import Frontend.animasi_lottie as animasi
from PIL import Image

icon_img = Image.open('Images/icon.png')
st.set_page_config(page_title="Tips Perlindungan dengan Cyber Security", page_icon=icon_img)
i.setHeader()


st.header("Cybersecurity untuk Pencegahan dan Perlindungan dari Cyber Crime" )
tab1, tab2 = st.tabs(["🧑 Individu", "🏭 Organisasi"])
with tab1:
    i.setGif("Images/infografis_tips1.gif")
with tab2:
    i.setGif("Images/infografis_tips2.gif")
