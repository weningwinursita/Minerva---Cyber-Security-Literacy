import streamlit as st
import Frontend.interface as i
import Frontend.animasi_lottie as animasi
from PIL import Image

icon_img = Image.open('Images/icon.png')
st.set_page_config(page_title="Sejarah Perkembangan Cyber Security", page_icon=icon_img)

i.setHeader()
st.header("Sejarah dan Perkembangan Cybersecurity")

lottie_cs = animasi.load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0os5xmbh.json")
animasi.st_lottie(
    lottie_cs,
    key = "Privacy")

tab1, tab2 = st.tabs(["⌛️ Sejarah Cyber Security", "💥 Macam-macam Cyber Crime"])

with tab1:
    st.write("Abad ke 21 saat ini memasuki masa revolusi industry 4.0 dan society 5.0 yang ditandai makin dengan gencarnya penggunaan teknologi terutama pengimplementasian Internet of Things yang dapat membantu pekerjaan manusia dengan mengintegrasikan ruang fisik dan maya menggunakan internet. Dengan adanya Internet of Things membuat manusia selalu terhubung dengan jaringan internet pada ruang siber.")
    st.write("Ditengah ruang maya penggunannya dapat menerima keuntungan atau bahkan kerugian. Pengguna internet memiliki ancaman terhadap Tindakan criminal diruang maya atau yang sering disebut cybercriminal. Untuk mencegah dan menghindari potensi terdampak cybercriminal, maka perlunya adanya kesadaran terhadap cybersecurity")
    st.write("Cybersecurity atau keamanan siber merupakan suatu mekanisme untuk melindungi computer, perangkat mobile, server, jaringan dan perangkat elektronik dari serangan jahat yang dapat merusak sistem atau menghilangkan data. Keamanan siber berkembang seiring dengan munculnya teknologi jaringan internet. Berikut merupakan perkembangan keamanan siber dari waktu ke waktu.")

    i.setGif("Images/infografis_sejarah.gif")

with tab2:
    with st.container():
        with st.expander("Pishing"):
            c1,c2 = st.columns((1, 0.5))
            with c1:
                st.write("Phising adalah contoh cyber crime yang bertujuan untuk mencuri informasi dan data pribadi dari email, telepon, pesan teks atau link palsu yang mengaku sebagai instansi atau pihak-pihak tertentu. Cara kerja phishing yaitu mengelabui target dengan tipuan yang seolah terlihat normal padahal mereka tidak sadar bahwa data pribadi miliknya sedang dicuri")
            with c2:
                img = Image.open("Images/phishing.png")
                st.image(img,"Pishing",use_column_width=True)
        with st.expander("Sniffing"):
            c1,c2 = st.columns((1, 0.5))
            with c1:
                st.write("Sniffing adalah tindak kejahatan penyadapan yang dilakukan menggunakan jaringan internet dengan tujuan utama untuk mengambil data dan informasi sensitive secara illegal. Cara kerja sniffing adalah ketika Anda terhubung ke jaringan yang bersifat public, saat Anda melakukan proses transfer data dari client server dan sebaliknya. Karena data yang mengalir pada client dan server yang bersifat bolak-balik, sniffing ini akan menangkap paket-paket yang dikirimkan dengan cara illegal menggunakan tools pembantu.")
            with c2:
                img = Image.open("Images/sniffing.png")
                st.text('')
                st.text('')
                st.image(img, "Sniffing", use_column_width=True)
        with st.expander("Cracking"):
            c1, c2 = st.columns((1,0.5))
            with c1 :
                st.write("Cracking adalah percobaan memasuki sistem komputer secara paksa dengan meretas sistem keamanan software atau komputer untuk tujuan ilegal yang mengarah ke kriminalisme. Pelaku cracking melakukan aksinya untuk mencuri, melihat, memanipulasi data hingga penanaman malware. Ada berbagai jenis cracking yang sering terjadi, misalnya password cracking, software cracking, dan network cracking.")
            with c2:
                st.text('')
                img = Image.open("Images/cracking.jpg")
                st.image(img, "Cracking", use_column_width=True)
        with st.expander("SQL Injection"):
            c1, c2 = st.columns((1,0.5))
            with c1:
                st.write("SQL injection adalah teknik penyalahgunaan celah keamanan pada lapisan database sebuah aplikasi. Hal ini umumnya terjadi akibat pengembang aplikasi tidak mengimplementasikan filter terhadap beberapa metakarakter yang digunakan dalam sintaks SQL, sehingga penyerang dapat menginput metakarakter tersebut menjadi instruksi pada aplikasi untuk mengakses database. Serangan SQL juga dapat terjadi jika backend tidak melakukan setting Web Application Firewall (WAF) atau Intrusion Prevention System (IPS) di arsitektur jaringan dengan baik, sehingga database bisa diakses langsung dari celah kerawanan yang ditemukan.")
            with c2:
                st.text('')
                st.text('')
                st.text('')
                img = Image.open("Images/sql.jpg")
                st.image(img, caption="SQL Injection")
        with st.expander("DDos"):
            img = Image.open("Images/DDoS.jpg")
            st.image(img,width=600, caption="Serangan DDoS")
            st.write("Secara sederhana DDoS attack dapat diartikan serangan yang dilakukan dengan membanjiri lalu lintas jaringan dengan banyak data. DDoS dibagi menjadi 3 tipe penggunaan, yakni sebagai berikut :")
            st.markdown('''
                1. Request flooding merupakan teknik yang digunakan dengan membanjiri jaringan  menggunakan banyak request. Akibatnya, pengguna lain yang terdaftar tidak dapat dilayani.
                1. Traffic flooding merupaka teknik yang digunakan dengan membanjiri lalu lintas jaringan dengan banyak data. Akibatnya, pengguna lain tidak bisa dilayani.
                1. Mengubah sistem konfigurasi atau bahkan merusak komponen dan server juga termasuk tipe denial of service, tetapi cara ini tidak banyak digunakan karena cukup sulit untuk dilakukan.
            ''')
            
                
        with st.expander("Malware dan Malicious Code"):
            c1, c2 = st.columns((1,0.5))
            with c1:
                st.write("Malware adalah perangkat lunak yang diciptakan untuk menyusup atau merusak sistem komputer, server atau jejaring komputer tanpa izin (informed consent) dari pemilik. Malware bisa menyebabkan kerusakan pada sistem komputer dan memungkinkan juga terjadi pencurian data / informasi. Hal yang pada umumnya menjadi penyebab malware adalah mengunduh perangkat lunak (software) ilegal yang mungkin disisipkan sebuah malware. Terdapat beberapa jenis Malware seperti virus, worm, trojan horse, sebagian besar rootkit, spyware, adware (infected), serta software-software lain yang berbahaya dan tidak diinginkan oleh pengguna perangkat komputer.")
            with c2:
                st.text('')
                st.text('')
                st.text('')
                img = Image.open("Images/malware.png")
                st.image(img, caption="Jenis Malware")
