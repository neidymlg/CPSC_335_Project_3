# gives list of coins we can use, and amount of the actual change
def coin_change(coins, amount):
    #makes an array that is the size of amount and fills with None
    coin_combo = [None] * (amount + 1)

    #if we have no change, return 0 monetary amount, 0 amount of coins
    #else make a list to carry the coins combos
    if(amount == 0):
        return None, 0
    else: 
        coin_combo[0] = list()

    #iterate from 0 to amount
    #it will attempt to add a value to the array if the previous value is not None, 
    #the value is empty (None)
    #it will only add in coins that are greater or equal to the current value (0, 1, 2.. etc)
    #it will add a combo of coins at the very end that equal to the amount,
    #if the coins are greater or not equal to the amount, the end will be None
    for i in range(1, amount + 1):
        for denom in coins:
            if i >= denom and coin_combo[i - denom] is not None:
                candidate = coin_combo[i-denom] + [denom]
                if coin_combo[i] is None or len(candidate)  < len(coin_combo[i]):
                    coin_combo[i] = candidate

    #if there is no solution  (None), return no solution
    #used when coins is empty [], or when coins cannot equal amount
    if(coin_combo[amount] == None):
        return None, 0
    else:
        return coin_combo[amount], len(coin_combo[amount])

amount = 11
coins = [1, 2, 5]
combo, num_of_coins= coin_change(coins, amount)
print(f'Coins used: {combo}  \nNumber of coins used: {num_of_coins}')