import streamlit as st

# 제목 표시
st.title('Hello, Streamlit!')

# 텍스트 입력 받기
name = st.text_input("Enter your name:")

# 버튼 클릭 시 이름 출력
if st.button("Say Hello"):
    st.write(f"Hello, {name}!")