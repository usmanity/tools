while(True):
        stock_price = float(raw_input('Stock price: '))
        dividend_per_month = float(raw_input('Dividend per month, in cents: '))

        ppm = dividend_per_month / stock_price

        print("%.2f" % ppm)

