import streamlit as st
import Frontend.interface as i
from PIL import Image

icon_img = Image.open('Images/icon.png')
st.set_page_config(page_title="Adware", page_icon=icon_img)

i.setHeader()
st.header("Adware, program penampil iklan yang mengganggu")
st.write("Seringkali, ketika kita sedang browsing di internet atau bermain game online, kita menjumpai iklan-iklan yang mengganggu. Iklan-iklan itu muncul dari program yang bernama Adware. Namun penggunaan adware dapat membuat kinerja komputer menjadi lambat. Hal ini karena adware menggunakan RAM cukup banyak dan juga siklus CPU. Selain itu, penggunaan adware juga akan berdampak pada menurunnya kecepatan internet karena perangkat lunak ini membutuhkan bandwidth yang besar dan stabil untuk bisa menjalankan tugasnya dengan baik. Bahkan penggunaan adware malah membuat sistem komputer menjadi tidak stabil sehingga rentan terhadap berbagai permasalahan yang dapat merugikan")

i.setGif("Images/popups.gif")

st.write("Ketika adware ditanamkan dalam sebuah program aplikasi atau website.  aplikasi tersebut akan mengirimkan sinyal ke server pengontrol adware. Setelah adware terpasang, orang di balik panggung yang mengontrol server tersebut bisa melakukan hal-hal yang tidak diinginkan ke ponsel pengguna. Misalnya, memaksa pengguna untuk membuka link situs adware/phishing atau penipuan di peramban ponsel serta mengalihkan (redirect) pengguna ke Play Store untuk membuka aplikasi berbahaya yang telah diatur oleh pelaku yang menanam adware itu. Aplikasi yang disusupi adware juga bisa mengunduh dan memasang aplikasi \"remote\" lainnya, yakni aplikasi berbahaya untuk mengendalikan smartphone pengguna dari jauh tanpa diketahui.")
st.write("Yuk ketahui cara mencegah dan mengatasi adware melalui inforgafis dibawah ini!")

i.setGif("Images/infografis_adware.gif")
