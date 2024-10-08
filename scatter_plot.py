from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from matplotlib.lines import Line2D
import seaborn as sns
import numpy as np

name = "winequality-red.csv"
current_citeria_index = 0

def display_quality(fig, axs, colors, current_citeria, citerias):
    i = 0
    for citeria in citerias:
        if citeria != current_citeria:
            for cnt, df_of_quality in enumerate(df_of_qualities):
                axs[i].scatter(x=df_of_quality[current_citeria], y=df_of_quality[citeria],\
                    alpha=0.5, color=[colors[cnt]], s=10)
                axs[i].set_title(citeria)
                axs[i].set_xlabel(f"Value of {current_citeria}")
                axs[i].set_ylabel(f"Value of {citeria}")
            i += 1


def save_all():
    global images

    images = []
    num_citerias = len(citerias) - 1
    ncols = int(num_citerias ** 0.5) + 1
    nrows = (num_citerias - 1) // ncols + 1
    colors = sns.color_palette("tab10", n_colors=len(qualities))
    custom_lines = [[qualities[i], (Line2D([0], [1], color=colors[i], lw=16))] for i in range(len(colors))]
    custom_lines = sorted(custom_lines, key=lambda x: x[0])
    custom_lines = [line[1] for line in custom_lines]

    for citeria in citerias:
        fig, axs = plt.subplots(ncols=ncols, nrows=nrows, figsize=(15, 12))
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)
        axs = axs.flatten()
        fig.suptitle(f"{citeria} with:", fontsize=25)
        display_quality(fig, axs, colors, citeria, citerias)
        for j in range(len(citerias) - 1, len(axs)):
            fig.delaxes(axs[j])
        fig.legend(custom_lines, sorted(qualities),\
                fontsize='x-large', loc='lower right', ncol=2, bbox_to_anchor=(1, 0),\
                handlelength=4.5, handleheight=3.5, borderpad=1.0)
        plt.tight_layout(rect=[0, 0.1, 1, 1])
        buf = BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        images.append(mpimg.imread(buf))
        plt.close()


def display_with_key():
    global ax
    global current_citeria_index

    current_citeria_index %= (len(citerias))
    ax.clear()
    ax.imshow(images[current_citeria_index])
    ax.axis('off')
    plt.draw()


def on_key(event):
    global current_citeria_index
    global fig

    if event.key == 'left':
        current_citeria_index -= 1
        display_with_key()
    elif event.key == 'right':
        current_citeria_index += 1
        display_with_key()
    elif event.key == 'escape':
        plt.close(fig)

def main():
    global qualities
    global df_of_qualities
    global citerias
    global ax
    global fig
    global df
    global qualities
    
    df = pd.read_csv("winequality-red.csv", sep=';')

    citerias = df.columns

    qualities = np.unique(df[np.array(df.columns)[-1]])

    linked_qualities_df = [[int(quality), df[df.values[:, -1] == quality]] for quality in qualities]
    linked_qualities_df = sorted(linked_qualities_df, key=lambda x: len(x[1]))[::-1]
    qualities = [item[0] for item in linked_qualities_df]

    df_of_qualities = [item[1] for item in linked_qualities_df]

    save_all()
    fig, ax = plt.subplots(figsize=(15,12))
    fig.canvas.mpl_connect('key_press_event', on_key)
    display_with_key()
    plt.show()
    

if __name__ == "__main__":
    main()
