import numpy as np


def simple_ma_strategy(data, short_window=5, long_window=20):
    """
    简单的移动平均交叉策略
    """
    # 计算短期和长期移动平均
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()

    # 生成买入和卖出信号
    data['signal'] = 0
    data.loc[short_window:, 'signal'] = np.where(data['short_ma'][short_window:] > data['long_ma'][short_window:], 1, -1)

    return data