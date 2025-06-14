import art

print(art.logo)
bid_start =True
auction_data = {}
while bid_start:
    print("Welcome to secret auction program.")
    key= input("What is your name ?")
    value = int(input("What is your bid ?"))
    auction_data[key]=value
    next_bid = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if next_bid =="yes":
        print(100 * "\n")
    elif next_bid =="no":
        bid_start=False
        winner_bid = max(auction_data.values())
        winner_name =""
        for i in auction_data:
            if auction_data[i] == winner_bid:
                winner_name=i
        print(f"The winner is {winner_name} with a bid if ${winner_bid}")
        bid_start = False

