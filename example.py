import okex.account_api as account
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot
import okex.swap_api as swap
import okex.index_api as index
import okex.option_api as option
import okex.system_api as system
import okex.information_api as information
import json
import datetime
import time

def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

times = get_timestamp()

if __name__ == '__main__':

    api_key = "dead719e-f3ed-49d0-b332-b22bc5759b57"
    secret_key = "52E95D0FEA84700FFE58060B5E39E1B9"
    passphrase = "577588"

    # param use_server_time's value is False if is True will use server timestamp
    # param test's value is False if is True will use simulative trading

# account api test
# 资金账户API
    accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False)
    # 资金账户信息
    # result = accountAPI.get_wallet()
    # 单一币种账户信息
    # result = accountAPI.get_currency('')
    # 资金划转
    # result = accountAPI.coin_transfer(currency='', amount='', account_from='', account_to='', type='', sub_account='', instrument_id='', to_instrument_id='')
    # 提币
    # result = accountAPI.coin_withdraw(currency='', amount='', destination='', to_address='', trade_pwd='', fee='')
    # 账单流水查询
    # result = accountAPI.get_ledger_record(currency='', after='', before='', limit='', type='')
    # 获取充值地址
    # result = accountAPI.get_top_up_address('')
    # 获取账户资产估值
    # result = accountAPI.get_asset_valuation(account_type='', valuation_currency='')
    # 获取子账户余额信息
    # result = accountAPI.get_sub_account('')
    # 查询所有币种的提币记录
    # result = accountAPI.get_coins_withdraw_record()
    # 查询单个币种提币记录
    # result = accountAPI.get_coin_withdraw_record('')
    # 获取所有币种充值记录
    # result = accountAPI.get_top_up_records()
    # 获取单个币种充值记录
    # result = accountAPI.get_top_up_record(currency='', after='', before='', limit='')
    # 获取币种列表
    # result = accountAPI.get_currencies()
    # 提币手续费
    # result = accountAPI.get_coin_fee('')

# spot api test
# 币币API
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    # 币币账户信息
    account_info = spotAPI.get_account_info()
    # 单一币种账户信息
    mana_json = spotAPI.get_coin_account_info('mana')
    hc_json = spotAPI.get_coin_account_info('hc')
    # 账单流水查询
    # result = spotAPI.get_ledger_record(currency='', after='', before='', limit='', type='')
    # 下单
    # result = spotAPI.take_order(instrument_id='', side='', client_oid='', type='', size='', price='', order_type='0', notional='')
    # 批量下单
    # result = spotAPI.take_orders([
    #     {'instrument_id': '', 'side': '', 'type': '', 'price': '', 'size': ''},
    #     {'instrument_id': '', 'side': '', 'type': '', 'price': '', 'size': ''}
    # ])
    # 撤销指定订单
    # result = spotAPI.revoke_order(instrument_id='', order_id='', client_oid='')
    # 批量撤销订单
    # result = spotAPI.revoke_orders([
    #     {'instrument_id': '', 'order_ids': ['', '']},
    #     {'instrument_id': '', 'order_ids': ['', '']}
    # ])
    # 获取订单列表
    # result = spotAPI.get_orders_list(instrument_id='', state='', after='', before='', limit='')
    # 获取所有未成交订单
    # result = spotAPI.get_orders_pending(instrument_id='', after='', before='', limit='')
    # 获取订单信息
    # result = spotAPI.get_order_info(instrument_id='', order_id='', client_oid='')
    # 获取成交明细
    # result = spotAPI.get_fills(instrument_id='', order_id='', after='', before='', limit='')
    # 委托策略下单
    # result = spotAPI.take_order_algo(instrument_id='', mode='', order_type='', size='', side='', trigger_price='', algo_price='', algo_type='')
    # 委托策略撤单
    # result = spotAPI.cancel_algos(instrument_id='', algo_ids=['',''], order_type='')
    # 获取当前账户费率
    # trade_fee = spotAPI.get_trade_fee()
    # 获取委托单列表
    # result = spotAPI.get_order_algos(instrument_id='', order_type='', status='', algo_id='', before='', after='', limit='')
    # 公共-获取币对信息
    # result = spotAPI.get_coin_info()
    # 公共-获取深度数据
    # result = spotAPI.get_depth(instrument_id='', size='', depth='')
    # 公共-获取全部ticker信息
    # result = spotAPI.get_ticker()
    # 公共-获取某个ticker信息
    # result = spotAPI.get_specific_ticker('')
    # 公共-获取成交数据
    # result = spotAPI.get_deal(instrument_id='', limit='')
    # 公共-获取K线数据
    # result = spotAPI.get_kline(instrument_id='', start='', end='', granularity='')
    # 公共-获取历史K线数据
    # result = spotAPI.get_history_kline(instrument_id='', start='', end='', granularity='')


# information api test
# 合约交易数据API
    informationAPI = information.InformationAPI(api_key, secret_key, passphrase, False)
    # 公共-多空持仓人数比
    # result = informationAPI.get_long_short_ratio(currency='', start='', end='', granularity='')
    # 公共-持仓总量及交易量
    # result = informationAPI.get_volume(currency='', start='', end='', granularity='')
    # 公共-主动买入卖出情况
    # result = informationAPI.get_taker(currency='', start='', end='', granularity='')
    # 公共-多空精英趋向指标
    # result = informationAPI.get_sentiment(currency='', start='', end='', granularity='')
    # 公共-多空精英平均持仓比例
    # result = informationAPI.get_margin(currency='', start='', end='', granularity='')

# index api test
# 指数API
    indexAPI = index.IndexAPI(api_key, secret_key, passphrase, False)
    # 公共-获取指数成分
    # HC_USD = indexAPI.get_index_constituents('HC-USD')

# system api test
# 获取系统升级状态
    system = system.SystemAPI(api_key, secret_key, passphrase, False)
    # 公共-获取系统升级状态
    # result = system.get_system_status('')
    print(json.dumps(account_info))
    # xx = json.dumps(mana_json)
    print(mana_json['frozen'])
    print(mana_json['currency'])

    print(json.dumps(hc_json))

while 1:
    try:
        BTC_USD = indexAPI.get_index_constituents('BTC-USD')
        print('BTC-USD '+ BTC_USD['data']['last'])
        MANA_USD = indexAPI.get_index_constituents('MANA-USD')
        print('MANA_USD ' + MANA_USD['data']['last'])
        time.sleep(1)
    except IOError:
        print(IOError)
    else:
        time.sleep(1)

    # print(json.dumps(trade_fee))

    # print(time + json.dumps(result2))

