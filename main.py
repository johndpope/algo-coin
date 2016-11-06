from trading import TradingEngine
from custom_strategies import SMACrossesStrategy


def main():
    # Instantiate trading engine
    #
    # The engine is responsible for managing the different components,
    # including the strategies, the bank/risk engine, and the
    # exchange/backtest engine.
    te = TradingEngine(live=False,
                       sandbox=False,
                       backtest=True,
                       verbose=False,
                       bt_file="/Volumes/MacintoshHD/theocean154/"
                               "Dropbox/Unsorted/cs/bitcoin/"
                               "krakenUSD.csv")

    # A sample strategy that impelements the correct interface
    ts = SMACrossesStrategy(10, 5)

    # Register the strategy with the Trading engine
    te.registerStrategy(ts)

    # Run the live trading engine
    te.run()

if __name__ == '__main__':
    main()