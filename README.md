# 🚀 CrewAI 기반 AI 여행 일정 플래너

> 다중 AI 에이전트를 활용한 지능형 여행 일정 자동 생성 시스템

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.114.0-green.svg)](https://github.com/joaomdmoura/crewAI)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.44.1-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📋 목차

- [프로젝트 소개](#-프로젝트-소개)
- [주요 기능](#-주요-기능)
- [시스템 아키텍처](#-시스템-아키텍처)
- [기술 스택](#-기술-스택)
- [프로젝트 구조](#-프로젝트-구조)
- [설치 및 환경 설정](#-설치-및-환경-설정)
- [사용 방법](#-사용-방법)
- [API 통합](#-api-통합)
- [에이전트 구조](#-에이전트-구조)
- [개발 가이드](#-개발-가이드)
- [문제 해결](#-문제-해결)
- [기여 방법](#-기여-방법)
- [라이선스](#-라이선스)

---

## 🎯 프로젝트 소개

**CrewAI 여행 일정 플래너**는 다중 AI 에이전트 시스템을 활용하여 사용자의 여행 요구사항을 자동으로 분석하고, 항공편, 숙소, 현지 맛집 및 관광지 정보를 통합하여 완벽한 여행 일정을 생성하는 지능형 여행 계획 도구입니다.

### ✨ 왜 이 프로젝트인가?

- **🤖 다중 에이전트 협업**: 3명의 전문 AI 에이전트가 각자의 역할을 수행하며 협력
- **🌐 실시간 API 통합**: Amadeus, Google Places, ExchangeRate API를 통한 실제 데이터 활용
- **💡 지능형 일정 생성**: LLM 기반 자연어 처리로 사용자 요구사항 정확히 이해
- **💰 예산 최적화**: 환율을 고려한 예산 계산 및 가성비 추천
- **🎨 직관적 UI**: Streamlit 기반 웹 인터페이스로 손쉬운 사용

---

## 🎁 주요 기능

### 1️⃣ 항공편 및 숙소 검색
- ✈️ Amadeus API를 통한 실시간 항공편 조회
- 🏨 다양한 숙박 옵션 검색 및 가격 비교
- 💱 다중 통화 지원 및 환율 자동 변환

### 2️⃣ 현지 정보 추천
- 🍜 Google Places API를 활용한 현지 맛집 추천
- 🗺️ 인기 관광지 및 숨은 명소 발굴
- ⭐ 평점, 리뷰, 영업시간 등 상세 정보 제공

### 3️⃣ 지능형 일정 생성
- 📅 일자별 세부 일정 자동 구성
- 💼 예산 범위 내 최적화된 여행 계획
- 📊 상세 예산표 및 비용 분석

### 4️⃣ 다중 인터페이스 지원
- 🖥️ CLI 모드 (`main.py`): 터미널에서 빠른 실행
- 🌐 Web UI 모드 (`app.py`): Streamlit 기반 인터랙티브 인터페이스

---

## 🏗️ 시스템 아키텍처

### 멀티 에이전트 워크플로우

```
사용자 입력
    ↓
┌─────────────────────────────────────────┐
│  1단계: 여행 정보 수집                    │
│  (Travel Info Agent)                    │
│  - 항공편 검색 (왕복)                     │
│  - 숙소 정보 조회                        │
│  - 기본 일정 초안 작성                    │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  2단계: 현지 추천 추가                    │
│  (Local Recommendation Agent)           │
│  - 현지 맛집 추천 (아침/점심/저녁)        │
│  - 관광 명소 정보 추가                    │
│  - 환율 적용 및 상세 예산 계산            │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  3단계: 최종 일정 조율                    │
│  (Coordinator Agent)                    │
│  - 전체 정보 통합 및 정리                 │
│  - 일자별 일정표 최적화                   │
│  - 고객 전달용 문서 완성                  │
└─────────────┬───────────────────────────┘
              ↓
    최종 여행 일정 계획서
```

### 데이터 흐름

```
┌──────────────┐
│  User Input  │
│  (요구사항)   │
└──────┬───────┘
       │
       ↓
┌──────────────────────────────────────────┐
│          CrewAI Orchestration            │
│  ┌────────────────────────────────────┐  │
│  │  Context Passing Between Tasks     │  │
│  │  (단계별 결과 자동 전달)            │  │
│  └────────────────────────────────────┘  │
└──────┬───────────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────────┐
│          External APIs                   │
│  ┌─────────────┬──────────────────────┐  │
│  │ Amadeus API │ Google Places API    │  │
│  │ (항공/숙소)  │ (현지 정보)          │  │
│  └─────────────┴──────────────────────┘  │
│  ┌──────────────────────────────────┐    │
│  │  ExchangeRate API (환율)         │    │
│  └──────────────────────────────────┘    │
└──────┬───────────────────────────────────┘
       │
       ↓
┌──────────────┐
│ Final Output │
│ (여행 계획서) │
└──────────────┘
```

---

## 🛠️ 기술 스택

### Core Framework
- **[CrewAI](https://github.com/joaomdmoura/crewAI)** (0.114.0): 다중 에이전트 오케스트레이션
- **[LangChain](https://www.langchain.com/)** (0.3.23): LLM 통합 및 체인 구성
- **[OpenAI API](https://openai.com/api/)**: GPT-4 기반 자연어 처리

### Web Framework
- **[Streamlit](https://streamlit.io/)** (1.44.1): 웹 UI 구축

### API Integration
- **[Amadeus Travel API](https://developers.amadeus.com/)**: 항공편 및 호텔 검색
- **[Google Places API](https://developers.google.com/maps/documentation/places/web-service)**: 현지 장소 정보
- **[ExchangeRate API](https://www.exchangerate-api.com/)**: 환율 정보

### Development
- **Python** 3.12
- **dotenv**: 환경 변수 관리
- **requests**: HTTP 클라이언트
- **pydantic**: 데이터 검증

---

## 📁 프로젝트 구조

```
crewai_prj_workspace/
│
├── 📄 main.py                    # CLI 실행 엔트리포인트
├── 📄 app.py                     # Streamlit 웹 애플리케이션
├── 📄 crew.py                    # Crew 구성 클래스
├── 📄 agents.py                  # 에이전트 정의
├── 📄 tasks.py                   # 태스크 정의
├── 📄 tools.py                   # API 통합 도구
│
├── 📁 tools/                     # 개별 API 도구 모듈
│   ├── amadeus_flight_api.py
│   ├── amadeus_hotel_api.py
│   ├── google_places_api.py
│   └── exchangerate_api.py
│
├── 📄 requirements.txt           # Python 의존성
├── 📄 .env__                     # 환경 변수 템플릿
├── 📄 .gitignore                 # Git 무시 파일
│
├── 📁 문서/                      # 개발 가이드 문서
│   ├── 01_개발환경준비.md
│   ├── 02_프로젝트 구조 및 코드 설명.md
│   ├── 03_항공편과 숙소 정보 연동 실습.md
│   ├── 04_현지 맛집과 가볼만한 곳 추천 실습.md
│   └── 05_최종 여행 일정 생성 및 Streamlit UI 연동.md
│
└── 📄 README.md                  # 프로젝트 문서 (이 파일)
```

### 주요 파일 설명

| 파일명 | 역할 | 설명 |
|--------|------|------|
| `main.py` | CLI 실행 | 터미널에서 여행 일정 생성 |
| `app.py` | Web UI | Streamlit 기반 웹 인터페이스 |
| `crew.py` | Crew 구성 | 에이전트와 태스크를 묶어 Crew 생성 |
| `agents.py` | 에이전트 정의 | 3개의 전문 에이전트 설정 |
| `tasks.py` | 태스크 정의 | 3단계 작업 프롬프트 및 흐름 |
| `tools.py` | API 도구 | 외부 API 통합 도구 클래스 |

---

## ⚙️ 설치 및 환경 설정

### 1️⃣ 사전 요구사항

- **Python 3.12** 이상
- **conda** 또는 **venv** (가상환경 권장)
- **API 키** (아래 4개 필요)
  - OpenAI API Key
  - Amadeus API (Client ID & Secret)
  - Google Places API Key
  - ExchangeRate API Key

### 2️⃣ 설치 단계

#### Step 1: 저장소 클론 (또는 다운로드)

```bash
git clone <repository-url>
cd crewai_prj_workspace
```

#### Step 2: 가상환경 생성 및 활성화

**Conda 사용 시:**
```bash
conda create -n crewai_prj_env python=3.12
conda activate crewai_prj_env
```

**venv 사용 시:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

#### Step 3: 의존성 설치

```bash
pip install -r requirements.txt
```

**주요 패키지:**
- `crewai[tools]` - CrewAI 프레임워크 및 도구
- `streamlit` - 웹 UI
- `langchain-community` - LangChain 커뮤니티 통합
- `langchain-openai` - OpenAI LLM 통합
- `python-dotenv` - 환경 변수 관리
- `requests` - HTTP 요청

#### Step 4: 환경 변수 설정

1. `.env__` 파일을 `.env`로 복사:
   ```bash
   cp .env__ .env
   ```

2. `.env` 파일을 편집하여 실제 API 키 입력:
   ```bash
   MODEL=gpt-4o-mini
   OPENAI_API_KEY=your_openai_api_key_here
   AMADEUS_CLIENT_ID=your_amadeus_client_id
   AMADEUS_CLIENT_SECRET=your_amadeus_client_secret
   GOOGLE_API_KEY=your_google_api_key
   EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key
   ```

### 3️⃣ API 키 발급 가이드

#### OpenAI API
1. [OpenAI Platform](https://platform.openai.com/) 접속
2. 계정 생성 및 로그인
3. API Keys 메뉴에서 새 키 생성

#### Amadeus API
1. [Amadeus for Developers](https://developers.amadeus.com/) 접속
2. 무료 계정 생성 (Self-Service 플랜)
3. My Self-Service Workspace에서 Client ID/Secret 확인

#### Google Places API
1. [Google Cloud Console](https://console.cloud.google.com/) 접속
2. 프로젝트 생성
3. Maps Platform → Places API 활성화
4. 사용자 인증 정보에서 API 키 생성

#### ExchangeRate API
1. [ExchangeRate-API](https://www.exchangerate-api.com/) 접속
2. 무료 플랜 가입
3. 대시보드에서 API 키 확인

---

## 🚀 사용 방법

### CLI 모드 (터미널 실행)

가장 간단한 방법으로 여행 일정을 생성할 수 있습니다.

```bash
python main.py
```

**출력 예시:**
```
=================================================================
여행 일정 계획이 시작되었습니다...
=================================================================

[여행 전문가] 항공편 정보를 검색하고 있습니다...
✓ 인천 → 오사카 항공편 10개 조회 완료
✓ 숙소 정보 5개 조회 완료

[현지 전문가] 현지 맛집과 명소를 추천하고 있습니다...
✓ 오사카 인기 관광지 5곳 발견
✓ 현지 맛집 추천 완료
✓ 환율 적용 예산 계산 완료

[코디네이터] 최종 여행 일정을 정리하고 있습니다...
✓ 일자별 일정 최적화 완료

=================================================================
최종 여행 일정 계획서
=================================================================

## 1. 여행 개요
- 출발: 2025년 4월 25일
- 귀국: 2025년 4월 27일
- 목적지: 오사카
- 총 예산: 800,000원

## 2. 항공편 정보
[왕복 항공편 상세 정보...]

...
```

### Web UI 모드 (Streamlit)

웹 브라우저에서 인터랙티브하게 사용할 수 있습니다.

```bash
streamlit run app.py
```

브라우저가 자동으로 열리며 `http://localhost:8501`에서 앱에 접근할 수 있습니다.

**사용 단계:**
1. 📝 여행 계획 입력란에 요구사항 작성
2. 🖱️ "여행 일정 생성하기" 버튼 클릭
3. ⏳ 에이전트들이 순차적으로 작업 수행 (약 1-2분 소요)
4. 📋 생성된 여행 일정 확인

**입력 예시:**
```
2025년 5월 1일부터 3일까지 부산에서 도쿄로 여행을 가려고 합니다.
항공편, 숙소, 현지 맛집, 관광지를 포함한 여행 일정을 만들어주세요.
예산은 100만원 이내이고, 2인 여행입니다.
```

---

## 🔌 API 통합

### 1️⃣ FlightSearchTool (항공편 검색)

**기능:** Amadeus API를 통한 항공편 정보 조회

```python
from tools import FlightSearchTool

tool = FlightSearchTool()
flights = tool.run(
    origin_city="인천",
    destination_city="오사카",
    departure_date="2025-04-25",
    adults=1
)
```

**반환 데이터:**
```python
[
    {
        "가격": "300000",
        "통화": "KRW",
        "출발지": "ICN",
        "목적지": "OSA",
        "출발일": "2025-04-25",
        "항공사": "OZ",
        "편명": "112",
        "출발시간": "2025-04-25T09:00:00",
        "도착시간": "2025-04-25T11:00:00"
    },
    # ... 최대 10개
]
```

**지원 도시 코드:**
- 한국: 서울(SEL), 인천(ICN), 부산(PUS), 제주(CJU)
- 일본: 오사카(OSA), 도쿄(TYO), 후쿠오카(FUK), 삿포로(SPK)
- 중국: 베이징(BJS), 상하이(SHA), 홍콩(HKG)
- 동남아: 방콕(BKK), 싱가포르(SIN), 하노이(HAN) 등

### 2️⃣ HotelSearchTool (숙소 검색)

**기능:** 도시별 호텔 정보 및 가격 조회

```python
from tools import HotelSearchTool

tool = HotelSearchTool()
hotels = tool.run(
    city_name="오사카",
    check_in_date="2025-04-25",
    check_out_date="2025-04-27",
    adults=1
)
```

**반환 데이터:**
```python
[
    {
        "hotel_name": "오사카 시티 호텔",
        "check_in": "2025-04-25",
        "check_out": "2025-04-27",
        "room_description": "스탠다드 트윈룸 (금연)",
        "total_price": "50000",
        "currency": "JPY"
    },
    # ... 최대 10개
]
```

### 3️⃣ NearbyPlacesTool (현지 장소 추천)

**기능:** Google Places API를 통한 맛집/관광지 검색

```python
from tools import NearbyPlacesTool

tool = NearbyPlacesTool()
places = tool.run(
    place_name="오사카",
    radius=1000  # 미터
)
```

**반환 데이터:**
```python
[
    {
        "이름": "도톤보리",
        "주소": "오사카부 오사카시 주오구 도톤보리...",
        "전화번호": "+81-6-1234-5678",
        "웹사이트": "https://example.com",
        "영업시간": ["월: 09:00 - 22:00", ...],
        "평점": 4.5,
        "리뷰": [
            {"내용": "정말 좋았어요!", "평점": 5},
            # ... 최대 3개
        ]
    },
    # ... 최대 5개
]
```

### 4️⃣ ExchangeRateTool (환율 변환)

**기능:** 실시간 환율 정보를 활용한 통화 변환

```python
from tools import ExchangeRateTool

tool = ExchangeRateTool()
result = tool.run(
    from_currency="JPY",
    to_currency="KRW",
    amount=50000
)
```

**반환 데이터:**
```python
{
    "from_currency": "JPY",
    "to_currency": "KRW",
    "original_amount": 50000,
    "converted_amount": 500000,
    "conversion_rate": 10.0
}
```

---

## 🤖 에이전트 구조

### 1️⃣ Travel Info Agent (여행 전문가)

**역할:** 기본 여행 정보 수집 및 일정 초안 작성

**담당 업무:**
- ✈️ 항공편 검색 및 최적 옵션 선택
- 🏨 숙소 정보 조회 및 예약 제안
- 📅 일자별 기본 일정 초안 작성
- 💰 대략적인 비용 산출

**사용 도구:**
- `FlightSearchTool`: 항공편 정보 조회
- `HotelSearchTool`: 숙소 정보 검색
- `ExchangeRateTool`: 환율 변환

**출력 예시:**
```
## 기본 여행 일정 초안

### 항공편 정보
- 출발편: 2025-04-25 09:00 ICN → 11:00 OSA (대한항공 OZ112)
- 귀국편: 2025-04-27 18:00 OSA → 20:30 ICN (대한항공 OZ113)
- 항공권 비용: 300,000원

### 숙소 정보
- 호텔명: 오사카 시티 호텔
- 체크인: 2025-04-25 / 체크아웃: 2025-04-27
- 숙박비: ¥50,000 (약 500,000원)

### 일자별 일정
- Day 1 (4/25): 인천 출발 → 오사카 도착, 호텔 체크인
- Day 2 (4/26): 오사카 시내 자유 일정
- Day 3 (4/27): 호텔 체크아웃 → 귀국
```

### 2️⃣ Local Recommendation Agent (현지 전문가)

**역할:** 현지 맛집 및 명소 추천, 상세 예산 계산

**담당 업무:**
- 🍜 아침/점심/저녁 현지 맛집 추천
- 🗺️ 관광 명소 및 숨은 장소 발굴
- 💱 환율 적용 상세 예산 계산
- 📊 항목별 비용 내역 작성

**사용 도구:**
- `NearbyPlacesTool`: 현지 장소 정보
- `ExchangeRateTool`: 환율 변환

**출력 예시:**
```
## 현지 추천 정보 및 상세 예산

### Day 2 상세 일정
- 오전: 도톤보리 거리 산책 (무료)
- 점심: 이치란 라멘 (¥1,000 ≈ 10,000원)
- 오후: 오사카 성 관람 (입장료 ¥600 ≈ 6,000원)
- 저녁: 쿠로몬 시장 해산물 투어 (¥2,000 ≈ 20,000원)

### 상세 예산표
| 항목 | 금액 (원화) |
|------|------------|
| 항공권 (왕복) | 300,000원 |
| 숙박 (2박) | 500,000원 |
| 식비 (3일) | 100,000원 |
| 교통비 | 30,000원 |
| 입장료/체험 | 20,000원 |
| **총합** | **950,000원** |
```

### 3️⃣ Coordinator Agent (여행 일정 코디네이터)

**역할:** 전체 정보 통합 및 최종 일정 정리

**담당 업무:**
- 📝 앞선 단계 결과 종합
- ✅ 예산 범위 검증
- 📋 고객 전달용 문서 완성
- 🎨 일정표 포맷팅 및 최적화

**특징:**
- 도구 없이 이전 에이전트의 출력만으로 작업
- 일관성 있고 보기 좋은 최종 문서 생성

**출력 예시:**
```
# 오사카 2박3일 여행 계획서

## 1. 여행 개요
- **기간**: 2025년 4월 25일 ~ 27일 (2박 3일)
- **출발지**: 인천
- **목적지**: 오사카
- **인원**: 1명
- **총 예산**: 800,000원

## 2. 항공편 상세
[상세 항공편 정보...]

## 3. 일자별 일정
[일자별 세부 일정...]

## 4. 숙소 정보
[숙소 상세 정보...]

## 5. 상세 예산표
[항목별 비용...]

## 6. 추가 정보
[준비물, 팁 등...]
```

---

## 📚 개발 가이드

프로젝트의 각 단계별 상세 가이드 문서가 준비되어 있습니다:

### 📖 학습 경로

1. **[개발환경 준비](01_개발환경준비.md)**
   - Miniconda 설치
   - Python 3.12 가상환경 설정
   - VS Code 설정 및 확장 설치
   - 필수 패키지 설치 가이드

2. **[프로젝트 구조 및 코드 설명](02_프로젝트%20구조%20및%20코드%20설명.md)**
   - 전체 파일 구성 개요
   - 에이전트-태스크-크루 상호작용
   - 코드 실행 흐름 이해
   - 프롬프트 튜닝 실습

3. **[항공편과 숙소 정보 연동 실습](03_항공편과%20숙소%20정보%20연동%20실습.md)**
   - FlightSearchTool 활용법
   - HotelSearchTool 활용법
   - 기본 여행 일정 생성 프로세스
   - 프롬프트 개선 기법

4. **[현지 맛집과 가볼만한 곳 추천 실습](04_현지%20맛집과%20가볼만한%20곳%20추천%20실습.md)**
   - NearbyPlacesTool 활용법
   - 에이전트 프롬프트 개선
   - 터미널 실행 및 디버깅
   - API 호출 최적화

5. **[최종 여행 일정 생성 및 Streamlit UI 연동](05_최종%20여행%20일정%20생성%20및%20Streamlit%20UI%20연동.md)**
   - Streamlit 앱 구조 이해
   - UI 컴포넌트 커스터마이징
   - 결과 표시 형식 개선
   - 사용자 경험 향상 기법

### 🔧 커스터마이징 가이드

#### 새로운 도시 추가하기

`tools.py`의 `get_city_code()` 메서드에 도시 코드를 추가하세요:

```python
def get_city_code(self, city_name):
    city_codes = {
        # 기존 도시들...
        "파리": "PAR",        # 추가
        "런던": "LON",        # 추가
    }
    # ...
```

#### 에이전트 프롬프트 수정하기

`agents.py`에서 에이전트의 `backstory`를 수정하여 행동을 조정할 수 있습니다:

```python
travel_info_agent = Agent(
    role="여행 전문가",
    goal="여행 목적지와 관련된 최신의 유용한 정보를 수집하여 제공합니다.",
    backstory="당신은 여행자에게 꼭 필요한 최신 정보를 찾아내는 데 탁월한 능력을 지닌 전문가입니다. "
              "**특히 가성비 좋은 옵션을 찾는 데 특화되어 있습니다.**",  # 수정 부분
    # ...
)
```

#### 새로운 태스크 추가하기

`tasks.py`에 새로운 단계를 추가할 수 있습니다:

```python
weather_check_task = Task(
    description="여행 날짜의 목적지 날씨 정보를 조회하고 추천 복장을 제안합니다.",
    expected_output="날씨 예보 및 복장 추천",
    agent=weather_agent,
    context=[initial_travel_plan_task]
)
```

그리고 `crew.py`에서 Crew에 추가:

```python
return Crew(
    agents=[travel_info_agent, weather_agent, local_recommendation_agent, coordinator_agent],
    tasks=[initial_travel_plan_task, weather_check_task, local_recommendation_task, final_coordinator_task],
    # ...
)
```

---

## 🐛 문제 해결

### 일반적인 오류

#### 1️⃣ API 인증 실패

**증상:**
```
Exception: Amadeus 토큰 발급 실패
```

**해결 방법:**
- `.env` 파일에 API 키가 올바르게 입력되었는지 확인
- API 키에 공백이나 따옴표가 없는지 확인
- Amadeus 계정에서 Test 환경 키를 사용하는지 확인

#### 2️⃣ 도시 코드 오류

**증상:**
```
ValueError: '파리'의 도시 코드를 찾을 수 없습니다.
```

**해결 방법:**
- `tools.py`의 `city_codes` 딕셔너리에 해당 도시 추가
- 또는 지원되는 도시로 변경

#### 3️⃣ 환율 API 한도 초과

**증상:**
```
Exception: 환율 정보 조회 실패
```

**해결 방법:**
- ExchangeRate API의 무료 플랜 한도 확인 (월 1,500 요청)
- 필요시 유료 플랜으로 업그레이드
- 또는 환율을 고정값으로 하드코딩

#### 4️⃣ Streamlit 실행 오류

**증상:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**해결 방법:**
```bash
pip install streamlit
# 또는
pip install -r requirements.txt
```

### 디버깅 팁

#### 1. Verbose 모드 활성화

에이전트 실행 과정을 자세히 확인하려면 `verbose=True` 설정 확인:

```python
# agents.py
travel_info_agent = Agent(
    # ...
    verbose=True  # 로그 출력
)
```

#### 2. 중간 결과 출력

각 태스크의 결과를 확인하려면:

```python
# main.py
result = TravelCoordinatorCrew().crew().kickoff(inputs=inputs)
print(f"1단계 결과: {result.tasks_output[0]}")  # 첫 번째 태스크 결과
print(f"2단계 결과: {result.tasks_output[1]}")  # 두 번째 태스크 결과
```

#### 3. API 응답 테스트

개별 도구를 독립적으로 테스트:

```python
# tool_test.ipynb 참고
from tools import FlightSearchTool

tool = FlightSearchTool()
result = tool.run(origin_city="인천", destination_city="오사카", departure_date="2025-04-25", adults=1)
print(result)
```

---

## 🤝 기여 방법

프로젝트에 기여하고 싶으신가요? 환영합니다! 🎉

### 기여 절차

1. **Fork** 저장소
2. **Clone** your fork
   ```bash
   git clone https://github.com/your-username/crewai-travel-planner.git
   ```
3. **Branch** 생성
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Commit** 변경사항
   ```bash
   git commit -m "Add some amazing feature"
   ```
5. **Push** to branch
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Pull Request** 생성

### 기여 아이디어

- 🌍 새로운 여행지 추가
- 🔧 새로운 API 통합 (날씨, 액티비티 등)
- 🎨 UI/UX 개선
- 📝 문서 개선 및 번역
- 🐛 버그 수정
- ⚡ 성능 최적화

---

## 📜 라이선스

이 프로젝트는 **MIT License** 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

```
MIT License

Copyright (c) 2025 CrewAI Travel Planner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📞 연락처 및 지원

### 문의사항

- 📧 Email: support@example.com
- 💬 Issues: [GitHub Issues](https://github.com/your-repo/issues)
- 📖 Documentation: [Wiki](https://github.com/your-repo/wiki)

### 참고 자료

- [CrewAI 공식 문서](https://docs.crewai.com/)
- [LangChain 문서](https://python.langchain.com/)
- [Streamlit 문서](https://docs.streamlit.io/)
- [Amadeus API 문서](https://developers.amadeus.com/self-service)

---

## 🌟 Star History

이 프로젝트가 도움이 되셨다면 ⭐ Star를 눌러주세요!

---

## 🙏 감사의 말

- [CrewAI](https://github.com/joaomdmoura/crewAI) 프레임워크 개발팀
- [LangChain](https://www.langchain.com/) 커뮤니티
- [Amadeus](https://developers.amadeus.com/), [Google](https://developers.google.com/), [ExchangeRate-API](https://www.exchangerate-api.com/) API 제공
- 모든 기여자 및 사용자 여러분

---

<div align="center">

**Made with ❤️ by CrewAI Travel Planner Team**

[⬆ 맨 위로 이동](#-crewai-기반-ai-여행-일정-플래너)

</div>

