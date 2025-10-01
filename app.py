import streamlit as st

# """
# linux환경 chromadb - sqlite3 호환성 이슈 대응
# - crewai가 의존하는 chromadb 모듈 로드 전에 pysqlite3 모듈을 로드
# """
# import pysqlite3     # pysqlite3-binary에서 제공하는 모듈
# import sys

# # sqlite3 모듈 이름으로 접근할 때 pysqlite3를 내보내도록 강제
# sys.modules['sqlite3'] = pysqlite3


from crewai import Crew, Process, Task
from agents import coordinator_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from crew import TravelCoordinatorCrew

load_dotenv()



# Streamlit 앱 제목
st.title("🚀 여행 일정 계획 챗봇")

# 사용자 입력을 받는 영역
user_input = st.text_area(
    "여행 계획을 입력해 주세요:",
    "2025년 10월 25일부터 27일까지 인천을 출발해서 오사카로 여행을 다녀오려고 합니다. "
    "항공편, 숙소, 현지 맛집, 가볼만한 곳까지 포함해서 여행 일정을 상세히 만들어주세요. "
    "예산은 총 80만 원 이내로 잡고 있어요. "
    "혼자 가는 여행이라 너무 비싸지 않으면서 가성비 좋은 곳들로 부탁드려요."
)

# 여행 일정 생성 버튼
if st.button("여행 일정 생성하기"):
    with st.spinner("일정을 생성 중입니다..."):

        inputs = {
            'content': user_input
        }

        result = TravelCoordinatorCrew().crew().kickoff(inputs=inputs)


    st.success("여행 일정 생성 완료!")

    # 생성된 일정 결과 출력
    st.markdown("### 📝 생성된 여행 일정:")
    st.markdown(result)
    print(result)
    
    