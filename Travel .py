print("\n Welcome to my Airlines")
name=input("\n Enter your name:")
pas_num=int(input("\n Enter your passport number:"))
if name and pas_num:
    print("\n your name and passport number is saved")
    print("\n Available Places are: ")
    print("\n Chennai \n Coimbatore \n Delhi \n Salem")
    trip=["Chennai","Coimbatore","Delhi","Salem"]    
    tr_c=input("\n which place you want:")
    if tr_c in trip:
        if tr_c =="Chennai":
            print(f"\n you select {tr_c} thank you")
            cla=input("\n Enter your class(first, second, third):")
            if cla=="first":
                print(f"\n you select {cla} class")
                print("\n Total amount is:2000")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            elif cla=="second":
                print(f"\n you select {cla} class")
                print("\n Total amount is:1500")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            elif cla=="third":
                print(f"\n you select {cla} class")
                print("\n Total amount is:1000")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
        elif tr_c =="Coimbatore":
            print(f"\n you select {tr_c} thank you")
            cla=input("\n Enter your class(first, second, third):")
            if cla=="first":
                print(f"\n you select {cla} class")
                print("\n Total amount is:2500")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            elif cla=="second":
                print(f"\n you select {cla} class")
                print("\n Total amount is:2000")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            elif cla=="third":
                print(f"\n you select {cla} class")
                print("\n Total amount is:1500")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
        elif tr_c =="Delhi":
            print(f"\n you select {tr_c} thank you")
            cla=input("\n Enter your class(first, second, third):")
            if cla=="first":
                print(f"you select {cla} class")
                print("\n Total amount is:3000")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            elif cla=="second":
                print(f"\n you select {cla} class")
                print("\n Total amount is:2500")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            elif cla=="third":
                print(f"\n you select {cla} class")
                print("\n Total amount is:2000")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
        elif tr_c =="Salem":
            print(f"\n you select {tr_c} thank you")
            cla=input("\n Enter your class(first, second, third):")
            if cla=="first":
                print(f"\n you select {cla} class")
                print("\n Total amount is:2000")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            elif cla=="second":
                print(f"\n you select {cla} class")
                print("\n Total amount is:1500")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            elif cla=="third":
                print(f"\n you select {cla} class")
                print("\n Total amount is:1000")
                book=input("\n Do you want to book (yes or no):")
                if book=="yes":
                    print("\n your seat is booked")
                    print("\n Thank you welcome again")
                else:
                    print("\n Thank you welcome again")
            else:
                print("\n Enter correct name of the city")
        else:
            print(f"\n This place {tr_c} not available")  
else:
    print("\n Thank you welcome again")      

     