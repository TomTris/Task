import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

name = "winequality-red.csv"
df = pd.read_csv(name, sep=";")
qualities = np.unique(df['quality'])
samples = []

for quality in qualities:
	samples.append(len(df[df['quality'] == quality]))
print(samples)

total_samples = sum(samples)
percentages = [sample / total_samples * 100 for sample in samples]

plt.figure(figsize=(15, 8))
colors = plt.cm.tab10.colors 

wedges, texts = plt.pie(samples, colors=colors, startangle=140)

labels = [f'Quality {quality}: {sample} ({percentage:.1f}%)' for quality, sample, percentage in zip(qualities, samples, percentages)]
plt.legend(wedges, labels, title="Quality Samples", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 1), fontsize=10)

plt.title('Sample Distribution by Quality')

plt.axis('equal')  

plt.show()