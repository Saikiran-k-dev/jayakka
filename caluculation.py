# def add(a,b):
#     print(f'additon of x and y are {a+b}')

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# x = int(input())
# y = int(input())

# # print(type(x),type(y))

# choice = 1

# while choice !=0:
#     print("1.add")
#     print("2.sub")
#     print("3.mul")
#     print("0.exit")
#     choice = int(input())
#     if choice ==1:
#         add(x,y)
#     if choice ==2:
#         print("subraction is",sub(x,y))
#     if choice ==3:
#         print("multiplication is",mul(x,y))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print('welcome to arithemetic program')
choice=1
while choice != 0:
    x=int(input('enter the first number\n'))
    y=int(input('enter the second number\n'))
    print('1. to perform addition')
    print('2. to perform subtraction')
    print('3. to perform multiplication')
    print('4. to perform divison')
    print('0. to exit') 
    choice=int(input('enter your choice'))
    if choice==1:
        print('addition is',add(x,y))
    if  choice==2:
        print("subtraction is",sub(x,y))
    if choice==3:
        print('multiplication is',mul(x,y))
    if choice==4:
        print('divison is',div(x,y))
    if choice==0:
        print('exit')   