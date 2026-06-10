#Headings for Different Functions
def heading( ) :
    print(" "*22,"~"*64)
    print(" "*25,"|| CHRIST CHURCH BOY's SENIOR SECONDARY SCHOOL JABALPUR ||")
    print(" "*42,"|| COMPUTER PROJECT ||")
    print(" "*45,"|| SAHIL HONDA ||")
    print(" "*41,"||'THE POWER OF DREAMS'||")
    print(" "*22,"~"*64)
def head():
    print("~"*112)
    print(" "*2,"S.NO.","\t\t","NAME","\t\t","MODEL","\t\t","RATE","\t\t","MRP","\t\t","MFG DATE","\t","QTY")
    print("~"*112)
def sl():
    print("~"*112)
    print(" "*12,"S.NO.","\t\t","NAME","\t\t","MODEL","\t\t","RATE","\t\t","MFG DATE")
    print("~"*112)
def det():
    print("~"*112)
    print("S.NO.","\t","NAME","\t\t","VEHICLE","\t","MODEL","\t\t","PRICE","\t\t","AADHAR","\t","PHONE NO." )
    print("~"*112)
#Purchasing of Vehicles
def purchase():
    import pickle
    heading( )
    p=open("purchase.dat","wb")
    ch = 'y'
    no=1
    while ch == 'y' or ch=='Y' :
        list = [ ]
        NAME = input("                               Enter the name of vehicle: ")
        MODEL = input("                               Enter the model of vehicle : ")
        RATE = int(input("                               Enter the rate of vehicle : "))
        MFG = input("                               Enter The Manufacturing Date : ")
        MRP = RATE + RATE*(50/100) 
        NV  = int(input("                               Enter the number of vehicles to be bought : "))
        list.extend([no,NAME,MODEL,RATE,MRP,MFG,NV])
        pickle.dump(list,p)    
        ch = input("                               Do You Want to purchase any more vehicle (Y/N) : ")
        no = 1 + no
    p.close()
    print(" "*33,"PURCHASE HAS BEEN COMPLETED")
#Display of Vehicles
def display():
        import pickle
        import time
        heading( )
        head()
        try :
            d = open("purchase.dat","rb") 
            x = pickle.load( d ) 
            try :
                while True :
                    if not x :
                        print("File is not present ")
                    else :
                        z=0
                        for i in range(0,7):
                            if z==0:
                                print(" "*2,x[i],end="\t\t\t ")
                                z=1
                            else:
                                if len(str(x[i])) >= 7 :
                                    print(x[i],end="\t ")
                                else:
                                    print(x[i],end="\t\t ")
                                
                            time.sleep(.2)
                    print("\n")
                    x = pickle.load( d )
            except EOFError :
                print(" "*24,"      'These are the variety of vehicles we have' ")
            print("~"*112)
            d.close( )
        except IOError :
            print("File Not Found ")
#Full Details of Vehicles
def sales():
    a=1
    cho='y'
    
    while (cho=='y' or cho=='Y')  and a<=4 :
        import pickle
        import time
        heading( )
        sl()
        try :
            d = open("purchase.dat","rb") 
            x = pickle.load( d ) 
            try :
                while True :
                    if not x :
                        print("File is not present ")
                    else :
                        z=0
                        for i in range(0,6):
                            if i==4:
                                continue
                            elif z==0:
                                print(" "*12,x[i],end="\t\t\t ")
                                z=1
                            else:
                                if len(str(x[i])) >= 7 :
                                    print(x[i],end="\t ")
                                else:
                                    print(x[i],end="\t\t ")
                            
                            time.sleep(.1)
                    print("\n")
                    x = pickle.load( d )
            except EOFError :
                print(" "*24,"      'These are the variety of vehicles we have' ")
            print("~"*112)
            d.close( )
        except IOError :
            print("File Not Found ")
        a=a+1
        ch = int(input("ENTER THE S.NO. OF THE VEHICLE YOU WANT OT PURCHASE : "))
        ch = ch-1
        try :
            e = open("information.dat","rb")
            x = pickle.load(e) 
            if not x :
                print("File is not present ")
            else :
                for i in x[ch] :
                    print(i,end="")
            print("~"*112)
            e.close( )
        except IOError :
            print("File Not Found ")
        if a == 4 :
            print("                                                !!!STOP JOKING!!!")
            break
        cho=input("Do You want to see any more data (Y/N):") 
