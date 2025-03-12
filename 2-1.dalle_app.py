# 1. 사용자에게 보여지는 부분 구현 
import streamlit as st

st.title("지영봇이 그려주는 멋쟁이 그림")
st.title("_jeey_is :blue[cool] :sunglasses:")
st.image("robot_painter.PNG", caption="작업중인 jeey")
st.write("원하는 그림을 말하면 뭐든 다 그려주마!")
import streamlit as st

txt = st.text_area(" ")

st.button("painter")
   



#  - 타이틀 
#  - 이미지표시
#  - 설명 텍스트 출력
#  - 입력 텍스트 area : 영어로(한글로) 그림 요청 설명 입력 
#  - button : openai에 그림 요청 버튼
# 
# 2. 버튼 클릭 시, 사용자 이벤트 
#  - gpt로부터 받은 이미지를 화면에 출력