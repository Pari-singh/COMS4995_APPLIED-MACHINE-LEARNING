import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
iris_dataset['data'], iris_dataset['target'], random_state=0)


fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(20,15), sharex='none', sharey='none')
a = axes[0, 0].hist(X_train[:,0], edgecolor='black', bins=20, color = 'blue')
b = axes[1, 1].hist(X_train[:,1], edgecolor='black', bins=20, color = 'blue')
c = axes[2, 2].hist(X_train[:,2], edgecolor='black', bins=20, color = 'blue')
d = axes[3, 3].hist(X_train[:,3], edgecolor='black', bins=20, color = 'blue')
color_dict = {0:'blue', 1: 'red', 2:'green'}
labels = {0:'sentosa', 1:'versicolor', 2:'verginica'}
scatter_x0 = np.array(X_train[:,0])
scatter_x1 = np.array(X_train[:,1])
scatter_x2 = np.array(X_train[:,2])
scatter_x3 = np.array(X_train[:,3])
vals = ['x','y','z']
for g in np.unique(y_test) :
    ix = np.where(y_train == g)
    axes[0, 1].scatter(scatter_x1[ix], scatter_x0[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[0, 2].scatter(scatter_x2[ix], scatter_x0[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[0, 3].scatter(scatter_x3[ix], scatter_x0[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[1, 0].scatter(scatter_x0[ix], scatter_x1[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[1, 2].scatter(scatter_x2[ix], scatter_x1[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[1, 3].scatter(scatter_x3[ix], scatter_x1[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[2, 0].scatter(scatter_x0[ix], scatter_x2[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[2, 1].scatter(scatter_x1[ix], scatter_x2[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[2, 3].scatter(scatter_x3[ix], scatter_x2[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[3, 0].scatter(scatter_x0[ix], scatter_x3[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[3, 1].scatter(scatter_x1[ix], scatter_x3[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
    axes[3, 2].scatter(scatter_x2[ix], scatter_x3[ix],c=color_dict[g], label = labels[g]).axes.legend(fontsize = 'x-small')
lbls = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
for i in range(len(axes.flat)):
    axes.flat[i].set(xlabel=lbls[i%4], ylabel=lbls[int(i/4)])
for ax in axes.flat:
    ax.label_outer()
plt.subplots_adjust(wspace=0, hspace=0)
fig.savefig('task22.png',bbox_inches='tight')
plt.show(block=True)