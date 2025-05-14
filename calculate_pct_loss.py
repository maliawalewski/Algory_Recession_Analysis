import matplotlib.pyplot as plt
import seaborn as sns

class Entry:
    def __init__(self, start_price, end_price):
        self.start_price = start_price
        self.end_price = end_price

    def calculate_pct_change(self):
        return (self.end_price - self.start_price) / self.start_price * 100
    
list = []
list.append(Entry(2053.73,1293.81))
list.append(Entry(114.86,69))
list.append(Entry(65.12,15.94))
list.append(Entry(108.45,52.86))
list.append(Entry(27.32,16.86))
list.append(Entry(140,70))
list.append(Entry(41.27,16))
list.append(Entry(90.09,45))
list.append(Entry(111.15,65))
list.append(Entry(61.39,39.81))
list.append(Entry(35.81,11.45))

# TRIP, MAR, EXPE, BKNG, IHG, H, MAR

pct = []
for e in list:
    pct.append(e.calculate_pct_change())

sns.boxplot(data=pct)
plt.title("Distribution of Company Performances During Recessions")
plt.ylabel("Percent Change of stock price")
plt.show()