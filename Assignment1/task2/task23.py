import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc

df = pd.read_csv('mpg.csv', header=0, index_col=0)

def rand_jitter(arr, val):
    stdev = val*(max(arr)-min(arr))
    return arr + np.random.randn(len(arr)) * stdev

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,15))
color_dict = {'f':'goldenrod', 'r': 'blue', '4':'black'}
labels = {"4":"4WD", "f":"FWD", "r":"RWD"}
scatter_x = np.array(df['cty'])
scatter_y = np.array(df['displ'])
for g in np.unique(df['drv']):
    ix = np.where(df['drv'] == g)
    axes[0,0].scatter(scatter_x[ix], scatter_y[ix], c = color_dict[g], label = labels[g], s = 100).axes.legend(fontsize = 'large')
    axes[0,1].scatter(scatter_x[ix], scatter_y[ix], c = color_dict[g], label = labels[g], alpha=0.5, s = 100).axes.legend(fontsize = 'large')
    axes[1,0].scatter(rand_jitter(scatter_x[ix], 0.02), rand_jitter(scatter_y[ix], 0.02), c = color_dict[g], label = labels[g], alpha = 0.5, s =100).axes.legend(fontsize = 'large')
    axes[1,1].scatter(rand_jitter(scatter_x[ix], 0.08), rand_jitter(scatter_y[ix], 0.08), c = color_dict[g], label = labels[g], alpha = 0.5, s =100).axes.legend(fontsize = 'large')
for i in axes.flat:
    i.set(xlabel='Displacement', ylabel='Fuel economy (mpg)')

fig.savefig('task23.png',bbox_inches='tight')
plt.show(block=True)