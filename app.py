import streamlit as st
import random

# 제목
st.title("🎮 숫자 맞추기 게임")

# 랜덤 숫자 저장
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)

# 입력창
guess = st.number_input(
    "1부터 10 사이 숫자를 맞춰보세요",
    min_value=1,
    max_value=10,
    step=1
)

# 버튼
if st.button("확인"):

    if guess == st.session_state.number:
        st.success("🎉 정답입니다!")

    else:
        st.error("❌ 틀렸습니다!")

# 다시 시작 버튼
if st.button("새 게임"):
    st.session_state.number = random.randint(1, 10)
    st.success("새 숫자가 생성되었습니다!")
