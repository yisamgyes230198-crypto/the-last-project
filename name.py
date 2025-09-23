import streamlit as st

st.title("나의 첫 웹 서비스 만들기")
name = st.text_input("이름을 입력해주세요. : ")
menu = st.selectbox("rkwkd aksgdl Tmsms doqdl anjdi?", ["dbxbqm", "dlstmxkrmfoa", "x"])
time = st.slider("gkfn tkdydtlrksdms?", 0,12,3)
if st.button('elwlxjf skdml tmqrhks'):
    st.write(f'{name}di {menu}fmf {time}tlrksehddks tkdydgksmsrnsk')
