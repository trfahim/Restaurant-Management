import math 
pizza_nm=''
burger_nm=''
coffe_nm=''
fry_nm=''
burger=coffe=bill=pizza=0
pizza_bill=burger_bill=0
coffe_bill=fry=fry_bill=0
while True:
##Home
    print('\n++* Friends Resturent *++')
    print('\n[1] Order Food\n[2] Cancel Food\n[3] Payment\n[4] Exit')
    home = input('\nEnter Options: ')
    
#Home [1] Order food
    if home == '1':
        menu = input('\n[P] Pizza\n[B] Burger\n[C] Coffee\n[H] Home\n[F] Chicken Items\nChoose Menu: ')
        if menu == 'P'or menu == 'p':
            print('\n++* Friends Resturent *++\n** Pizza Section **')
            print('[1] Chess Pizza -- 350tk\n[2] Chicken Pizza -- 350tk\n[3] Beef Pizza -- 400tk')
            print('[4] Special Pizza -- 300tk')
            choose_pizza = input('\nChoose Pizza: ')
            if choose_pizza == '1':
                cofrom=input('\nDo you want Chess Pizza [y/n]: ')
                if cofrom=='y' or cofrom=='Y':
                    bill=bill+350
                    pizza_bill=pizza_bill+350
                    pizza=pizza+1
                    pizza_nm=pizza_nm+'\tChess Pizza'
                    print('\n**Chess Pizza add successful**')
                else:
                    print('\nChees Pizza Cancel')
            elif choose_pizza == '2':
                cofrom=input('\nDo you want Chicken Pizza [y/n]: ')
                if cofrom=='y' or cofrom=='Y':
                    bill=bill+350
                    pizza=pizza+1
                    pizza_bill=pizza_bill+350
                    pizza_nm=pizza_nm+'\tChicken Pizza'
                    print('\n**Chicken Pizza add successful**')       
                else:
                    print('\nChicken Pizza Cancel') 
            elif choose_pizza == '3':
                cofrom=input('\nDo you want Beef Pizza [y/n]: ')
                if cofrom=='y' or cofrom=='Y':
                    bill=bill+400
                    pizza=pizza+1
                    pizza_bill=pizza_bill+400
                    pizza_nm=pizza_nm+'\tBeef Pizza'
                    print('\n**Beef Pizza add successful**')
                else:
                    print('\nBeef Pizza Cancel')
            elif choose_pizza == '4':
                cofrom=input('\nDo you want Special Pizza [y/n]: ')
                if cofrom=='y' or cofrom=='Y':
                    bill=bill+300
                    pizza=pizza+1
                    pizza_bill=pizza_bill+300
                    pizza_nm=pizza_nm+'\tSpecial Pizza'
                    print('\n**Special Pizza add successful**')
                else:
                    print('\nSpecial Pizza Cancel')
            else:
                print('\nInput Error !!')
#Burger menu start
        elif menu == 'b' or menu =='B':      
            print('\n++* Friends Resturent *++\n** Burger Section **')
            print('[1] Chess Burger -- 250tk\n[2] Chicken Burger -- 180tk\n[3] Beef Burger -- 250tk')
            print('[4] Special Burger -- 200tk')
            choose_burger = input('\nChoose Burger: ')
            if choose_burger == '1':
                cofrom=input('\nDo you want Chess Burger [y/n]: ')
                if cofrom=='y' or cofrom=='Y':
                    bill=bill+250
                    burger=burger+1
                    burger_bill=burger_bill+250
                    burger_nm=burger_nm+'\tChess Burger'
                    print('\n**Chess Burger add successful**')
                else:
                    print('\nChees Burger Cancel')
            elif choose_burger == '2':
                cofrom=input('\nDo you want Chicken Burger [y/n]: ')
                if cofrom=='y' or cofrom=='Y':
                    bill=bill+180
                    burger=burger+1
                    burger_bill=burger_bill+180
                    burger_nm=burger_nm+'\tChicken Burger'
                    print('\n**Chicken Burger add successful**')       
                else:
                    print('\nChicken Burger Cancel') 
            elif choose_burger == '3':
                cofrom=input('\nDo you want Beef Burger [y/n]: ')
                if cofrom=='y' or cofrom=='Y':
                    bill=bill+250
                    burger=burger+1
                    burger_bill=burger_bill+250
                    burger_nm=burger_nm+'\tBeef Burger'
                    print('\n**Beef Burger add successful**')
                else:
                    print('\nBeef Burger Cancel')
            elif choose_burger == '4':
                cofrom=input('\nDo you want Special Burger [y/n]: ')
                if cofrom=='y' or cofrom=='Y':
                    bill=bill+200
                    burger=burger+1
                    burger_bill=burger_bill+200
                    burger_nm=burger_nm+'\tSpecial Burger'
                    print('\n**Special Burger add successful**')
                else:
                    print('\nSpecial Burger Cancel')
            else:
                print('\nInput Error !!') ##Burger section end  
                     
