

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


def coins_optimized(cents):
    result = {
        25:0,
        10:0,
        5:0,
        1:0,
        'coin_count':0,
    }

    coin_values = [25, 10, 5, 1]
    for value in coin_values:
        coin_count = int(cents / value)
        cents = cents % value
        result[value] = coin_count
        result['coin_count'] += coin_count
        if cents == 0:
            break
    return result

print(coins_optimized(138))

