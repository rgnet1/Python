

# Input: cents
# Goal: Determine min number of coins and coin type needed to get to cents
# EX: 33 Cents = 1 qarter, 1 nickel, 3 pennies

def coins(cents):
    result = {
        25:0,
        10:0,
        5:0,
        1:0,
        'coin_count':0,
    }

    coin_values = [25, 10, 5, 1]
    for value in coin_values:
        while(cents >= value):
            result[value] +=1
            cents -=value
            result['coin_count'] +=1
    return result

# Gets number of coins based on cents and availble coins
def coins_optimized(cents, coins_available):
    result = {
        25:0,
        10:0,
        5:0,
        1:0,
        'coin_count':0,
    }

    coin_values = [25, 10, 5, 1]
    for value in coin_values:
        if coins_available[value] == 0 :
            continue
        coin_count = int(cents / value)
        
        exising_coins = coins_available[value]
        if exising_coins < coin_count:
            coin_count -= exising_coins
            cents -= (coin_count * value)

        result[value] = coin_count
        coins_available[value] -= coin_count
        result['coin_count'] += coin_count 
        cents = cents % value
    
        if cents == 0:
            break
            

    return result


coins_available = {
        25:0,
        10:100,
        5:50,
        1:35,
}
print(coins_optimized(138, coins_available))
print("Remaining coins available:", coins_available)
