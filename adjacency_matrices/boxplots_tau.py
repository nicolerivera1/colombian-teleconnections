# libraries
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_variables_all_indexes(
    varname, indexlist=["car", "nino3", "nino34", "nta", "soi", "tna"]
):
    """
    Imports all indexes tau for a given variable
    Input: varname : srt, indexlist : list
    Return: df : DataFrame
    """

    all_indexes = []

    for index in indexlist:
        # import nc file
        DS = xr.open_dataset("col-inf-transf-data/T_" + index + "_" + varname + ".nc")
        ds = DS.to_dataframe()
        ds.rename(columns={"tau21": index.upper()}, inplace=True)
        ds[index.upper()] *= 100  # to %
        all_indexes.append(ds)

    df = pd.concat(all_indexes, axis=1)

    return df


# function to plot distributions


def all_variables_boxplot(df, title, save_fig=False):
    # Change some of seaborn's style settings with `sns.set()`
    sns.set(
        style="ticks",  # The 'ticks' style
        rc={
            "figure.figsize": (9, 6),  # width = 6, height = 9
            "figure.facecolor": "white",  # Figure colour
            "axes.facecolor": "white",
        },
    )  # Axes colour# Box plot

    b = sns.boxplot(
        x="variable",  # takes all columns
        y="value",  # distribute its frecuency
        data=pd.melt(df),  # specify data
        width=0.4,  # The width of the boxes
        linewidth=2,  # Thickness of the box lines
        showfliers=True,
        palette="flare",
    )

    b.set_ylabel(
        "Relative Information Flow (%)", fontsize=14, weight="bold"
    )  # Set the x axis label and font size
    b.set_xlabel(
        "Index", fontsize=14, weight="bold"
    )  # Set the plot title with the pval variable and font size
    # b.set_title("\n" + title, fontsize=16)
    # b.set_xticklabels(['CAR', 'NINO3', 'NINO3.4', 'NTA', 'SOI', 'TNA'])

    # Remove axis spines
    sns.despine(offset=5, trim=True)

    plt.tight_layout()

    if save_fig:
        fig = b.get_figure()
        fig.savefig("imgs/tau_" + title.replace(" ", "_").lower() + ".png")

    #plt.show()
    plt.clf()

    return True


if __name__ == "__main__":

    vars = ["tp", "t2m", "vimflux"]
    titles = {
        "tp": "Total Precipitation",
        "t2m": "Two-meter Temperature",
        "vimflux": "Vertical Moisture Convergence",
    }

    for name in vars:
        df_var = get_variables_all_indexes(name)
        all_variables_boxplot(df_var, titles[name] + " (" + name.upper() + ")", True)
