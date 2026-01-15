print("Welcome to the restraunt")
print("Here is the menu")
print(" Pizza - 79rs.")
print(" Burger - 69rs.")
print(" Pasta - 89rs.")
print(" Salad - 59rs.")
print("What did you like to order sir/ma'am?")

menu = {  "pizza": 79, "burger": 69,  "pasta": 89, "salad": 59}
flag = True
bill =0
i = 1
while(flag):
    
    a = input(f"enter {i} item => ")
    item = a.lower()
    if(item in menu):
        print("item added..")
        print("You may type 'No' when your order is completed." )
        bill = bill + menu[item]      #menu.get(item)
    elif(item == "No" or item == "no" or item == "NO"):
        flag = False
    else:
        print("Sorry! Not available, enter another item: ")
    i = i+1

print(f"your Total bill is {bill} rs.")
print("Thank you for coming! Visit us Again.")
fb = input("Also give us feeback...")
print(f"Customer feedback: {fb}")