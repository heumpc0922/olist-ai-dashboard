"""
Olist 딥러닝 리뷰 감성분석

사용 파일:
1. part7_2_tokenizer.pkl
2. part7_2_sentiment_model.keras

입력: 포르투갈어 리뷰
출력: 긍정/부정 및 긍정 확률
"""

from pathlib import Path
import pickle

import streamlit as st

# 모델이 학습할 때 사용한 문장 길이
MAX_LEN = 50

# 프로젝트 폴더 위치
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"


@st.cache_resource
def load_deep_learning_model():
    """딥러닝 모델과 Tokenizer를 불러옵니다."""

    from tensorflow.keras.models import load_model

    model_path = MODEL_DIR / "part7_2_sentiment_model.keras"
    tokenizer_path = MODEL_DIR / "part7_2_tokenizer.pkl"

    # 모델 파일 확인
    if not model_path.is_file():
        raise FileNotFoundError(
            f"딥러닝 모델 파일이 없습니다: {model_path}"
        )

    if not tokenizer_path.is_file():
        raise FileNotFoundError(
            f"Tokenizer 파일이 없습니다: {tokenizer_path}"
        )

    # 신뢰할 수 있는 수업 자료의 Tokenizer만 불러옵니다.
    with open(tokenizer_path, "rb") as file:
        tokenizer = pickle.load(file)

    # 학습된 딥러닝 모델 불러오기
    model = load_model(model_path, compile=False)

    return model, tokenizer


def predict_deep_sentiment(text):
    """리뷰를 입력받아 긍정/부정을 예측합니다."""

    from tensorflow.keras.preprocessing.sequence import pad_sequences

    # 빈 문장 검사
    if not text or not text.strip():
        raise ValueError("리뷰 문장을 입력해 주세요.")

    # 모델과 Tokenizer 불러오기
    model, tokenizer = load_deep_learning_model()

    # ① 문장을 숫자 배열로 변환
    sequence = tokenizer.texts_to_sequences([text])

    # ② 문장 길이를 50개로 통일
    padded = pad_sequences(
        sequence,
        maxlen=MAX_LEN,
        padding="post",
        truncating="post"
    )

    # 학습된 단어가 있는지 확인
    known_words = [
        number
        for number in sequence[0]
        if number not in (0, 1)
    ]

    if not known_words:
        raise ValueError(
            "모델이 알고 있는 단어가 없습니다. "
            "포르투갈어 리뷰를 입력해 주세요."
        )

    # ③ 딥러닝 모델로 예측
    prediction = model.predict(padded, verbose=0)

    # ④ 긍정 확률 계산
    probability = float(prediction[0][0])

    # ⑤ 긍정/부정 구분
    if probability >= 0.5:
        result = "긍정 😊"
    else:
        result = "부정 😞"

    return result, probability
