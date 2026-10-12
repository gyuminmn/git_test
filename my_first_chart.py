import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"

km =[3.8, 5.2, 4.4, 4.2, 5.1]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(km)
for i, p in enumerate(km):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 8), ha="center")
ax.set_title("나의 매 주 일요일 조기축구 운동거리량(단위=km)")
fig.savefig("my _first_chart.png")

plt.show()