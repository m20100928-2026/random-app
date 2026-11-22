import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍱")

# 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 눌러 오늘 먹을 맛있는 점심 메뉴를 뽑아보세요!")

# 점심 메뉴 리스트
menus = [
    "김치찌개",
    "된장찌개",
    "돈가스",
    "제육볶음",
    "짜장면",
    "짬뽕",
    "초밥",
    "국밥",
    "비빔밥",
    "칼국수",
    "햄버거",
    "파스타",
    "쌀국수",
    "마라탕",
    "떡볶이",
]

# 버튼 클릭 시 랜덤 메뉴 출력
if st.button("🎲 오늘의 메뉴 뽑기!", type="primary"):
    selected_menu = random.choice(menus)
    st.balloons()  # 축하 풍선 효과
    st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}**입니다! 맛있게 드세요! 😋")
