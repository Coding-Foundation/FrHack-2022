import matplotlib.pyplot as plt

def savePlotofVector(vec, filename, dataset, title="", color="b", save=True):
    plt.figure(figsize=(30, 4))
    plt.bar(range(len(vec)), vec, color=color)
    plt.xticks(range(len(vec)), dataset.X_week_labels(), rotation=90, fontsize=20)
    plt.title(title)
    if save:
        plt.savefig(f'{filename}.png', bbox_inches="tight", dpi=300)
    plt.show()

def show7dayFromDatetime(dataset, sonde:str, i_datetime):
    select = dataset.measure_df[(dataset.measure_df["numero"]==sonde) & (dataset.measure_df["datetime"]>=i_datetime)].iloc[:12*7]
    vec = select["E_volt_par_metre"].iloc[:12*7].to_numpy()
    labels = tuple(select["date"])
    
    plt.figure(figsize=(30, 4))
    plt.bar(range(len(vec)), vec, color="g")
    plt.xticks(range(len(vec)), labels, rotation=90, fontsize=20)
    plt.title("")
    plt.show()