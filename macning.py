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
            background: url('https://p4.wallpaperbetter.com/wallpaper/600/885/315/fishing-astronaut-person-fishing-in-crack-area-illustration-wallpaper-preview.jpg?t=1');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Inisialisasi variabel global untuk menyimpan status login
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    if not st.session_state.is_logged_in:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if verify_login(username, password):
                st.success("Login berhasil!")
                st.session_state.is_logged_in = True  # Set status login menjadi True setelah berhasil login
                # Hapus halaman login setelah login berhasil
                st.experimental_rerun()
            else:
                st.error("Username atau password salah")

    if st.session_state.is_logged_in:
        # Tampilkan halaman utama jika sudah login
        st.title("Halaman Utama")
        st.write("Selamat datang di Halaman Utama! Silakan lanjutkan dengan aktivitas Anda di sini.")

if __name__ == "__main__":
    main()
