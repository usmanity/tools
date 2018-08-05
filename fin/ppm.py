while(True):
        stock_price = float(input('Stock price: '))
        dividend_per_month = float(input('Dividend per month, in cents: '))

        ppm = dividend_per_month / stock_price

        print("%.2f" % ppm)

