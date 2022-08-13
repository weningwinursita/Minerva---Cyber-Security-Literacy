import streamlit as st
import Frontend.interface as i
from PIL import Image

icon_img = Image.open('Images/icon.png')
st.set_page_config(page_title="Bahaya Berbagi Password dengan Orang Lain", page_icon=icon_img)
i.setHeader()


st.header("BAHAYA! Berbagi Pasword dengan Orang Lain" )
c1, c2,c3 = st.columns((1,3 , 1))
with c2:
    st.image("https://media.giphy.com/media/FtLZ05FBnC48uYGzuO/giphy.gif")


st.write("Password adalah hal penting yang harus dimiliki oleh setiap orang jika ingin membuat media sosial, blog, email, dan lain sebagainya. Adanya password dibutuhkan untuk menjaga keamanan agar akun tersebut terhindar dari tindakan-tindakan oknum yang tidak bertanggungjawab.")
st.write("Salah satu fungsi password adalah untuk meningkatkan keamanan dari file, aplikasi, serta jaringan yang ingin dilindungi. Password sangat penting sekali dijaga kemanannya. Salah satu caranya adalah dengan tidak membagikannya atau memberitahukannya kepada orang lain ")
st.write("Membagikan password kepada orang lain tentunya sangat membahayakan. Berikut bahayanya:")    

st.image("Images/infografis_password.png")
