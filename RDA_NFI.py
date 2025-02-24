import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

nfi = yf.download("NFI.TO", start="2019-10-01", end="2100-01-01", auto_adjust=False)

rev = yf.download("BYD", start="2019-10-01", end="2100-01-01", auto_adjust=False)

# Take the last 150 days of adjusted closing prices for both stocks
closing_nfi = nfi["Adj Close"][-10000:]
closing_rev = rev["Adj Close"][-10000:]

normalized_nfi = closing_nfi
normalized_rev = closing_rev

print(normalized_nfi)
plt.plot(normalized_nfi, label="NFI Group (NFI.TO)", color="blue")

plt.plot(normalized_rev, label="REV Group (REVG)", color="green")

#150 days up to whatever the CURRENT day is
closing = np.array(closing_nfi)

# print(np.mean(closing))

pct_change = (closing[1:]/closing[:-1] - 1) * 100

print(np.std(pct_change))

# plt.plot(pct_change,label = "Percent Change", color="red")

plt.title("Comparison of NFI Group and REV Group Prices During 2020 Recession")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price / Initial Close Price") 
plt.legend()

plt.show()