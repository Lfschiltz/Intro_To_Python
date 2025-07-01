inp = input("What is clients credit ? 300 - 850 ")
if(float(inp)) >= 700:
    print("Client has good credit")
    (good_credit) = True
    (bad_credit) = False

    house_price = float("1000000")
    if good_credit:
        print("Down payment is $", int(house_price) * float(.1), " with your credit")
    elif bad_credit:
        print("Down payment is $", int(house_price) * float(.3), " with your credit")

if(float(inp)) <= 699:
    print("Client has bad credit")
    (good_credit) = False
    (bad_credit) = True

    house_price = float("1000000")
    if good_credit:
        print("Down payment is $",int(house_price) * float(.1)," with your credit")
    elif bad_credit:
        print("Down payment is $",int(house_price) * float(.3)," with your credit")