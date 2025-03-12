# 1. 사용자에게 보여지는 부분 구현 
import os
import streamlit as st
from dotenv import load_dotenv
import openai

# openai key값 로딩, 환경변수 .env에 저장, git에 업로딩은 안되도록
# .env 파일 로드
load_dotenv()

# 환경변수에서 API Key 가져오기
openai_api_key = os.getenv("OPENAI_API_KEY")

# openai값 프린트 해보기 
# print(f"OpenAI API Key: {openai_api_key}")

#openai 객체 생성 
client = openai.OpenAI(api_key=openai_api_key)

# openai에 이미지 생성 요청 함수 정의 
def get_image(input_txt):
     response = client.images.generate(
         model="dall-e-3",
         prompt=input_txt,
         size = "1024x1024",
         quality="standard",
         n=1,
     )
     image_url=response.data[0].url
     # print(image_url)
     return(image_url)  # 리턴값이 생성 url

##  - 타이틀 
st.title("지영봇이 그려주는 멋쟁이 그림")
st.header("jeey is :blue[cool] :sunglasses:",divider=True)

##  - 이미지표시
st.image("robot_painter.PNG", caption="작업중인 jeey")

##  - 설명 텍스트 출력
st.subheader("원하는 그림을 말하면 뭐든 다 그려주마!")

## - 입력 텍스트 area : 영어로(한글로) 그림 요청 설명 입력 
input_txt = st.text_area("하단에 영어로 입력하렴",height=200)
##  - button : openai에 그림 요청 버튼
# st.button("painting")
# 2. 버튼 클릭 시, 사용자 이벤트 
#  - gpt로부터 받은 이미지를 화면에 출력
if st.button("painting") :
    #txt area 박스에 입력한 값이 있는지 체크 
    if input_txt : 
        # print("프롬프트값",input_txt)
        # openai에 그림요청 메세지 전송 
        image_url = get_image(input_txt)
        st.image(image_url,caption="지영봇의 작품")
    else : 
        # 원하는 그림을 설명해봐. 
        st.write("원하는 그림을 설명해봐.")  


