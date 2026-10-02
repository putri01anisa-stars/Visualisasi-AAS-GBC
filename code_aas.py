from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Analisis Gangguan Ca pada AAS", layout="wide")
html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=780, scrolling=False)
