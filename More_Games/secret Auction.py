logo = '''
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
'''

def highest_bid(bid_record):
    high_bid = 0
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount>high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner) with the highest bid ${high_bid}")

auction = {}
bid = True
while bid == True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    auction[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "yes":
        bid = True
    else:
        break
highest_bid(bid_record=auction)


