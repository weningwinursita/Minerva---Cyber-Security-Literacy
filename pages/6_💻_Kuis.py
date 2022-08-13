import streamlit as st
import Frontend.interface as i
import Frontend.animasi_lottie as animasi
from PIL import Image

icon_img = Image.open('Images/icon.png')
st.set_page_config(page_title="Kuis Minerva", page_icon=icon_img)

st.session_state.aktif = False
if not "initialized" in st.session_state:
    st.session_state.aktif = False
    st.session_state.poin = 0
    st.session_state.initialized = True

i.setHeader()


st.header("👨🏻‍💻   Let's Play Quiz    👩🏻‍💻 ")

soal = []
with st.form("form_survey") :
    soal.append(st.radio("1. Serangan dengan menggunakan code berbahaya dengan menyisipkan virus, worm/trojan horse” merupakan pengertian dari ?",["SQL Injection","Malicious Code","Social Engineering","Traffic Flooding"]))
    soal.append(st.radio("2. Berikut ini merupakan kebudayaan zaman batu, kecuali...", ["Paleolitikum", "Mesolitikum", "Neolitikum", "Proto Melayu"]))
    soal.append(st.radio("3. Kepanjanan dari VPN adalah", ["Virtual Private Network", "Virtual Personal Network","Vurnerability Personal Network", "Visual Private Network"]))
    soal.append(st.radio("4. Tokoh Indonesia yang mengukir sejarah dengan terbentuknya ASEAN pada tahun 1967 adalah",["Adam Malik","Soekarno","Moh. Hatta","Soeharto"]))
    soal.append(st.radio("5. Serangan pada keamanan jaringan dengan membanjiri lalu lintas jaringan adalah ...",["Request Flooding", "SQL Injection","Cross Script Server (XSS)","Traffic Flooding"]))
    soal.append(st.radio("6. kebudayaan ngandong adalah ...",["kebudayaan batu","kebudayaan tulang","kebudayaan homoerectus","kebudayaan wajakensis"]))
    soal.append(st.radio("7. siapa yang menjalan kan misi apollo 11 dan gemini 8?",["yuri gagarin","janet shearon","neil armstrong","rakesh sharma"]))
    soal.append(st.radio("8. Bertugas untuk memetakan potensi ancaman keamanan, lalu memberikan rekomendasi untuk mitigasi terhadap potensi ancaman tersebut disebut",["Analisis keamanan","Spesialisasi Forensik", "Cracker","Hacker"]))
    soal.append(st.radio("9. Phobos dan Deimos adalah satelit yang dimiliki planet ....",["Merkurius", "Jupiter","Mars","Saturnus"]))
    soal.append(st.radio("10.Berikut ini merupakan fungsi dari Firewall, Kecuali",["Mengatur dan mengontrol lalu lintas jaringan","Melakukan autentikasi terhadap akses","Melakukan pembuatan virus","Memcatat semua kejadian, dan melaporkan kepada administrator"]))

    poin = 0
    submitted = st.form_submit_button("Submit")
    if submitted :
    
        if soal[0] == "Malicious Code":
            poin = poin+1
        if soal[1] == "Proto Melayu":
            poin = poin+1
        if soal[2] == "Virtual Private Network":
            poin = poin+1
        if soal[3] =="Adam Malik":
            poin = poin+1
        if soal[4] == "Traffic Flooding":
            poin = poin+1
        if soal[5] == "kebudayaan tulang":
            poin = poin+1
        if soal[6] == "neil armstrong":
            poin = poin+1
        if soal[7] == "Analisis keamanan":
            poin = poin+1
        if soal[8] == "Mars":
            poin = poin+1
        if soal[9] == "Melakukan pembuatan virus":
            poin = poin+1   
        
        st.session_state.poin = poin
        st.session_state.aktif = True
        

if st.session_state.aktif:
    st.balloons()

    str = "#### Poinmu :"+str(st.session_state.poin)+"/10"
    col1, col2 =st.columns((1,0.5))
    with col1:
        st.markdown("### Yeaay kamu berhasil menyelesaikan kuis")
        st.markdown(str)
    with col2:
        lottie_finish = animasi.load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_m3ixidnq.json")
        animasi.st_lottie(
            lottie_finish,
            height = 200,
            width = 200,
            key = "Finish Attemp Quiz")
