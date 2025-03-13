# streamlit 실행 방법 : 
## streamlit run 1.st_test.py


# lib 설치 ##########
# pip install openai
# pip install streamlit
# pip install python-dotenv
# 실행 ##############
#  streamlit run 2-2.docent_img_file.py
#####################

import base64
from io import BytesIO
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image  # PIL 라이브러리 필요

# .env 파일 로드
load_dotenv(override=True)

# Open AI API 키 설정
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

# 이미지를 Base64로 변환하는 함수 정의
# Base64 인코딩은 바이너리 데이터를 ASCII 문자열로 변환하는 표준 방식
def encode_image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")  # PNG 형식으로 변환
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# 이미지 해설을 위한 함수 정의
def ai_describe1(image):
    try:
        base64_image = encode_image(image)  # 이미지를 Base64로 변환
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "이 이미지에 대해서 자세하게 설명해 주세요."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
                    ],
                }
            ],
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"오류 발생: {str(e)}"
# URL 해설을 위한 함수 정의
def ai_describe2(image_url):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "이 이미지에 대해서 자세하게 설명해 주세요."},
            {"type": "image_url",
                "image_url": {"url": image_url,},
            },
        ],
        }
    ],
    max_tokens=1024,
    )
    result = response.choices[0].message.content
    print("결과 >> ", result)
    return result

# 탭형식으로 위에서 url을 넣을지 파일을 넣을지 선택할 수 있음 
#1 이미지 url을 넣으면, 이미지 내용에 대해서 AI가 해설을 해줌
## 타이틀 : 똑똑씨 : 이미지를 설명해주는 AI 도슨트
st.title("내 이름은 똑똑씨:sunglasses:")
st.title("이미지를 설명하는:blue[AI 도슨트]에요")
## tab 삽입 : 이미지파일 업로드 / 이미지url 업로드 
tab1, tab2 = st.tabs(["이미지 파일 업로드", "이미지 URL 입력"])

# tab1 : 이미지 업로드 시 화면에 업로드한 이미지 표출
with tab1:
    # st.subheader(":blue[이미지]를 업로드하세요.")
    # streamlit에서 file uploader 찾아서 삽입
    uploaded_file = st.file_uploader(":blue[이미지]를 업로드하세요.", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
    # 업로드된 이미지 표시
        st.image(uploaded_file, width=300)
    
    # 이미지 설명 요청 버튼
        if st.button("해설", key="desc_button_1"):
            image = Image.open(uploaded_file)  # PIL 이미지 열기
        
            # GPT-4V를 이용한 이미지 분석 수행
            result = ai_describe1(image)
            st.success(result)  

    ## 이미지 파일이 없으면 이미지 재요청     
    else : 
        st.write("원하는 그림 파일을 올려주세요.")
  
    
    


with tab2:
    # st.subheader(":blue[이미지 URL]을 업로드하세요.")
    input_URL = st.text_area(":blue[이미지 URL]을 업로드하세요.",height=80)
    if st.button("해설", key="desc_button_2"):

    # st.text_area()의 값이 존재하면 input_url의 값이 True가 되면서 if문 실행
        if input_URL:
            try:
                # st.image()는 기본적으로 이미지 주소로부터 이미지를 웹 사이트 화면에 생성됨
                st.image(input_URL, width=300)

                # describe() 함수는 GPT4V의 출력 결과를 반환함
                result = ai_describe2(input_URL)

                # st.success()는 텍스트를 웹 사이트 화면에 출력하되, 초록색 배경에 출력
                st.success(result)
            except:
                st.error("요청 오류가 발생했습니다!")
        else:
            st.warning("텍스트를 입력하세요!") # 화면 상으로 노란색 배경으로 출력  
    
## 결과 출력 : 
### 1) 업로드한 이미지 
### 2) 이미지에 대한 해설 : 해설(button) / 해설(txt area)

#2 이미지 파일을 업로딩 하면, 이미지에 내용에 대해 AI가 해설을 해줌