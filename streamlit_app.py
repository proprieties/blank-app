import yfinance as yf
import streamlit as st
import pandas as pd

# Streamlit 제목
st.title("VIX 지수 시각화")

# 데이터 가져오기
@st.cache_data
def get_vix_data():
    try:
        vix = yf.Ticker("^VIX")  # VIX 지수의 티커 심볼
        hist = vix.history(period="1y")  # 지난 1년간의 데이터 가져오기
        if hist.empty:
            st.error("VIX 데이터를 가져오지 못했습니다. 다시 시도해주세요.")
        return hist
    except Exception as e:
        st.error(f"데이터를 가져오는 중 오류가 발생했습니다: {e}")
        return pd.DataFrame()

# VIX 데이터 로드
vix_data = get_vix_data()

# 데이터프레임 표시
if not vix_data.empty:
    st.subheader("VIX 지수 데이터")
    st.write(vix_data)

    # 그래프 표시
    st.subheader("VIX 지수 그래프")
    st.line_chart(vix_data["Close"])
else:
    st.warning("표시할 데이터가 없습니다.")