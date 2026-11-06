# 📦 Olist AI 데이터 분석 및 대시보드 프로젝트

> Python과 머신러닝을 활용한 브라질 이커머스 데이터 분석 프로젝트

## 📌 1. 프로젝트 소개

브라질 온라인 쇼핑 플랫폼 Olist의 데이터를 활용하여
데이터 분석, 머신러닝, AI 기반 대시보드 및 RAG 챗봇을 실습한 프로젝트입니다.

데이터 분석 결과를 사용자가 쉽게 이해하고 활용할 수 있도록
Streamlit 기반 웹 대시보드로 구현했습니다.

### 프로젝트 목표

- 이커머스 주문 및 판매 데이터 분석
- 데이터 전처리와 시각화
- 머신러닝 모델을 활용한 예측 및 추천
- Streamlit 기반 대시보드 구현
- RAG 챗봇을 통한 근거 기반 질의응답

## 📊 2. 주요 기능

| 기능 | 설명 |
|---|---|
| 🏠 홈 | 프로젝트 소개 및 주요 분석 지표 |
| 📊 데이터 분석 | 주문 데이터를 활용한 통계 및 시각화 |
| 💬 리뷰 감성 분석 | 포르투갈어 리뷰의 긍정·부정 판정 |
| 🛍️ 상품 추천 | 비슷한 특성을 가진 상품 5개 추천 |
| 🏪 판매자 유형 | 판매자 데이터를 활용한 유형 분류 |
| 🚨 판매자 이탈 위험 | 판매자의 이탈 위험 예측 |
| 🤖 분석 Q&A | 분석 결과와 근거ID를 활용한 질의응답 |

## 🛠️ 3. 사용 기술

- Python
- Pandas / NumPy
- Scikit-learn
- Streamlit
- LangChain
- OpenAI API
- Google Colab
- Visual Studio Code

## 📁 4. 프로젝트 폴더 구조

```text
olist_dashboard/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
├── model/
├── utils/
└── views/
```

## ⚠️ 5. 프로젝트 안내
본 프로젝트는 AI 기반 데이터 저널리즘 교육과정에서
데이터 분석 및 머신러닝 활용 방법을 학습하기 위해 제작했습니다.

AI 모델의 예측값은 실제 결과를 보장하지 않으며,
분석 결과를 활용할 때는 데이터의 출처와 집계 기준을 확인해야 합니다.

또한 RAG 챗봇의 답변에 포함된 근거ID는
실제 자료에 존재하는지 별도로 검증해야 합니다.

## ▶️ 6. 프로젝트 실행 방법

### 1단계: 프로젝트 폴더 열기

VS Code에서 `olist_dashboard` 폴더를 엽니다.

### 2단계: 가상환경 만들기

Windows PowerShell 터미널에서 실행합니다.

```powershell
py -3.10 -m venv .venv
```

### 3단계: 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4단계: 필요한 패키지 설치

```powershell
python -m pip install -r requirements.txt
```

### 5단계: 대시보드 실행

```powershell
python -m streamlit run app.py
```

실행 후 터미널에 표시되는 로컬 주소로 접속합니다.

일반적으로 다음 주소를 사용합니다.

`http://localhost:8501`

### 참고 사항

- 분석 데이터와 학습된 모델 파일이 필요합니다.
- 분석 Q&A 기능은 별도의 OpenAI API 키가 필요합니다.
- API 키는 GitHub에 업로드하지 않습니다.
- Python 버전과 패키지 호환성은 실행 환경에 따라 확인해야 합니다.

## 📸 7. 프로젝트 실행 화면

### ① 대시보드 홈
프로젝트 소개와 주요 분석 지표를 확인할 수 있습니다.

![대시보드 홈](screenshots/01_home.png)

### ② 데이터 분석
Olist 주문 데이터의 주요 지표와 그래프를 확인합니다.

![데이터 분석](screenshots/02_analysis.png)

### ③ 리뷰 감성 분석
포르투갈어 리뷰 문장을 분석하여 긍정 또는 부정을 예측합니다.

![리뷰 감성 분석](screenshots/03_sentiment.png)

### ④ 상품 추천
선택한 상품과 특성이 비슷한 상품 5개를 추천합니다.

![상품 추천](screenshots/04_recommend.png)

### ⑤ 판매자 유형 분석
판매자의 활동 데이터를 바탕으로 유형을 분류합니다.

![판매자 유형](screenshots/05_seller_segment.png)

### ⑥ 판매자 이탈 위험 예측
판매자의 이탈 위험을 예측하여 확인합니다.

![판매자 이탈 위험](screenshots/06_seller_churn.png)

### ⑦ RAG 분석 Q&A
분석 결과와 모델 설명, 실습용 규정집을 활용하여 질문에 답변하고 근거ID를 표시합니다.

![RAG 챗봇 실행 화면 1](screenshots/07_rag_chatbot_1.png)

![RAG 챗봇 실행 화면 2](screenshots/07_rag_chatbot_2.png)

## 📄 8. 프로젝트 발표자료

Olist 데이터 분석부터 머신러닝, Streamlit 대시보드, RAG 챗봇까지의 전체 실습 과정을 정리한 PDF 발표자료입니다.

### 📥 발표자료 보기

[📘 Olist AI 프로젝트 전체 발표자료 PDF 열기](docs/Olist_AI_Project_Portfolio.pdf)