atm_balance=124300
users=[["SUJITH",1234,123400],["SARATHI",2345,234500],["SANKAR",3456,34500],["SUPRIYA",4567,45600],["GANASRI",1325,500000]]
l=None
amount=[100,200,500,2000]
number=[0,0,0,0]
def addmoney(bal):
    ind=0
    for i in amount:
        num=int(input("Enter No. of"+str(i)+"Notes: "))
        number[ind]+=num
        ind+=1
        bal+=(i*num)
    print("Your current balance amount in ATM: ",bal)
    print("Your money added successfully")
    return bal
def showmoney(bal):
    for j in range(0,len(amount)):
        print(str(amount[j])+"-"+str(number[j]))
    print("Your current balance amount:",bal)
def leave():
    print("Thank you")
def withdraw(bal):
    w=int(input("Enter your withdrawal amount: "))
    if(w<bal and w%100==0):
        if(w>=2000):
            a2=w//2000
            w1=(w%2000)
            if(w1>=500):
                a3=w1//500
                w1=(w1%500)
                if(w1>=200):
                    a4=w1//200
                    w1=(w1%200)
                    if(w1>=100):
                        a5=w1//100
                        w1=(w1%100)
                        if(w1==0):
                            bal-=w
                            print("Your current balance is: ",bal)
                            print("Your withdrawal amount: ")
                            print(a2,a3,a4,a5)
                    elif(w1==0):
                        a5=0
                        bal-=w
                        print("Your current balance is:",bal)
                        print("Your withdrawal amount: ")
                        print(a2,a3,a4,a5)
                    else:
                        print("Invalid amount")
                elif(w1>=100):
                    a4=0
                    a5=w1//100
                    w1=(w1%100)
                    if(w1==0):
                        bal-=w
                        print("Your current balance is: ",bal)
                        print("Your withdrawal amount: ")
                        print(a2,a3,a4,a5)
                elif(w1==0):
                    a4=0
                    a5=0
                    bal-=w
                    print("Your current balance is:",bal)
                    print("Your withdrawal amount: ")
                    print(a2,a3,a4,a5)
                else:
                    print("Invalid amount")
            elif(w1>=200):
                a3=0
                a4=w1//200
                w1=(w1%200)
                if(w1>=100):
                    a5=w1//100
                    w1=(w1%100)
                    if(w1==0):
                        bal-=w
                        print("Your current balance is: ",bal)
                        print("Your withdrawal amount: ")
                        print(a2,a3,a4,a5)
                elif(w1==0):
                    a5=0
                    bal-=w
                    print("Your current balance is:",bal)
                    print("Your withdrawal amount: ")
                    print(a2,a3,a4,a5)
                else:
                    print("Invalid amount")
            elif(w1>=100):
                a3=0
                a4=0
                a5=w1//100
                w1=(w1%100)
                if(w1==0):
                    bal-=w
                    print("Your current balance is: ",bal)
                    print("Your withdrawal amount: ")
                    print(a2,a3,a4,a5)
            elif(w1==0):
                a3=0
                a4=0
                a5=0
                bal-=w
                print("Your current balance is:",bal)
                print("Your withdrawal amount: ")
                print(a2,a3,a4,a5)
            else:
                print("Invalid amount")
        elif(w>=500):
            a2=0
            a3=w//500
            w1=(w%500)
            if(w1>=200):
                a4=w1//200
                w1=(w1%200)
                if(w1>=100):
                    a5=w1//100
                    w1=(w1%100)
                    if(w1==0):
                        bal-=w
                        print("Your current balance is: ",bal)
                        print("Your withdrawal amount: ")
                        print(a2,a3,a4,a5)
                elif(w1==0):
                    a5=0
                    bal-=w
                    print("Your current balance is:",bal)
                    print("Your withdrawal amount: ")
                    print(a2,a3,a4,a5)
                else:
                    print("Invalid amount")
            elif(w1>=100):
                a4=0
                a5=w1//100
                w1=(w1%100)
                if(w1==0):
                    bal-=w
                    print("Your current balance is: ",bal)
                    print("Your withdrawal amount: ")
                    print(a2,a3,a4,a5)
            elif(w1==0):
                a4=0
                a5=0
                bal-=w
                print("Your current balance is:",bal)
                print("Your withdrawal amount: ")
                print(a2,a3,a4,a5)
            else:
                print("Invalid amount")
        elif(w>=200):
            a2=0
            a3=0
            a4=w//200
            w1=(w%200)
            if(w1>=100):
                a5=w1//100
                w1=(w1%100)
                if(w1==0):
                    bal-=w
                    print("Your current balance is: ",bal)
                    print("Your withdrawal amount: ")
                    print(a2,a3,a4,a5)
            elif(w1==0):
                a5=0
                bal-=w
                print("Your current balance is:",bal)
                print("Your withdrawal amount: ")
                print(a2,a3,a4,a5)
            else:
                print("Invalid amount")
        elif(w==100):
            a2=0
            a3=0
            a4=0
            a5=w//100
            w1=w%100
            if(w1==0):
                bal-=w
                print("Your current balance is: ",bal)
                print("Your withdrawal amount: ")
                print(a2,a3,a4,a5)
        else:
            print("Invalid amount")
    else:
        print("Invalid amount")
    return bal
