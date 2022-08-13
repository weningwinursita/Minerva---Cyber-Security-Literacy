import streamlit as st
import Frontend.interface as i
import Frontend.animasi_lottie as animasi
from PIL import Image
from typing import List

icon_img = Image.open('Images/icon.png')
st.set_page_config(page_title="Welcome to Minerva", page_icon=icon_img)

lottie_hello = animasi.load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3vbOcw.json")
i.setHeader()

# Generate Three equal columns
c1,c2 = st.columns((3, 1))
with c1 :
    st.title("Welcome to Our Website!")
    st.write("Halo kami dari kelompok 10 kelas A Women in Tech 'Minerva' membuat sebuah website menggunakan streamlit untuk literasi dan pembelajaran mengenai cyber security. Selamat mengeksplorasi!")
    
with c2 :
    animasi.st_lottie(
        lottie_hello,
        height = 250,
        width = 250,
        key = "hello animation")


st.subheader("Nama Kelompok 10 : Minerva")
st.write("Minerva adalah salah satu dewi utama yang dipuja oleh bangsa Romawi Pagan dan merupakan dewi dari Mitologi Romawi. Minerva dipuja sebagai seorang dewi perang, kebijaksanaan, ilmu pengetahuan, seni kriya, puisi, obat-obatan, pelindung para pengrajin dan penemu alat musik.")
st.write("Dengan nama Minerva, sebagai dewi kebijaksanaan dan ilmu pengetahuan, kami berharap website yang kami buat dapat menambah wawasan dan kesadaran kepada pembaca akan pentingnya cyber security")

x1,x2, x3 = st.columns((1,1,1))
with x2:

    st.image("https://media.giphy.com/media/3o7bubzc43GQ3pQB7G/giphy.gif")

st.subheader("Anggota :")

image_arin = Image.open('Images/arin.png')
image_vivia = Image.open('Images/vivia.png')
image_wening = Image.open('Images/wening.png')

x1,x2, x3 = st.columns((1,1,1))
with x1 :
    i.setProfileCard("Arin Tsamrotul Fitriyah","Ibu Rumah Tangga","Samarinda", "Images/arin.png","arinfitria843@gmail.com")
with x2:
    
    i.setProfileCard("Vivia Afrilia Ningrum","Karyawan Swasta","DKI Jakarta", "Images/vivia.png", "viviaa801@gmail.com")
with x3:

    i.setProfileCard("Wening Winursita","Mahasiswi","Cimahi", "Images/wening.png","weningwinursita@upi.edu")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
