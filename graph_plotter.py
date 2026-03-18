import matplotlib.pyplot as plt


class GraphPlotter:

    def __init__(self, ticker_name, plot_df):
        self._ticker_name = ticker_name
        self._plot_df = plot_df


    def graph_displayment(self):
        x_axis = self._plot_df['index']
        y_axis_prices = self._plot_df['actual']
        y_axis_trend_line = self._plot_df['trend']

        plt.plot(x_axis, y_axis_prices, label="Actual Price")
        plt.plot(x_axis, y_axis_trend_line, linestyle='--', label="Trend Line")

        #labeling the axes
        plt.xlabel("Trading Days")
        plt.ylabel("Closing Price(USD)")

        #title
        plt.title(f"{self._ticker_name} Stock Price & Trend")
        plt.legend()
        plt.show()

