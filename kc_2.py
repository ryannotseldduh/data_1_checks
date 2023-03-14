import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('car_price.csv')
sns.jointplot(x='price',xlim=(0,50000), y='highwaympg', ylim=(10,55), data=data, kind='scatter', hue="carbody")
plt.show()