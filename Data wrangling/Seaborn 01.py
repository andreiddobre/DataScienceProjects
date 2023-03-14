import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(30).reshape(3,10))
correlations = df.corr()

#rectangular dataset 2D dataset that can be coerced into an ndarray
#if True, set the Axes aspect to 'equal' so that each cell will be square-shaped
#Matplotlib colormap name, object or list of colors
#Use annot to represent the cell values with text, control the annotations with a formatting string
ax1 = sns.heatmap(correlations, cbar=True, linewidths=0.3, vmin=-1, vmax=1, square = True, cmap = 'copper', annot=True, fmt='.2f')

plt.yticks(rotation = 0)
plt.xticks(rotation = 90)
plt.title("Seaborn Heatmap Random Data [Copper]")
plt.show()
