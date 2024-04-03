# ---------------------------------------------------
# Plots histograms for information transference
# -------------- ------------------------------------

# libraries
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import time


def get_data(varname, index):
    """
    Import data for a given variable and index
    Input: varname : str, index : str
    Return: df : DataFrame
    """

    # import nc file
    DS = xr.open_dataset("col-inf-transf-data/T-percent/T_" + index + "_" + varname + ".nc")
    ds = DS.to_dataframe()
    arr = ds["tau21"].to_numpy()

    return arr


def plot_hist_from_data(index_name, var_name, save=False):

    data = get_data(var_name, index_name)

    titles = {
        "car": "a",
        "nino3": "e",
        "nino34": "d",
        "soi": "f",
        "tna": "b",
        "nta": "c",
    }
    title = titles[index_name]

    # plot histogram

    sns.set(
        style="ticks",  # The 'ticks' style
        rc={
            "figure.figsize": (9, 6),  # width = 6, height = 9
            "figure.facecolor": "white",  # Figure colour
            "axes.facecolor": "white",
        },
    )  # Axes colour# Box plot

    b = sns.histplot(
        data,
        bins=25,
        stat="probability",
        color="gray",
        edgecolor="black",
        linewidth=1.5,
        alpha=0.8,
    )

    if index_name == "nino34" or index_name == "car":
        b.set_ylabel(
            r"$\rho$", fontsize=26, weight="bold"
        )  # Set the x axis label and font size
    else:
        b.set_ylabel(
            " ", fontsize=26, weight="bold"
        )  # Set the x axis label and font size

    if index_name == "nino3":
        b.set_xlabel(
            '\n'+r'$\tau_{Y \rightarrow %s }$ ' % var_name.upper() + r'$(\%)$', fontsize=26, weight="bold"
        )  # Set the x axis label and font size
    else:
        b.set_xlabel(
            '\n', fontsize=26, weight="bold"
        )  # Set the x axis label and font size

    b.xaxis.set_tick_params(labelsize=24)
    b.yaxis.set_tick_params(labelsize=24)
 
    # Remove axis spines
    sns.despine(offset=5, trim=True)

    plt.tight_layout()

    if save:
        plt.savefig("hist-inf-transf/tau_" + index_name + "_" + var_name +"_hist.png")

    #plt.show()
    plt.clf()

    return True


if __name__ == "__main__":

    indexes = ["car", "nino3", "nino34", "nta", "soi", "tna"]
    vars = ["tp", "t2m", "vimflux"]

    for index in indexes:
        for var in vars:
            plot_hist_from_data(index, var, True)
            time.sleep(2)

