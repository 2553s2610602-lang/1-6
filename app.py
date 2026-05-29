import streamlit as st

# 제목
st.title("💌 연애 코칭 앱")

# 설명
st.write("현재 고민을 선택하면 간단한 연애 조언을 제공합니다.")

# 고민 선택
problem = st.selectbox(
    "어떤 고민이 있나요?",
    [
        "썸",
        "연락 문제",
        "고백",
        "이별",
        "재회",
    ]
)

# 버튼
if st.button("조언 받기"):

    if problem == "썸":
        st.success("상대에게 부담 주지 말고 자연스럽게 대화를 이어가세요.")

    elif problem == "연락 문제":
        st.success("답장이 늦다고 조급해하지 말고 여유를 가지세요.")

    elif problem == "고백":
        st.success("완벽한 타이밍보다 솔직한 마음이 더 중요합니다.")

    elif problem == "이별":
        st.success("억지로 잊으려 하지 말고 충분히 감정을 정리하세요.")

    elif problem == "재회":
        st.success("다시 만나기 전에 왜 헤어졌는지 먼저 돌아보세요.")
