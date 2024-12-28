import tushare as ts
import pandas as pd
from data.data_get import *
from strategy.strategy_ma import *
from backtest.backtest_1 import *
import matplotlib.pyplot as plt
import os


def main(path_name: str):
    # 1. 获取股票数据
    stock_code = '000001.SZ'  # 以平安银行为例
    start_date = '20230101'
    end_date = '20231231'

    # 获取历史股票数据
    stock_data = get_stock_data(stock_code, start_date, end_date)

    # 2. 应用策略：简单的移动平均交叉策略
    stock_data = simple_ma_strategy(stock_data, short_window=5, long_window=20)

    # 3. 运行回测
    backtest = Backtest(stock_data, initial_capital=100000)
    backtest.run()

    # 4. 绘制回测结果
    plot_results(stock_data)

    # 5. 导出回测结果
    export_to_csv(stock_data,path_name)


def plot_results(data):
    """
    绘制股价、短期和长期均线
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['trade_date'], data['close'], label='Close Price')
    plt.plot(data['trade_date'], data['short_ma'], label='Short MA', alpha=0.7)
    plt.plot(data['trade_date'], data['long_ma'], label='Long MA', alpha=0.7)
    plt.legend()
    plt.title("Stock Price and Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.show()


def export_to_csv(data, path_name):
    # 设置保存的文件路径，文件名为 'tushare_data.xlsx'
    file_path = os.path.join(path_name, 'tushare_data.csv')

    # 导出数据为Excel
    data.to_csv(file_path, index=False)
    print(f"Data has been exported to {file_path}")


if __name__ == "__main__":
    main(r'C:\Users\S_YZ\OneDrive\桌面')

print(1)