#Purchasing of The Vehicles
def detail():
    import pickle
    V = input("Enter the name of the vehicle you want to purchase :")
    a = V.title()
    try :
        d = open("purchase.dat","rb") 
        x = pickle.load( d ) 
        try:
            while True :
                if not x :
                    print("File is not present ")
                else :
                    if x[1]== a :
                        b=int(x[4])
                        c=x[2]
                x = pickle.load( d )
        except EOFError :
            pass
        d.close( )
    except IOError :
        print("File Not Found ")
    print("Are You Really interested In Buying The Vehicle Then Pay The Amount of Rupees:",b)
    pay=input("Enter The Mode Of Payment (Check/Cash):")
    ch = input("Is The Payment Complete(Y/N):")
    if ch=='y' or ch=='Y':
        print("The Payment has been completed please give us the required information :")
        try :
            d = open("sale.dat","rb") 
            try:
                x = pickle.load( d )
                try:
                    while True :
                        if not x :
                            print("File is not present ")
                        else :
                            e = int(x[0])+ 1
                        x = pickle.load( d )
                except EOFError :
                    pass
            except EOFError :
                e = 1
            d.close( )
        except IOError :
            print("File Not Found ")
        Name = input("                               Enter Your Name : ")
        Aadhar = int(input("                               Enter Your Aadhar No. : "))
        Phone = int(input("                               Enter Your Phone No. : "))
        list = [e,Name.title(),a,c,b,Aadhar,Phone]
        s=open("sale.dat","ab")
        pickle.dump(list,s)    
        s.close()
        print(" "*33,"PURCHASE HAS BEEN COMPLETE")
        det()
        z=0
        for i in range(0,7):
            if z==0:
                print(list[i],end="\t ")
                z=1
            else:
                if len(str(list[i])) >= 7 :
                    print(list[i],end="\t ")
                else:
                    print(list[i],end="\t\t ")
        print("~"*112)         
        import os
        try :
            d = open("purchase.dat","rb") 
            g = open("temp.dat","wb")
            x = pickle.load( d ) 
            try :
                while True :
                    if not x :
                        print("File is not present ")
                    else :
                        if x[1] == a :
                            h=[]
                            for i in x :
                                if x.index(i) == 6:
                                    h.append(int(i-1))
                                else :
                                    h.append(i)
                            pickle.dump(h,g)
                        else :
                            pickle.dump(x,g)
                    x = pickle.load( d )
            except EOFError :
                pass
            d.close()
            g.close()
        except IOError :
            print("File Not Found ")
        os.remove("purchase.dat")
        os.rename("temp.dat","purchase.dat")
    else:
        print("Please Complete The Process First ")
#Information of the Customers who Bought Vehicle 
def full():
    import pickle
    import time
    try :
        d = open("sale.dat","rb") 
        x = pickle.load( d ) 
        try :
            ch = input("                               Do You Want To See A Particular Record (Y/N):")
            if ch == "y" or ch == "Y" :
                k = int(input("                               Enter The Phone No. of the Record You Want To View :"))
                while True :
                    if not x :
                        print("File is not present ")
                    else :
                        if x[6]==k :
                            det( )
                            z=0
                            for i in range(0,7):
                                if z==0:
                                    print(x[i],end="\t ")
                                    z=1
                                else:
                                    if len(str(x[i])) >= 7 :
                                        print(x[i],end="\t ")
                                    else:
                                        print(x[i],end="\t\t ")
                                time.sleep(.2)
                            print("\n")
                    x = pickle.load( d )
            else:   
                det( )
                while True :
                    if not x :
                        print("File is not present ")
                    else :
                        z=0
                        for i in range(0,7):
                            if z==0:
                                print(x[i],end="\t ")
                                z=1
                            else:
                                if len(str(x[i])) >= 7 :
                                    print(x[i],end="\t ")
                                else:
                                    print(x[i],end="\t\t ")
                            time.sleep(.2)
                    print("\n")
                    x = pickle.load( d )
        except EOFError :
            print(" "*24,"      'These are the details of customers' ")
        print("~"*112)
        d.close( )
    except IOError :
        print("File Not Found ")
#Tax given to Government
def tax():
    import pickle
    try :
        d = open("sale.dat","rb") 
        x = pickle.load( d ) 
        try :
            sum = 0
            while True :
                    if not x :
                        print("File is not present ")
                    else :
                        sum = sum + x[4] 
                    x = pickle.load( d )
        except EOFError :
            pass
        d.close( )
        print(" "*34,"The Tax Paid is :",sum*(15/100))
    except IOError :
        print("File Not Found ")
def EXIT():
    print(" "*34,"THANK YOU FOR VISITING PLEASE VISIT AGAIN")
import pickle
try :
    d = open("purchase.dat","rb") 
    x = pickle.load( d ) 
    try :
        while True :
            if not x :
                print("File is not present ")
            else :
                if int(x[6]) < 3 :
                    b=x[1]
                    print(" "*39,"YOU DON'T HAVE ENOUGH STOCK ")
                    break
            x = pickle.load( d )
    except EOFError :
        print(" "*34,"YOU HAVE ENOUGH STOCK PLEASE PROCEED")
    
    d.close( )
except IOError :
    print("File Not Found ")
#MAIN-MENU 
dict = {1:purchase,2:display,3:sales,4:detail,5:full,6:tax,7:EXIT}
ch=0
while  ch!=7 :
    print(" "*22,"~"*64)
    print(" "*25,"|| CHRIST CHURCH BOY's SENIOR SECONDARY SCHOOL JABALPUR ||")
    print(" "*42,"|| COMPUTER PROJECT ||")
    print(" "*45,"|| SAHIL HONDA ||")
    print(" "*41,"||'THE POWER OF DREAMS'||")
    print(" "*22,"~"*64)
    print(" "*30,"1.To Purchase The Vehicle .")
    print(" "*30,"2.To See The Variety Of Vehicles .")
    print(" "*30,"3.To See The Full Information Of The Vehicle You Are Interested In .")
    print(" "*30,"4.If You Are Interested In Buying The Vehicle .")
    print(" "*30,"5.To Check The Personal Details Of Customers.")
    print(" "*30,"6.To See The Tax Applied In The Vehicle .")
    print(" "*30,"7.Exit")
    ch=int(input("                               Enter Your Choice :"))
    dict.get(ch)()
