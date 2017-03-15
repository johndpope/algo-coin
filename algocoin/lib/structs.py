import datetime
from .enums import Side, \
                   CurrencyType, \
                   OrderType, \
                   OrderSubType, \
                   ExchangeType, \
                   TickType
from .utils import struct, NOPRINT


@struct
class MarketData:
    # common
    time = datetime.datetime, NOPRINT
    volume = float
    price = float
    type = TickType
    currency = CurrencyType, CurrencyType.BTC
    side = Side

    # maybe specific
    remaining = float, float('nan')
    reason = str, ''
    sequence = int, -1
    order_type = OrderType, OrderType.NONE


@struct
class TradeRequest:
    data = MarketData, NOPRINT
    side = Side

    volume = float
    price = float
    currency = CurrencyType, CurrencyType.BTC, NOPRINT

    order_type = OrderType, OrderType.MARKET
    order_sub_type = OrderSubType, OrderSubType.NONE
    # exchange = ExchangeType

    risk_check = bool, False
    risk_reason = str, ''


@struct
class TradeResponse:
    data = MarketData, NOPRINT
    request = TradeRequest
    side = Side

    volume = float
    price = float
    currency = CurrencyType, CurrencyType.BTC

    slippage = float, 0.0
    transaction_cost = float, 0.0

    success = bool


@struct
class Account:
    currency = CurrencyType
    balance = float
    id = str

    def __repr__(self):
        return "<" + self.id + " - " + \
              str(self.currency) + " - " + str(self.balance) + ">"