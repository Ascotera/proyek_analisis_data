import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title('Belajar Analisis Data')
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])
 
with tab1:
    st.header("Code")
    code = """plt.figure(figsize=(5,6))
sns.barplot(
    x='workingday',
    y='cnt',
    data=day)

plt.title('Perbandingan pengguna sepeda saat hari libur dan hari biasa')
plt.xlabel(None)
plt.ylabel('Jumlah Pengguna Sepeda')
plt.show()"""
    st.code(code, language='python')
    st.subheader("Hasil")
    day = pd.read_csv('day.csv')

    fig, ax = plt.subplots(figsize=(5, 6))
    sns.barplot(
        x='workingday',
        y='cnt',
        data=day,
        palette=['#3CB371','#006400'],
        ax=ax
    )
    ax.set_title('Perbandingan pengguna sepeda saat hari libur dan hari biasa')
    ax.set_xlabel(None)
    ax.set_ylabel('Jumlah Pengguna Sepeda')

    st.pyplot(fig)
 
with tab2:
    st.header("Code")
    code = """day.groupby(by='weathersit').agg({
    'cnt': ['max', 'min', 'mean', 'sum']
})"""
    st.code(code, language='python')
    st.subheader("Hasil")
    day = pd.read_csv('day.csv')

    fig, ax = plt.subplots(figsize=(7, 6))
    sns.barplot(
        x='weathersit',
        y='cnt',
        data=day,
        palette=['#006400','#3CB371','#008000'],
        ax=ax
    )
    ax.set_title('Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Pengguna Sepeda')

    st.pyplot(fig)