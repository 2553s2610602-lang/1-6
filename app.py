import streamlit as st
import random

# 제목
st.title("✌️ 가위바위보 게임")

# 선택 목록
choices = ["가위", "바위", "보"]

# 사용자 선택
user = st.radio(
    "하나를 선택하세요",
    choices
)

# 게임 버튼
if st.button("게임 시작"):

    # 컴퓨터 선택
    computer = random.choice(choices)

    st.write(f"🧑 당신: {user}")
    st.write(f"💻 컴퓨터: {computer}")

    # 승패 판정
    if user == computer:
        st.success("🤝 비겼습니다!")

    elif (
        (user == "가위" and computer == "보") or
        (user == "바위" and computer == "가위") or
        (user == "보" and computer == "바위")
    ):
        st.success("🎉 당신이 이겼습니다!")

    else:
        st.error("😢 컴퓨터가 이겼습니다!")
