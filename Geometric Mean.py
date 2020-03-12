endPrice = 313.6
startPrice = 153
interest = 0.06741909042
# Bruteforcing using for loop algorithm.
currentPrice = startPrice
for i in range(0, 11):
    currentPrice = (currentPrice * interest) + currentPrice
    print(currentPrice)

currentPrice = round(currentPrice, 4)

if(currentPrice == endPrice):
    print(
        f"The predicted price: {endPrice} and the final price {currentPrice} is correct!")

# Geometric Mean formula:
# GM = ((n-1) root of valueEnd/valueStart) - 1
# valueEnd = value at the end of the period.
# valueStart = value at the start of the period.
