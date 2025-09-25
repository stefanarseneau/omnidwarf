import matplotlib.pyplot as plt
import pandas as pd

def plot(data):
    fig, ax = plt.subplots(ncols=1, figsize=(16, 8))
    ax.scatter(data.teff*1e-3, 109.75*data.radius, c = 'white', edgecolor = 'k')
    ax.set_xlabel('$T_\\text{eff}$ [kK]')
    ax.set_ylabel('Radius $[R_\\oplus]$')
    ax.invert_xaxis()

    plt.show()

if __name__ == "__main__":
    data = pd.read("summary.pqt")
    plot(data)