def balance_enquiry(bal):
    print("Your current balance amount: ",bal)
def pin_change(pin):
    p=int(input("Enter your current pin number:"))
    if(p==pin):
        p1=int(input("Enter your New password:"))
        p2=int(input("Confirm your New password:"))
        if(p1==p2):
            pin=p1
            return pin
            print("Your New password is updated")
        else:
            print("Enter correct password")
    else:
        print("Incorrect password")
        print("Please try again")
def admin(bal):
    while True:
        print("1. Load")
        print("2. Show")
        print("3. Exit")
        a1=int(input("Enter your choice:"))
        if(a1==1):
            bal=addmoney(bal)
        elif(a1==2):
            showmoney(bal)
        elif(a1==3):
            leave()
            break
        else:
            print("Invalid move")
    return bal
def user(bal,pin):
    while True:
        print("1. Withdraw")
        print("2. Balance Enquiry")
        print("3. Pin change")
        print("4. Exit")
        d=int(input("Enter your choice"))
        if(d==1):
            bal=withdraw(bal)
        elif(d==2):
            bal=balance_enquiry(bal)
        elif(d==3):
            pin=pin_change(pin)
        elif(d==4):
            leave()
            break
        else:
            print("Invalid move")
    return (bal,pin)
print("\t")
print("\t\t\tATM")
print("Welcome")
print("Please insert your ATM card")
print("Press Enter to continue!!!")
input()
print("1. Admin")
print("2. User")
print("3. Exit")
c=int(input("Enter your choice:"))
if(c==1):
    j=0
    while(j<3):
        j+=1
        st=str(input("Enter admin username:"))
        pi=int(input("Enter your 4 digit pin number:"))
        print("Please Enter to continue!!!")
        input()
        if(st=="Sujith"):
            if(pi==1325):
                atm_balance=admin(atm_balance)
                break
            else:
                print("Incorrect password")
        else:
            print("Incorrect admin username")
        if(j==3):
            print("Your admin account is temporarily blocked")
            print("Please try again later")
elif(c==2):
    j=0
    while(j<3):
        j+=1
        st=input("Enter your username:")
        pi=int(input("Enter your 4 digit pin number"))
        print("Please Enter to continue!!!")
        input()
        for i in range(0,len(users)):
            lis=users[i]
            if(st==lis[0] and pi==lis[1]):
                l=lis
                lis[2],lis[1]=user(lis[2],lis[1])
                break
            else:
                continue
        if(l==None):
            print("No such user")
            if(j==3):
                print("Your account is temporarily blocked")
                print("Please try again later")
elif(c==3):
    print("Thank you")
    print("Please collect your card")
else:
    print("Invalid move")
print("Please collect your card")
