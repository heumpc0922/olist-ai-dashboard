"""
Olist 리뷰 감성분석 - 딥러닝 모델

사용 모델:
- part7_2_tokenizer.pkl
- part7_2_sentiment_model.keras
"""

import streamlit as st

from utils.deep_sentiment import predict_deep_sentiment


# ① 화면 제목
st.title("🧠 Olist 딥러닝 리뷰 감성분석")

st.caption(
    "Embedding 기반 딥러닝 모델을 이용해 "
    "포르투갈어 상품 리뷰의 감성을 분석합니다."
)

st.info(
    "이 모델은 포르투갈어 리뷰로 학습했습니다. "
    "한국어와 영어는 정확한 분석이 어려울 수 있습니다."
)


# ② 예시 리뷰
examples = {
    "직접 입력": "",
    "긍정 리뷰": "produto muito bom gostei",
    "부정 리뷰": "produto ruim nao gostei",
    "배송 지연 리뷰": "ainda nao recebi o produto",
}


# ③ 예시 선택
selected = st.selectbox(
    "예시 리뷰 선택",
    list(examples.keys())
)


# ④ 리뷰 입력창
review_text = st.text_area(
    "분석할 리뷰를 입력하세요 (포르투갈어)",
    value=examples[selected],
    height=130,
    placeholder="포르투갈어 리뷰를 입력하세요."
)


# ⑤ 분석 버튼
if st.button("🔍 딥러닝 감성분석 실행", type="primary"):

    if not review_text.strip():
        st.warning("분석할 리뷰 문장을 입력해 주세요.")

    else:
        try:
            # 딥러닝 모델 실행
            with st.spinner("딥러닝 모델이 리뷰를 분석하고 있습니다..."):
                result, probability = predict_deep_sentiment(
                    review_text
                )

            # ⑥ 분석 결과 표시
            st.subheader("📊 감성분석 결과")

            st.metric(
                label="AI 감성 판정",
                value=result
            )

            st.metric(
                label="긍정 예측 점수",
                value=f"{probability * 100:.1f}%"
            )

            # ⑦ 확률 막대
            st.progress(
                probability,
                text=f"긍정 예측 점수: {probability * 100:.1f}%"
            )

            # ⑧ 결과 해석
            if probability >= 0.5:
                st.success(
                    "딥러닝 모델이 이 리뷰를 긍정으로 분류했습니다."
                )
            else:
                st.error(
                    "딥러닝 모델이 이 리뷰를 부정으로 분류했습니다."
                )

            # ⑨ 분석 주의사항
            st.caption(
                "※ 표시된 확률은 모델의 예측 점수이며, "
                "실제 정답일 확률을 보장하지 않습니다."
            )

        except ValueError as error:
            st.warning(str(error))

        except Exception as error:
            st.error("딥러닝 모델 실행 중 오류가 발생했습니다.")
            st.exception(error)


# ⑩ 사용 모델 안내
with st.expander("📘 사용된 딥러닝 모델 정보"):

    st.write("**모델:** Embedding 기반 딥러닝")
    st.write("**입력 언어:** 포르투갈어")
    st.write("**입력 길이:** 최대 50개 단어 번호")
    st.write("**분석 결과:** 긍정 또는 부정")
    st.write("**긍정 판정 기준:** 모델 출력값 0.5 이상")

    st.warning(
        "이 모델은 교육용으로 제작됐습니다. "
        "실제 고객 평가나 중요한 의사결정에 사용하려면 "
        "추가 검증이 필요합니다."
    )
