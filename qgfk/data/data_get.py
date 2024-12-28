import tushare as ts
import pandas as pd

# 初始化 Tushare
pro = ts.pro_api('20241217202523-6dc513df-e2f2-4ab8-8dfd-038be46b739c')
pro._DataApi__http_url = 'http://tsapi.majors.ltd:7000'

def get_stock_data(stock_code, start_date, end_date):
    """
    获取指定股票的历史数据
    """
    data = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    data = data[['trade_date', 'open', 'high', 'low', 'close', 'vol']]
    data['trade_date'] = pd.to_datetime(data['trade_date'])
    return data

