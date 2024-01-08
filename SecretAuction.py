import bids

print('''
                              ___________
                              \         /
                               )_______(
                               |"""""""|_.-._,.---------.,_.-._
                               |       | | |               | | ''-.
                               |       |_| |_             _| |_..-'
                               |_______| '-' `'---------'` '-'
                               )"""""""(
                              /_________\\
                            .-------------.
                           /_______________\\
     ''')
#import os

print("Welcom to the secret auction program.")
should_end = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # biddind_record = {"Dalya": 123, "Saja": 321}
    #erste runde ist bidder == Dalya und zweite runde ist bidder == Saja
    for bidder in bidding_record:
        # bidding_record[(key)->Dalya]
        bid_amount = bidding_record[bidder]
        #erste runde: if 123 is greater than 0
        #zweite runde: if 321 is greater than 123
        if bid_amount > highest_bid:
            #erste runde: highest_bid is now 123
            #zweite runde: highest_bid is now 321
            highest_bid = bid_amount
            winner += bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not should_end:
    name = input("What is your name?: ").lower()
    price = int(input("What is yor bid?: $"))
    #dictionary bids:{price}
    bids[name] = price
    other_biddes = input("Are there any other bidders? type 'yes' or 'no': ").lower()
    if other_biddes == "no":
        should_end = True
        find_highest_bidder(bids="find_highest_bidder")







