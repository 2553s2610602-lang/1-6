import streamlit as st
from streamlit_javascript import st_javascript

# 제목
st.title("🏃 점프 게임")

# 점프 상태 저장
if "jump" not in st.session_state:
    st.session_state.jump = False

# 스페이스바 감지
key = st_javascript("""
document.addEventListener('keydown', function(e) {
    if (e.code === 'Space') {
        window.parent.postMessage("jump", "*");
    }
});
""")

# 점프 처리
if key == "jump":
    st.session_state.jump = True

# 화면 출력
if st.session_state.jump:
    st.markdown(
        "<h1 style='font-size:100px;'>🦘</h1>",
        unsafe_allow_html=True
    )
    st.write("점프 성공!")
    st.session_state.jump = False

else:
    st.markdown(
        "<h1 style='font-size:100px;'>🐤</h1>",
        unsafe_allow_html=True
    )
