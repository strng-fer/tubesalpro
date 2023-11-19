import streamlit as st
from sqlalchemy import create_engine

# Fungsi untuk menghubungkan ke database SQL
def create_connection():
    username = 'root'
    password = 'FarestaHaerz135'
    host = 'localhost'
    database_name = 'journeymancing123'

    # Buat string koneksi
    connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}/{database_name}"

    # Buat koneksi
    engine = create_engine(connection_string)
    conn = engine.connect()
    return conn

# Fungsi untuk melakukan login
def login(username, password):
    conn = create_connection()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = conn.execute(query)
    return result.fetchone()

# Fungsi untuk tampilan halaman login
def login_page():
    st.title("Journey Mancing")
    st.markdown("## Silakan login untuk melanjutkan")

    username_input = st.text_input("Username")
    password_input = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        user = login(username_input, password_input)
        if user:
            st.success("Login berhasil!")
            # Redirect ke halaman selanjutnya setelah login berhasil
            st.write("Halaman selanjutnya...")
        else:
            st.error("Login gagal. Silakan coba lagi.")

# Tampilan background mancing dengan CSS
st.markdown(
    """
    <style>
    body {
        background-image: url('https://example.com/background-image.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Tampilkan halaman login
login_page()
