import streamlit as st

cicilan = st.selectbox("Pilih unit", ["Unit A", "Unit B", "Unit C"])
if cicilan == "Unit A":
    tempo = st.selectbox("Pilih jatuh tempo", ["10 tahun", "15 tahun", "20 tahun"])
    if tempo == "10 tahun":
        st.write("Dp 15% = Rp.600.000.000")
        st.write("Suku bunga fix = 3,5%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = Rp.33.621.195")
    elif tempo == "15 tahun":
        st.write("Dp 15% = Rp.600.000.000")
        st.write("Suku bunga fix = 5%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = Rp.26.886.983")
    elif tempo == "20 tahun":
        st.write("Dp 15% = Rp.600.000.000")
        st.write("Suku bunga fix = 7%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = Rp.26.360.983")
elif cicilan == "Unit B":
    tempo = st.selectbox("Pilih jatuh tempo", ["10 tahun", "15 tahun", "20 tahun"])
    if tempo == "10 tahun":
        st.write("Dp 15% = Rp.375.000.000")
        st.write("Suku bunga fix = 3,5%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = Rp.21.013.247")
    elif tempo == "15 tahun":
        st.write("Dp 15% = Rp.375.000.000")
        st.write("Suku bunga fix = 5%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = Rp.16.804.365")
    elif tempo == "20 tahun":
        st.write("Dp 15% = Rp.375.000.000")
        st.write("Suku bunga fix = 7%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = Rp.16.475.102")
elif cicilan == "Unit C":
    tempo = st.selectbox("Pilih jatuh tempo", ["10 tahun", "15 tahun", "20 tahun"])
    if tempo == "10 tahun":
        st.write("Dp 15% = Rp.225.000.000")
        st.write("Suku bunga fix = 3,5%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = Rp.12.607.948")
    elif tempo == "15 tahun":
        st.write("Dp 15% = Rp.225.000.000")
        st.write("Suku bunga fix = 5%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = Rp.10.082.619")
    elif tempo == "20 tahun":
        st.write("Dp 15% = Rp.225.000.000")
        st.write("Suku bunga fix = 7%")
        st.write("Masa Kredit fix = 5 tahun")
        st.write("Angsuran per bulan = 9.885.061")


    

