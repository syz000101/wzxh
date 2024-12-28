import numpy as np


class Backtest:
    def __init__(self, data, initial_capital=1000000):
        """
        初始化回测引擎
        """
        self.data = data  # 股票历史数据
        self.initial_capital = initial_capital  # 初始资金
        self.cash = initial_capital  # 可用现金
        self.position = 0  # 当前持仓
        self.capital = initial_capital  # 总资产
        self.transaction_cost = 0.0005  # 假设交易费用为千分之一

    def run(self):
        """
        执行回测
        """
        for i in range(1, len(self.data)):
            # 获取今天的价格和信号
            today_price = self.data.iloc[i]['close']
            signal = self.data.iloc[i]['signal']

            # 如果信号为买入，且没有持仓
            if signal == 1 and self.position == 0:
                # 买入股票，使用全部资金
                self.position = self.cash / today_price * (1 - self.transaction_cost)
                self.cash = 0
                print(f"买入股票，价格：{today_price}, 当前资金：{self.cash}, 持仓：{self.position}")

            # 如果信号为卖出，且有持仓
            elif signal == -1 and self.position > 0:
                # 卖出股票
                self.cash = self.position * today_price * (1 - self.transaction_cost)
                self.position = 0
                print(f"卖出股票，价格：{today_price}, 当前现金：{self.cash}, 持仓：{self.position}")

            # 计算总资产（现金 + 当前持仓的市值）
            self.capital = self.cash + self.position * today_price

        print(f"回测结束，总资产：{self.capital}")