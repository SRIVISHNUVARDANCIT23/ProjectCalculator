def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
print("******************************************calculation starts**************************")
print("select operations:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice=input("Enter the choice(1,2,3,4): ")
    if choice in('1','2','3','4'):
        x=float(input('Enter the 1st number: '))
        y=float(input('Enter the 2nd number: '))

        if choice=='1':
            print(x,'+',y,'=',add(x,y))
        elif choice=='2':
            print(x,'-',y,'=',subtract(x,y))
        elif choice=='3':
            print(x,'*',y,'=',multiply(x,y))
        elif choice=='4':
            print(x,'/',y,'=',division(x,y))
            

        nxt_calculation=input("Let's do the nxt calculation(yes/no): ")
        if nxt_calculation=='no':
            print("**********************calculation ends**********************************")

        else:
            print("***********************calculation starts again****************************")
    
