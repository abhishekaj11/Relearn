
def myfunc():
    print("hello")

minbal=1000

def manger(name,money):
    if money < minbal:
        print('insuffient bal')
    else:
        print("current balance: $",money)
    return name,money



manger(input('enter name :'),int (input("enter money: ")))


acct ={
    'ramu' : 23,
    "bala" : 2000,
    "natti" : 302,
    'ravi' : 100,
    "k7" : 49

}


y = acct.values()

def bank():
    for x in y :
        

        if x > 100:
             print("accont terminated")
            
             print(x)
    
  
    
       

bank()



