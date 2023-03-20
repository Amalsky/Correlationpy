import csv
import statistics

# data source = https://finance.yahoo.com/

def correlation(dataz, price):
    """
    Calculates the daily returns of a stock using its opening price and
    returns a list of the dispersion of those returns from the mean.

    Args:
    dataz (file object): A csv file containing daily closing prices of a benchmark index
    price (float): The opening price of the stock for which the daily returns are to be calculated

    Returns:
    list: A list of the dispersion of daily returns of the stock from the mean
    """
    bench_mark_daily_return = []
    bench_mark_dispersion = []
    stock_name_daily_return = []
    index1 = 0
    index_for_dispersion = 0
    stock1 = price
    stock1_average_daily_return = 0
    data = csv.reader(dataz)
    next(data)  # skip header row
    for line in data:
        if index1 >= 1:
            closing = float(line[4])
            daily_return = closing / stock1 - 1
            bench_mark_daily_return.append(daily_return)

            # Finding average return
            stock1_average_daily_return = sum(bench_mark_daily_return) / len(bench_mark_daily_return)
            stock1 = closing

        index1 += 1

    # Finding dispersion
    for line in bench_mark_daily_return:
        dispersion = line - stock1_average_daily_return
        bench_mark_dispersion.append(dispersion)
        index_for_dispersion += 1

    # finding std
    std = statistics.stdev(bench_mark_daily_return)
    std_stock = std * 15.8113883

    return bench_mark_dispersion

def co(dataset1, data2):
    """
    Calculates the correlation coefficient between a stock and a benchmark index.

    Args:
    dataset1 (list): A list of the dispersion of daily returns of a benchmark index
    data2 (list): A list of the dispersion of daily returns of a stock

    Returns:
    float: The correlation coefficient between the benchmark index and the stock
    """
    index = 0
    dispersion_multiplayer = []
    for line in dataset1:
        result = line * data2[index]
        result = result * 100
        index += 1
        dispersion_multiplayer.append(result)

    count = len(dispersion_multiplayer) - 1
    covariance = sum(dispersion_multiplayer) / count

    std_benchmark = statistics.stdev(dataset1) * 15.8113883
    std_stock = statistics.stdev(data2) * 15.8113883

    final_result = covariance / (std_benchmark * std_stock)

    return final_result


with open('nifty.csv') as bench_mark, open('reliance.csv') as stock_name:
    bm_daily_returns = correlation(bench_mark, 17117.599609)
    sn_daily_returns = correlation(stock_name, 2467.399902)

    correlation_coefficient = co(bm_daily_returns, sn_daily_returns)

    print(correlation_coefficient)
