import warnings

warnings.filterwarnings("ignore")
import pandas as pd
from matplotlib import animation
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = (20, 3)


def plot_daily(*dfs, index=None, save=None):
    if index is not None:
        dfs = [pd.Series(df, index=index) for df in dfs]
    plt.ioff()
    fig = plt.figure()
    plt.ion()
    max_y = max((df.max() for df in dfs))
    xlim = (dfs[0].index.time.min(), dfs[0].index.time.max())
    ax = plt.axes(ylim=(0, max_y), xlim=xlim)
    len_df = len(set(dfs[0].index.date))
    lines = [ax.plot([], [], "o-", lw=2)[0] for _ in dfs]
    df_days = [df.groupby(pd.Grouper(freq="D")) for df in dfs]
    time_text = ax.text(0.05, 0.9, "", transform=ax.transAxes)

    def init():
        for line in lines:
            line.set_data([], [])
        time_text.set_text("")
        return lines + [time_text]

    def update(df):
        for df_day, line in zip(df, lines):
            line.set_data(df_day[1].index.time, list(df_day[1]))
        time_text.set_text(df[0][0].strftime("%b %Y"))
        return lines + [time_text]

    anim = animation.FuncAnimation(
        fig,
        update,
        frames=zip(*df_days),
        init_func=init,
        blit=True,
        interval=50,
        save_count=len_df,
    )

    if save:
        anim.save(save)
    return anim


if __name__ == "__main__":
    from dataset import suny_international

    plot_daily(suny_international.load_data()["GHI"], save="media/plot_simple.mp4")
