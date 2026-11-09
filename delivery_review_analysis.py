# Olist 배송 지연 여부와 고객 리뷰 평점 비교
# 2026.11.09 데이터 분석 실습

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# 1. 데이터 불러오기
base_path = Path(__file__).resolve().parent

data_path = base_path / "data" / "orders.parquet"

df = pd.read_parquet(data_path)

# 2. 결측치 제거
valid = df.dropna(subset=["지연", "review_score"])

# 3. 배송 지연 여부별 평균 평점 계산
result = valid.groupby("지연")["review_score"].agg(
    ["count", "mean", "median"]
)

normal = result.loc[False, "mean"]
delayed = result.loc[True, "mean"]

print("배송 지연 여부별 리뷰 평점")
print(result.round(2))

print(f"\n정상 배송 평균: {normal:.2f}점")
print(f"지연 배송 평균: {delayed:.2f}점")
print(f"평균 평점 차이: {normal - delayed:.2f}점")

# 4. 그래프 만들기
fig, ax = plt.subplots(figsize=(9, 6))

labels = ["On-time delivery", "Delayed delivery"]
values = [normal, delayed]

bars = ax.bar(
    labels,
    values,
    color=["steelblue", "coral"],
    width=0.55
)

# 5. 그래프 제목과 축 설정
ax.set_title(
    "Olist: Delivery Delay vs Review Score",
    fontsize=15
)

ax.set_ylabel("Average Review Score")
ax.set_ylim(0, 5)

# 6. 막대 위에 실제 평균 평점 표시
for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.08,
        f"{height:.2f}",
        ha="center",
        fontsize=12
    )

# 7. 그래프 저장
save_path = base_path / "screenshots" / "delivery_review_comparison.png"

save_path.parent.mkdir(parents=True, exist_ok=True)

fig.savefig(
    save_path,
    dpi=200,
    bbox_inches="tight"
)

print(f"\n그래프 저장 완료: {save_path}")

# 8. 그래프 화면 출력
plt.show()