#coffe section start
        elif menu == 'c' or menu == 'C':
            print('\n++* Friends Resturent *++\n** Coffe Section **')
            print('[1] Cream Coffe -- 150tk\n[2] Normal Coffe -- 100tk')
            choose_coffe = input('\nChoose Coffe: ')
            if choose_coffe == '1':
                confrom=input('Do you wnat to add Cream Coffe [y/n]: ')
                if confrom == 'y' or confrom == 'Y':
                    bill=bill+150
                    coffe=coffe+1
                    coffe_bill=coffe_bill+150
                    coffe_nm=coffe_nm+'\tCream Coffe'
                    print('\n**Cream Coffe add succesful**')
                else:
                    print('\nCream Coffe cancel')
            elif choose_coffe == '2':
                confrom=input('Do you wnat to add Normal Coffe [y/n]: ')
                if confrom == 'y' or confrom == 'Y':
                    bill=bill+100
                    coffe=coffe+1
                    coffe_bill=coffe_bill+100
                    coffe_nm=coffe_nm+'\tNormal Coffe'
                    print('\n**Normal Coffe add succesful**')
                else:
                    print('\nNormal Coffe cancel')  
            else:
                print('\nError Input !')     
          
## Fry Section Start
        elif menu == 'f' or menu == 'F':
            print('\n++* Friends Resturent *++\n** Fry Section **')
            print('\n[1] Chicken Fry -- 160tk\n[2] Chicken BBQ -- 150tk\n[3] Masala BBQ -- 180tk')
            choose_fry = input('\nChoose Fry: ')
            if choose_fry == '1':
                confrom=input('\nDo you want Chicken Fry [y/n]: ')
                if confrom == 'Y' or confrom == 'y':
                    bill=bill+160
                    fry=fry+1
                    fry_nm=fry_nm+'\tChicken Fry'
                    fry_bill=fry_bill+160
                    print('\n**Chicken Fry add sucessful**')
                else:
                    print('\nChicken Fry cancel')
            elif choose_fry == '2':
                confrom=input('\nDo you want BBQ Fry [y/n]: ')
                if confrom == 'Y' or confrom == 'y':
                    bill=bill+150
                    fry=fry+1
                    fry_nm=fry_nm+'\tBBQ Fry'
                    fry_bill=fry_bill+150
                    print('\n**BBQ Fry add sucessful**')
                else:
                    print('\nBBQ Fry cancel')
            elif choose_fry == '3':
                confrom=input('\nDo you want Masala BBQ [y/n]: ')
                if confrom == 'Y' or confrom == 'y':
                    bill=bill+180
                    fry=fry+1
                    fry_nm=fry_nm+'\tChicken Fry'
                    fry_bill=fry_bill+180
                    print('\n**Masala BBQ add sucessful**')
                else:
                    print('\nMasala BBQ cancel')     ##Fry Saction End
        
        else:
            print('\nReturn Home')   
                
#Home [3] Payment          
    elif home == '3':
        print('\n-----------------------')
        print('** Your Cart **')
        print('-----------------------')
        if (pizza >= 1) or (burger >= 1) or (coffe >= 1) or (fry >= 1):
            print(f"\nSelected Items:")
            print(f"\nPizza:\n{pizza_nm}\n\tPizza ({pizza}) -- {pizza_bill}tk")
            print(f"\nBurger:\n{burger_nm}\n\tBurger ({burger}) -- {burger_bill}tk")
            print(f"\nCoffe:\n{coffe_nm}\n\tCoffe ({coffe}) -- {coffe_bill}tk")
            print(f"\nChicken Items:\n{fry_nm}\n\tFry ({fry}) -- {fry_bill}tk")
            print('\n*********************')
            print(f'Your Total bill: {bill}tk')
            print('*********************')
#Pay Bill
        if bill>0:
            pay = input('\nDo you want to pay bill [y/n]: ')
            if pay == 'y' or pay =='Y':
                print(f'\nSend {bill}tk in 01712345678')
                con_pay=input('Send money complete [y/n]: ')
            
                if con_pay == 'Y' or con_pay =='y':
                    print('\nPayment Sucessful\n**Thank You**')
                    break
                else:
                    print('\nPayment Cancel')
        elif bill == 0:
            print("\nYou didn't select any item yet !")
                       
        else:
            print(f'\nBill {bill}tk not payed')
    
#Home [2] Cancel Food
    elif home == '2':
