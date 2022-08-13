import base64
import streamlit as st
from pathlib import Path

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

#header
header_html = "<img src='data:image/png;base64,{}' style='width: 100%; height: 200px'>".format(
    img_to_bytes("Images/bg.png")
)
def setHeader():
    st.markdown(
        header_html, unsafe_allow_html=True,
    )



def setGif(path_gif):
    gif_html = "<img src='data:image/gif;base64,{}' style='width: 80%; display: block; margin:0 auto;'>".format(
        img_to_bytes(path_gif)
    )
    st.markdown(
        gif_html, unsafe_allow_html=True,
    )

def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-profile'>".format(
      img_to_bytes(img_path)
    )
    return img_html

def setProfileCard(nama, keterangan, domisili, img, email):
    html = '''
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <div class="card"> '''
    html += img_to_html(img)
    html += "<div class='ket'><div class='nama'><b>"+nama+"</b><BR>"  
    link_email="mailto:"+email
    html += "<a href='"+link_email+"'>"+email+"  "+img_to_html("Images/email.png")+"</a></div>"
    html += "<div class='title'>"+ keterangan+"</div><div class='title'>"+domisili+"</div></div>"
    st.markdown(html, unsafe_allow_html=True)

def delete_footer():
    hide_streamlit_sytle = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_sytle, unsafe_allow_html=True)