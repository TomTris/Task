import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import csv 
import pandas as pd
import sys
import numpy as np
import seaborn as sns
import matplotlib.ticker as ticker

column = 20
houses = 0

value_from_column = 0
value_to_column = -1

def format_ticks(x, pos):
    if x >= 1000 or x <= -1000:
        return f'{int(x/1000)}k'
    return str(int(x))

def eprint(*args, **kwargs):
	print('Error:', *args, file=sys.stderr, **kwargs)

def display_all(df, citerias, qualities, data_each_quality):
	num_citerias = len(citerias)
	ncols = int(num_citerias ** 0.5) + 1
	nrows = (num_citerias - 1 ) // ncols + 1
	fig, axs = plt.subplots(nrows, ncols, figsize=(15, 12))
	axs = axs.flatten() #convert 2D to 1D Axes
	colors = sns.color_palette("tab10", n_colors=len(qualities))
	for i, citeria in enumerate(citerias):
		max_value = df[citeria].max()
		min_value = df[citeria].min()
		for cnt in range(len(qualities)):
			axs[i].hist((data_each_quality[cnt])[citeria], bins=column, alpha=0.8, color=colors[cnt], range=(min_value, max_value))
		axs[i].set_title(citeria)
		axs[i].set_xlabel('value')
		axs[i].set_ylabel('Frequency')
		# axs[i].xaxis.set_major_formatter(ticker.FuncFormatter(format_ticks))
		# axs[i].yaxis.set_major_formatter(ticker.FuncFormatter(format_ticks))
	for j in range(len(citerias), len(axs)):
		fig.delaxes(axs[j])
	custom_lines = []
	for i in range(len(colors)):
		custom_lines.append(Line2D([0], [1], color=colors[i], lw=16))
	fig.legend(custom_lines, qualities,\
				fontsize='x-large', loc='lower right', ncol=1, bbox_to_anchor=(1, 0),\
				handlelength=4.5, handleheight=3.5, borderpad=1.0)

	plt.tight_layout()
	plt.show()


name = "abc.csv"

def main() -> None:
		df = pd.read_csv(name, sep=";")
		citerias = df.columns[0:-1]
		qualities = np.unique(df.values[:, -1])
		linked_quality_data = [[int(quality), df[df.values[:, -1] == quality]] for quality in qualities]

		sorted_data = sorted(linked_quality_data, key=lambda x: len(x[1]))[::-1]
		qualities = [item[0] for item in sorted_data]
		data_each_quality = [item[1] for item in sorted_data]
		display_all(df, citerias, qualities, data_each_quality)




if  __name__ == "__main__":
	main()
