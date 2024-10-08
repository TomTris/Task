import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def display_quality(axs, citerias, df):
    for cnt, citeria in enumerate(citerias):
        sns.barplot(x='quality', y=citerias[cnt], data=df, palette='Reds', errorbar=None, ax=axs[cnt], legend=False)
        axs[cnt].set_title(citeria)
        axs[cnt].set_xlabel(f"Value of wine quality")
        axs[cnt].set_ylabel(f"Value of {citeria}")

def save_all(citerias, df):
    global fig

    num_citerias = len(citerias) - 1
    ncols = int(num_citerias ** 0.5) + 1
    nrows = (num_citerias - 1) // ncols + 1
    fig, axs = plt.subplots(ncols=ncols, nrows=nrows, figsize=(15, 12))
    axs = axs.flatten()
    fig.suptitle(f"Avarage value of each attribute by Wine Quality", fontsize=25)
    display_quality(axs, citerias, df)
    for j in range(len(citerias), len(axs)):
        fig.delaxes(axs[j])
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def on_key(event):
    global fig

    if event.key == 'escape':
        plt.close(fig)

name = "winequality-red.csv"

def main():
    global fig

    df = pd.read_csv("winequality-red.csv", sep=';')

    citerias = df.columns[0:-1]
    save_all(citerias, df)
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()
    

if __name__ == "__main__":
    main()

