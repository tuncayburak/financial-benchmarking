import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Örnek veri çerçevesi (şimdilik demo için)
df = pd.DataFrame({
    "Symbol": ["GARAN.IS", "AKBNK.IS", "YKBNK.IS", "BIMAS.IS"],
    "Sector": ["Bankacılık", "Bankacılık", "Bankacılık", "Perakende"]
})

# Örnek fonksiyonlar (demo için basit versiyonlar)
def compute_metric_trend(symbol, metric="ROE"):
    # Demo amaçlı sahte veri üretelim
    dates = pd.date_range("2022-01-01", periods=4, freq="Y")
    values = [0.15, 0.20, 0.18, 0.17] if metric == "ROE" else [0.10, 0.12, 0.11, 0.09]
    return pd.DataFrame({"Date": dates, metric: values})

def plot_company_vs_sector_trend(symbol, sector, metric="ROE"):
    comp_trend = compute_metric_trend(symbol, metric)
    comp_trend["Type"] = symbol

    sector_trend = compute_metric_trend(sector, metric)
    sector_trend["Type"] = sector + " Ort."

    plot_df = pd.concat([comp_trend, sector_trend])

    plt.figure(figsize=(8,5))
    sns.lineplot(data=plot_df, x="Date", y=metric, hue="Type", marker="o")
    plt.title(f"{symbol} vs {sector} {metric} Trend")
    st.pyplot(plt)

def generate_comment(symbol):
    return f"{symbol} için seçilen metrikte sektör ortalamasına göre karşılaştırma yapılmıştır."

# Streamlit Arayüzü
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


def compute_metric_trend(symbol, metric="ROE"):
    dates = pd.date_range("2022-01-01", periods=5, freq="Y")
    if symbol == "Bankacılık":
        values = [0.10, 0.12, 0.11, 0.09, 0.095]
    else:
        values = [0.11, 0.13, 0.12, 0.10, 0.105]
    return pd.DataFrame({"Date": dates, metric: values})

def plot_company_vs_sector_trend(symbol, sector, metric="ROE"):
    comp_trend = compute_metric_trend(symbol, metric)
    comp_trend["Type"] = symbol

    sector_trend = compute_metric_trend(sector, metric)
    sector_trend["Type"] = sector + " Ort."

    plot_df = pd.concat([comp_trend, sector_trend])

    plt.clf()
    plt.figure(figsize=(8,5))
    sns.lineplot(data=plot_df, x="Date", y=metric, hue="Type", marker="o")
    plt.title(f"{symbol} vs {sector} {metric} Trend")
    st.pyplot(plt)

if comp_trend[metric].dropna().empty:
    st.warning(f"{symbol} için {metric} verisi bulunamadı.")
