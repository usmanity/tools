stock_price = float(raw_input('Stock price: '))
dividend_per_month = float(raw_input('Dividend per month: '))

ppm = dividend_per_month / stock_price * 100

print("%.2f" % ppm)