#dislist items
        if (pizza >= 1) or (burger >= 1) or (coffe >= 1):
            print('\n--------------------')
            print('** Disselect Items **')
            print('--------------------')
            print(f"\nSelected Items:")
            print(f"\nPizza:\n{pizza_nm}\n\tPizza ({pizza}) -- {pizza_bill}tk")
            print(f"\nBurger:\n{burger_nm}\n\tBurger ({burger}) -- {burger_bill}tk")
            print(f"\nCoffe:\n{coffe_nm}\n\tCoffe ({coffe}) -- {coffe_bill}tk")
            print(f"\nChicken Items:\n{fry_nm}\n\tFry ({fry}) -- {fry_bill}tk")
        dis = input('\nDo you want to disselect item [y/n]: ')
        if dis =='y' or dis == 'Y':
            item_dis=input('\nEnter item name: ')
            if item_dis == 'Chess Pizza' or item_dis == 'chess pizza':
                pizza_nm=pizza_nm+'\t(x)Chess Pizza'
                pizza=pizza-1
                bill=bill-350
                pizza_bill=pizza_bill-350
                print(f'\n! {item_dis.title()} dislist Succesful !')
            elif item_dis == 'Chicken Pizza' or item_dis == 'chicken pizza':
                pizza_nm=pizza_nm+'\t(x)Chiken Pizza'
                pizza=pizza-1
                bill=bill-350
                pizza_bill=pizza_bill-350
                print(f'\n! {item_dis.title()} dislist Succesful !')
            elif item_dis == 'Beef Pizza' or item_dis == 'beef pizza':
                pizza_nm=pizza_nm+'\t(x)Beef Pizza'
                pizza=pizza-1
                bill=bill-400
                pizza_bill=pizza_bill-400
                print(f'\n! {item_dis.title()} dislist Succesful !')
            elif item_dis == 'Special Pizza' or item_dis == 'special pizza':
                pizza_nm=pizza_nm+'\t(x)Special Pizza'
                pizza=pizza-1
                bill=bill-300
                pizza_bill=pizza_bill-300
                print(f'\n! {item_dis.title()} dislist Succesful !')
            
            elif item_dis == 'Chess Burger' or item_dis == 'chess burger':
                burger_nm=burger_nm+'\t(x)Chess Burger'
                burger=burger-1
                bill=bill-250
                burger_bill=burger_bill-250
                print(f'\n! {item_dis.title()} dislist Succesful !')
            elif item_dis == 'Chicken Burger' or item_dis == 'chicken burger':
                burger_nm=burger_nm+'\t(x)Chiken Burger'
                burger=burger-1
                bill=bill-180
                burger_bill=burger_bill-180
                print(f'\n! {item_dis.title()} dislist Succesful !')
            elif item_dis == 'Beef Burger' or item_dis == 'beef burger':
                burger_nm=burger_nm+'\t(x)Beef Burger'
                burger=burger-1
                bill=bill-250
                burger_bill=burger_bill-250
                print(f'\n! {item_dis.title()} dislist Succesful !')
            elif item_dis == 'Special Burger' or item_dis == 'special burger':
                burger_nm=burger_nm+'\t(x)Special Burger'
                burger=burger-1
                bill=bill-200
                burger_bill=burger_bill-200
                print(f'\n! {item_dis.title()} dislist Succesful !')
            elif item_dis == 'Cream Coffe' or item_dis == 'cream coffe':
                coffe_nm=coffe_nm+'\t(x)Cream Coffe'
                coffe=coffe-1
                bill=bill-150
                coffe_bill=coffe_bill-150
                print(f'\n{item_dis.title()} dislist Succesful')
            elif item_dis == 'Normal Coffe' or item_dis == 'normal coffe':
                coffe_nm=coffe_nm+'\t(x)Noraml Coffe'
                coffe=coffe-1
                bill=bill-100
                coffe_bill=coffe_bill-100
                print(f'\n{item_dis.title()} dislist Succesful')
            elif item_dis == 'Chicken Fry' or item_dis =='chicken fry':
                fry_nm=fry_nm+'\t(x)Chicken Fry'
                fry=fry-1
                bill=bill-160
                fry_bill=fry_bill-160
                print(f'\n{item_dis.title()} dislist Sucessful')
            elif item_dis == 'BBQ Fry' or item_dis == 'bbq fry':
                fry_nm=fry_nm+'\t(x)BBQ Fry'
                fry=fry-1
                bill=bill-150
                fry_bill=fry_bill-150
                print(f'\n{item_dis.title()} dislist Sucessful')
            elif item_dis == 'BBQ Masala' or item_dis == 'bbq masala':
                fry_nm=fry_nm+'\t(x)BBQ Masala'
                fry=fry-1
                bill=bill-180
                fry_bill=fry_bill-180
                print(f'\n{item_dis.title()} dislist Sucessful')
            else:
                print('\nItem not found !')
        else:
            print('\nReturn Home')  ##Dislist End
        
    ##Exit Section
    elif home == '4':
        print('\n** EXIT SUCCESSFUL **\n')
        break
    else:
        print('\nInput Error !!')
        
                                           ##END CODE
