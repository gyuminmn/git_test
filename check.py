import pandas as pd
import matplotlib.pyplot as plt

watchlist_df = pd.read_csv("watchlist.csv", dtype={"code": str})
print(watchlist_df["code"].tolist())

prices = [71000, 70500, 71800, 72400, 71900]
fig, ax = plt. subplots()
ax.plot (prices)
fig.savefig("my _first_chart.png")

days = [1, 2, 3, 4, 5]
ax.plot(days, prices) #x를 직접 정하려면 둘을 넘깁니다
ax.plot(prices) # x가 없으면 x는 0,1,2,3,4 가 자동으로 붙습니다

for i, p in enumerate(prices):
    ax.annotate (f"{p:,}", (i, p),
                textcoords="offset points",
                xytext=(0, 8), ha="center")

plt.show()