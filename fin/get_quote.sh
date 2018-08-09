TICKER=$1

./curl_quote_data.sh $TICKER | python3 quote.py
