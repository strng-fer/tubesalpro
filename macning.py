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

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if verify_login(username, password):
            st.success("Login berhasil!")
            return True  # Kembalikan True jika login berhasil
        else:
            st.error("Username atau password salah")
    
    return False  # Kembalikan False jika login gagal

def main_page():
    st.title("Halaman Utama")
    st.write("Selamat datang di Halaman Utama! Silakan lanjutkan dengan aktivitas Anda di sini.")

def main():
    if not login_page():
        return
    
    main_page()

if __name__ == "__main__":
    main()
