from cmath import pi
import streamlit as st
import Frontend.interface as i
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
from PIL import Image

icon_img = Image.open('Images/icon.png')
st.set_page_config(page_title="Survei", page_icon=icon_img)

if not "initialized" in st.session_state:
    st.session_state.pilihChart = 0
    st.session_state.initialized = True

i.setHeader()

st.header("Survey mengenai Cyber Security")

soal = []
pie_survey = []
label_pie = []
pilihan_display = ("Mengetahui cyber security","Pernah mengalami cyber crime","Mengetahui cara melindungi password","Selalu berhati-hati dengan iklan yang muncul", "Urgensi cyber security")
pilihan = list(range(len(pilihan_display))) 
def sessChart() :
    st.session_state.pilihChart

with st.form("form_survey") :
    soal.append(st.radio("1. Apakah anda mengetahui mengenai cyber security?",["Ya","Tidak"]))
    soal.append(st.radio("2. Apakah anda pernah mengalami kejadian cyber crime?", ["Ya", "Tidak"]))
    soal.append(st.radio("3. Apakah anda tahu cara pengamanan dalam membuat password agar tidak di hack?", ["Ya", "Tidak"]))
    soal.append(st.radio("4. Apakah anda selalu berhati-hati ketika akan mengklik tautan website?" , ["Ya", "Tidak"]))
    soal.append(st.radio("5. Di era revolusi industri 4.0 dan society 5.0, apakah kesadaran akan cyber security perlu ditingkatkan?",["Ya", "Tidak"]))

    submitted = st.form_submit_button("Submit")
    if submitted :
        poin = 0
        data_survey = {}
        ya = []
        tidak =[]

        for i in range(len(soal)):
            if soal[i] == 'Ya' :
                
                if Path("data_survey.csv").is_file() :
                    file_data_survey = pd.read_csv("data_survey.csv")

                    #update data
                    ya.append(file_data_survey.loc[i,"Ya"] + 1)
                    tidak.append(file_data_survey.loc[i,"Tidak"])
                    
                else :
                    ya.append(1)
                    tidak.append(0)
                    
                if i==1 :
                    continue
                else:
                    poin = poin+1
            else :
                if Path("data_survey.csv").is_file() :
                    file_data_survey = pd.read_csv("data_survey.csv")
                    
                    #update data
                    ya.append(file_data_survey.loc[i,"Ya"])
                    tidak.append(file_data_survey.loc[i,"Tidak"] + 1)
                else :
                    ya.append(0)
                    tidak.append(1)
                    
                poin = poin+0

        if poin == 4 :
            msg ="🥳🥳 Yeay, anda sudah memahami tentang Cyber Security!."
        else :
            msg ="😢😢 Maaf, anda belum paham mengenai cyber security."
        msg += "\n\nUntuk menambah wawasan cyber security anda dapat mengklik link konten yang tersedia pada website ini "
        link = "<h3>Daftar Konten Literasi Cyber Security Minerva</h3>"
        link += "\n\n[1. Sejarah Perkembangan Cyber Security](%EF%B8%8F_Sejarah_Perkembangan)\n\n[2. Adware, Program Penampil Iklan yang Mengganggu](%EF%B8%8F_Adware)\n\n[3. BAHAYA! Berbagi Pasword dengan Orang Lain](%EF%B8%8F_Bahaya_Berbagi_Password)\n\n[4. Cybersecurity untuk Pencegahan dan Perlindungan dari Cyber Crime](%EF%B8%8F_Tips_Perlindungan)"
        with st.container():
            st.info(msg)
            st.markdown(link, unsafe_allow_html=True)
        data_survey = {"Ya" : ya, "Tidak" : tidak}
        df_survey = pd.DataFrame(data_survey)
        df_survey.to_csv("data_survey.csv")

survey = st.selectbox("Lihat hasil survey", pilihan, key="pilihChart", format_func=lambda x: pilihan_display[x], on_change=sessChart)

file_data_survey = pd.read_csv("data_survey.csv", index_col='Unnamed: 0')

if st.session_state.pilihChart == 0 :
    pie_survey = file_data_survey.loc[0]
    label_pie= ["Mengetahui cyber security","Belum mengetahui cyber security"]
elif st.session_state.pilihChart == 1 :
    pie_survey  = file_data_survey.loc[1]
    label_pie= ["Pernah","Belum pernah"]
elif st.session_state.pilihChart == 2 :
    pie_survey  = file_data_survey.loc[2]
    label_pie= ["Tahu","Tidak tahu"]
elif st.session_state.pilihChart == 3 :
    pie_survey  = file_data_survey.loc[3]
    label_pie= ["Ya","Tidak"]
else :
    pie_survey  = file_data_survey.loc[4]
    label_pie= ["Perlu","Tidak perlu"]

c1,c2,c3 = st.columns((1,2,1))
with c2:
    fig = plt.figure(figsize=(2, 2))
    plt.pie(pie_survey , labels = label_pie,  autopct='%1.1f%%', textprops={'fontsize': 6})
    st.pyplot(fig)
