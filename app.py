import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Тестовый отчёт", layout="wide")

st.title("📊 Тестовый отчёт Streamlit")
st.write("Это пример приложения для загрузки и визуализации Excel-файла.")

# Загрузка файла
uploaded_file = st.file_uploader("Загрузите Excel-файл", type=["xlsx", "xls"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("📋 Предварительный просмотр данных")
    st.dataframe(df)

    if not df.empty:
        st.subheader("📈 График по первому числовому столбцу")
        numeric_cols = df.select_dtypes(include=['int', 'float']).columns
        if len(numeric_cols) > 0:
            st.line_chart(df[numeric_cols[0]])
        else:
            st.warning("Нет числовых данных для отображения графика.")
else:
    st.info("Пожалуйста, загрузите Excel-файл для начала.")
