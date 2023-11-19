import streamlit as st
import requests

# Fungsi untuk verifikasi login
def verify_login(username, password):
    # Ganti URL dengan URL file txt di GitHub yang berisi username dan password
    url = 'https://raw.githubusercontent.com/strng-fer/tubesalpro/main/user.txt'
    response = requests.get(url)
    credentials = response.text.split('\n')
    
    for cred in credentials:
        if ',' in cred:
            stored_username, stored_password = cred.split(',')
            if username == stored_username and password == stored_password:
                return True
    
    return False

def main():
    st.title("Journey Mancing")
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url('https://p4.wallpaperbetter.com/wallpaper/600/885/315/fishing-astronaut-person-fishing-in-crack-area-illustration-wallpaper-preview.jpg');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input username dan password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if verify_login(username, password):
            st.success("Login berhasil!")
            # Lanjutkan ke halaman berikutnya di sini
        else:
            st.error("Username atau password salah")

if __name__ == "__main__":
    main()
