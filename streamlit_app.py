import pandas as pd

df = pd.DataFrame({
    "Symbol": ["GARAN.IS", "AKBNK.IS", "YKBNK.IS", "BIMAS.IS"],
    "Sector": ["Bankacılık", "Bankacılık", "Bankacılık", "Perakende"]
})

import streamlit as st

st.set_page_config(page_title="Finansal Benchmarking Paneli", layout="wide")

st.title("📊 Finansal Benchmarking Paneli")

# Şirket seçimi
symbol = st.selectbox("Şirket Seçin", df["Symbol"].unique())

# Sektörü otomatik bul
sector = df[df["Symbol"] == symbol]["Sector"].iloc[0]

# Metrik seçimi
metric = st.selectbox("Metrik Seçin", ["ROE", "NetMargin", "DebtEquity"])

# Grafik
st.subheader(f"{symbol} vs {sector} {metric} Trend")
plot_company_vs_sector_trend(symbol, sector, metric)

# Yorum
st.subheader("💬 Otomatik Yorum")
st.write(generate_comment(symbol))
