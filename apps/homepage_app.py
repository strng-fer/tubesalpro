import streamlit as st

def run():
    st.title("Homepage")
    import streamlit as st
    import sqlite3  # Jika menggunakan SQLite
    # Atau
    # from pymongo import MongoClient  # Jika menggunakan MongoDB
    
    # Koneksi ke database
    # Jika menggunakan SQLite
    conn = sqlite3.connect('catatan_memancing.db')
    # Atau
    # client = MongoClient('mongodb://localhost:27017/')
    # db = client['catatan_memancing']
    
    # Fungsi untuk menambahkan catatan baru
    def tambah_catatan(judul, isi):
        conn.execute('INSERT INTO catatan (judul, isi) VALUES (?, ?)', (judul, isi))
        conn.commit()
    
    # Fungsi untuk mengambil semua catatan
    def ambil_semua_catatan():
        cursor = conn.execute('SELECT judul, isi FROM catatan')
        return cursor.fetchall()
    
    # Fungsi untuk menghapus catatan
    def hapus_catatan(judul):
        conn.execute('DELETE FROM catatan WHERE judul = ?', (judul,))
        conn.commit()
    
    # Fungsi untuk mengedit catatan
    def edit_catatan(judul, isi_baru):
        conn.execute('UPDATE catatan SET isi = ? WHERE judul = ?', (isi_baru, judul))
        conn.commit()
      
    def main():
        st.title('Website Catatan Memancing')
    
        # Menu untuk menambahkan catatan baru
        st.header('Tambah Catatan Baru')
        judul_baru = st.text_input('Masukkan Judul Catatan:')
        isi_baru = st.text_area('Masukkan Isi Catatan:')
        if st.button('Tambah'):
            tambah_catatan(judul_baru, isi_baru)
            st.success('Catatan berhasil ditambahkan!')
    
        # Tampilkan daftar catatan
        st.header('Daftar Catatan')
        catatan = ambil_semua_catatan()
        for judul, isi in catatan:
            st.write(f'**{judul}**')
            st.write(isi)
    
            # Tambahkan tombol untuk mengedit dan menghapus catatan
            if st.button(f'Edit {judul}'):
                isi_baru = st.text_area(f'Masukkan Isi Baru untuk {judul}:', value=isi)
                edit_catatan(judul, isi_baru)
                st.success('Catatan berhasil diedit!')
    
            if st.button(f'Hapus {judul}'):
                hapus_catatan(judul)
                st.success('Catatan berhasil dihapus!')
    
    if __name__ == '__main__':
        main()
