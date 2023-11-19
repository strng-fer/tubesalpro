import streamlit as st
import mysql.connector

# Koneksi ke database SQL
username = 'root'
password = 'FarestaHaerz135'
host = 'localhost'
database_name = 'journeymancing123'

try:
    connection = mysql.connector.connect(
        user=username, password=password, host=host, database=database_name
    )
    cursor = connection.cursor()
    st.sidebar.title("Journey Mancing")
    st.sidebar.image('background_image.jpg', caption='Background Mancing', use_column_width=True)
    
    # Halaman Login
    st.title("Login")
    username_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")

    if st.button("Login"):
        # Query untuk memeriksa apakah username dan password ada di database
        query = "SELECT * FROM user WHERE username = %s AND password = %s"
        cursor.execute(query, (username_input, password_input))
        result = cursor.fetchone()

        if result:
            st.success("Login berhasil!")
            # Lanjutkan ke halaman berikutnya setelah berhasil login
            # Tambahkan kode untuk halaman berikutnya di sini
        else:
            st.error("Username atau password salah")
            
except mysql.connector.Error as e:
    st.error(f"Gagal terhubung ke database: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
