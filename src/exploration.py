import matplotlib.pyplot as plt
import seaborn as sns


def distribution_visualization(series):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    sns.distplot(series.dropna(), kde=False, ax=ax)
    ax.set_title(series.name)
    plt.show()
