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

# Fungsi untuk menambahkan catatan
def add_note():
    st.title("Tambah Catatan Mancing")
    
    # Memasukkan foto
    uploaded_file = st.file_uploader("Unggah Foto", type=['jpg', 'png'])

    # Memasukkan detail lokasi
    location_details = st.text_input("Detail Lokasi")

    # Memasukkan lokasi pada map untuk mendapatkan latitude dan longitude
    gmaps_api_key = "YOUR_GOOGLE_MAPS_API_KEY"  # Ganti dengan API key Google Maps
    gmaps = googlemaps.Client(key=gmaps_api_key)
    location = st.text_input("Cari Lokasi")
    if location:
        result = gmaps.geocode(location)
        if result:
            latitude = result[0]['geometry']['location']['lat']
            longitude = result[0]['geometry']['location']['lng']
            st.write("Latitude:", latitude, "Longitude:", longitude)

    # Memasukkan tanggal dan waktu
    date_time = st.date_input("Tanggal") + st.time_input("Waktu")

    # Memasukkan jenis ikan yang ditangkap
    fish_type = st.text_input("Jenis Ikan yang Ditangkap")

    # Memasukkan metode memancing
    fishing_method = st.text_input("Metode Memancing")

    # Tombol untuk menyimpan catatan memancing
    if st.button("Simpan Catatan"):
        # Simpan catatan memancing ke database atau file
        st.success("Catatan Mancing Disimpan")

        # Mendapatkan info cuaca
        weather_info = get_weather_info(latitude, longitude)
        st.subheader("Info Cuaca")
        st.write(f"Temperatur: {weather_info['temperature']}")
        st.write(f"Kondisi Cuaca: {weather_info['condition']}")
        st.write(f"Kecepatan Angin: {weather_info['wind_speed']}")


# Fungsi untuk mengedit catatan
def edit_note():
    st.title("Edit Catatan")
    # Implementasikan logika untuk mengedit catatan di sini

# Fungsi untuk menghapus catatan
def delete_note():
    st.title("Hapus Catatan")
    # Implementasikan logika untuk menghapus catatan di sini

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
    option = st.selectbox("Pilih Operasi", ["Tambah Catatan", "Edit Catatan", "Hapus Catatan"])

    if option == "Tambah Catatan":
        add_note()
    elif option == "Edit Catatan":
        edit_note()
    elif option == "Hapus Catatan":
        delete_note()

def main():
    if not login_page():
        return
    
    main_page()

if __name__ == "__main__":
    main()
