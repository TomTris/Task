from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fig = None

def display_all(citerias, df):
    global fig

    num_citerias = len(citerias)
    ncols = int(num_citerias ** 0.5) + 1
    nrows = (num_citerias - 1) // ncols + 1
    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, 12))
    fig.suptitle("Distribution of Each Attribute by Wine Quality", fontsize=25)

    ncol = -1
    nrow = 0

    for cnt, citeria in enumerate(citerias):
        g = sns.catplot(x='quality', y=citeria, data=df, kind='violin', palette='Reds', height=4, aspect=1.5)
        g.fig.suptitle(f"Distribution of {citeria} by Wine Quality", fontsize=16)
        buf = BytesIO()
        g.savefig(buf)
        buf.seek(0)
        plt.close(g.fig)

        ncol += 1
        if ncol == ncols:
            ncol = 0
            nrow += 1
        img = plt.imread(buf)
        ax = axs[cnt // ncols, cnt % ncols]
        ax.imshow(img)
        ax.axis('off')

    axs = axs.flatten()
    for j in range(len(citerias), len(axs)):
        fig.delaxes(axs[j])
    plt.tight_layout(rect=[0, 0, 1, 0.95])

def on_key(event):
    global fig

    if event.key == 'escape':
        plt.close(fig)

name = "winequality-red.csv"

def main():
    global fig
    
    df = pd.read_csv("winequality-red.csv", sep=';')

    citerias = df.columns[0:-1]
    display_all(citerias, df)
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()
    

if __name__ == "__main__":
    main()

