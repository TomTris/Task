import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
import numpy as np
import seaborn as sns
import screeninfo

def display_inside_axs(colors, axs):
    col = -1
    row = 0

    for ax in axs:
        col += 1
        if col == len(citerias):
            col = 0
            row += 1
        if col == row:
            max = df[citerias[col]].max()
            min = df[citerias[col]].min()
            for cnt in range(len(df_of_qualities)):
                ax.hist((df_of_qualities[cnt])[citerias[col]], \
                    bins=20, alpha=0.7, color=colors[cnt], range=(min, max))
        else:
            for cnt, df_of_house in enumerate(df_of_qualities):
                ax.scatter(x=df_of_house[citerias[col]], y=df_of_house[citerias[row]],\
                    alpha=0.5, color=[colors[cnt]], s=3)


def on_key(event):
    if event.key == 'escape':
        plt.close()


def display_all():
    num_citerias = len(citerias)
    colors = sns.color_palette("tab10", n_colors=len(qualities))
    custom_lines = [[qualities[i], (Line2D([0], [1], color=colors[i], lw=16))] for i in range(len(colors))]
    custom_lines = sorted(custom_lines, key=lambda x: x[0])
    custom_lines = [line[1] for line in custom_lines]
    screen = screeninfo.get_monitors()[0]
    fig, axs = plt.subplots(ncols=num_citerias, nrows=num_citerias, \
                        figsize=(screen.width / 120, screen.height / 113))
    axs = axs.flatten()
    display_inside_axs(colors, axs)

    
    fig.legend(custom_lines, sorted(qualities),\
                fontsize='x-large', loc='lower right', ncol=len(qualities), bbox_to_anchor=(1, 0),\
                handlelength=4.5, handleheight=3.5, borderpad=1.0)
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()

name = "winequality-red.csv"

def main():
    global df
    global citerias
    global qualities
    global df_of_qualities

    df = pd.read_csv(name, sep=";")
    citerias = df.columns[0:-1]
    qualities = np.unique(df[np.array(df.columns)[-1]])
    linked_qualities_df = [[int(quality), df[df.values[:, -1] == quality]] for quality in qualities]
    linked_qualities_df = sorted(linked_qualities_df, key=lambda x: len(x[1]))[::-1]

    qualities = [item[0] for item in linked_qualities_df]
    df_of_qualities = [item[1] for item in linked_qualities_df]
    display_all()

if __name__ == "__main__":
    main()
