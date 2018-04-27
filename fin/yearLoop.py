def yearLoop(startPrice, gainer):
  price = startPrice
  print("Start price: ", startPrice)
  print("Change per month (percentage): ", gainer);
  for i in range(1, 12):
    print("For month %d, price is %d" % (i, price))
    price = price + (price * gainer / 100.0)
  print("Started with %d, ended with %d, difference of %d" % (startPrice, price, price - startPrice))
  return price

input_price = input("What's your start amount? ")
input_gainer = input("What percentage are you moving per month? ")

yearLoop(input_price, input_gainer)
