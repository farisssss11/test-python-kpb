import streamlit as st

st.title("Ini aplikasi pertamaku")
st.header("programmer banyuwangi")
nama = st.text_input("Masukan nama anda")
if not nama:
    st.stop()
st.markdown(f'Selamat <b>Datang</b> {nama}', unsafe_allow_html=True)