import matplotlib.pyplot as plt

def savePlotofVector(vec, filename, dataset, title="", color="b"):
    plt.figure(figsize=(30, 4))
    plt.bar(range(len(vec)), vec, color=color)
    plt.xticks(range(len(vec)), dataset.X_week_labels(), rotation=90, fontsize=20)
    plt.title(title)
    plt.savefig(f'{filename}.png', bbox_inches="tight", dpi=300)
    plt.show()