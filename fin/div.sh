TICKER=$1

./get_yahoo_fin_quote.sh ${TICKER} | python3 dividend_schedule.py
