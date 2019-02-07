import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', header=0)

fig = plt.figure()
ax1 = plt.gca()
line1, = ax1.plot(df['Year'], df['spending '], c='r', linestyle='-', marker='o')
ax2 = ax1.twinx()
line2, = ax2.plot(df['Year'], df['Suicides'], c = 'black', linestyle='-', marker='o')
ax1.set_ylabel("US spending on Science in billion")
ax2.set_ylabel("Hanging suicide")
ax2.legend((line1, line2),
           ("US spending on Science in billion", "Hanging suicide"))
ax2 = ax2.twiny()
ax2.set_title("US spending on Science, space and Technology \n correlates with \n Suicides by hanging, strangulation and suffocation \n\n")
fig.savefig('task21.png',bbox_inches='tight')
plt.show(block=True)