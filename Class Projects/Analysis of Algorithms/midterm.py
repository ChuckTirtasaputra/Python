# Chuck Tirtasaputra
global cache
cache = {0:0}
price = [1, 2, 5, 19, 20]
card = 6
print(price)

n = len(price)

# the fuction returns the amount left on the card
def bta(n, card, price):
    # if there are no items or money on the card, you cannot buy anything
    if (n == 0) or (card == 0):
        return 0
    else:
        # loop through the prices of the items 
        for i in range(0, n-1):
            ''' golden step: should be trying to choose whether to buy the item
            or to choose the next item in the list, but making sure that it stays
            within the amount on the card. I am not sure how to account of skipping 
            items like my example would need to buy the 1st and 3rd item. 
            Instead, it only buys the 1st and 2nd item. 
            '''
            cache[i] = max(card-price[i+1], card-price[i])
            card = cache[i]
            # checking if its within the amount on the card
            if card < 0:
                return cache[i-1]
            else:
                continue
        return cache[i]

if bta(n, card, price) == 0:
    print("Can buy exact amount on giftcard")
if bta(n, card, price) > 0:
    print("Cannot buy exact amount on giftcard. Have $", bta(n, card, price), "left on the card")

'''
I am not sure how to account of skipping items like my example 
would need to buy the 1st and 3rd item. Instead, it only buys 
the 1st and 2nd item. 
'''