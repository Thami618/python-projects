

bids = {}
bidding_finished = False



def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount  = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f" the winner is {winner} with bid of {highest_bid}")

while not bidding_finished:
    name = input("What is your name")
    price = int(input("Whats your Bid: $"))
    bids[name] = price
    should_continue = input("Are there any biders?")

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)


