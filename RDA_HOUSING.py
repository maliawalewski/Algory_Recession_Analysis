import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# the approximate starting and ending dates of the housing crisis
start_date = "2007-09-01"
end_date = "2009-06-01"

a = yf.download("MUSA", start=start_date, end=end_date, auto_adjust=False)
b = yf.download("^SP500TR", start=start_date, end=end_date, auto_adjust=False)
c = yf.download("CASY", start=start_date, end=end_date, auto_adjust=False)
d =yf.download("8278.T", start=start_date, end=end_date, auto_adjust=False)
e = yf.download("ATD.TO", start=start_date, end=end_date, auto_adjust=False)
f = yf.download("SVNDY", start=start_date, end=end_date, auto_adjust=False)
g = yf.download("5903.TWO", start=start_date, end=end_date, auto_adjust=False)

# Take the last 150 days of adjusted closing prices for both stocks
closing_a = a["Adj Close"][-10000:]
closing_b = b["Adj Close"][-10000:]
closing_c = c["Adj Close"][-10000:]
closing_d = d["Adj Close"][-10000:]
closing_e = e["Adj Close"][-10000:]
closing_f = f["Adj Close"][-10000:]
closing_g = g["Adj Close"][-10000:]
# norm_a = closing_a / closing_a.iloc[0]
norm_b = closing_b / closing_b.iloc[0]
norm_c = closing_c / closing_c.iloc[0]
norm_d = closing_d / closing_d.iloc[0]
norm_e = closing_e / closing_e.iloc[0]
norm_f = closing_f / closing_f.iloc[0]
norm_g = closing_g / closing_g.iloc[0]

# plt.plot(trip_exp, label = "Trip Advisor", color="purple")
# plt.plot(norm_a, label="Murphy USA", color="blue")
plt.plot(norm_b, label="S&P500 (SPY)", color="red")
plt.plot(norm_c,label="Caseys General Stores", color = "yellow")
plt.plot(norm_d,label="Fuji Co", color="purple")
plt.plot(norm_e,label="Alimentation Couche Tard", color = "blacK")
plt.plot(norm_f,label="Seven Eleven", color="green")
plt.plot(norm_g,label="Family Mart", color="brown")

plt.title("RDA")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price / Initial Close Price")
plt.legend()

plt.show()