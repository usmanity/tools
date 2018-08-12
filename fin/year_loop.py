def yearLoop(startPrice, gainer, years = 1):
  price = startPrice
  print("Start price: %d" % startPrice)
  print("Change per month (percentage): %.2f" % gainer);
  for i in range(1, 12 * years):
    print("For month %d, price is %.2f" % (i, price))
    price = price + (price * gainer / 100.0)
  print("Started with %.2f, ended with %.2f, difference of %.2f" % (startPrice, price, price - startPrice))
  return price

input_price  = int(input("What's your start amount? "))
input_gainer = float(input("What percentage are you moving per month? "))
input_years  = int(input("How many years? "))

yearLoop(input_price, input_gainer, input_years)
