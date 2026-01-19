print("welcom to task mangament system")
Todolist=[]

def add_task():
    no_of_task=int(input("enter the number of task"))
    for i in range(1,no_of_task+1):
        tasks=input(f'enter task"{i}-  ')
        Todolist.append(tasks)
    print("all the tasks added seccessfully")    

def  update_task():
    old_task=input("enter the task you want to update")
    idx=Todolist.index(old_task)
    new_task=input("enter the new  task you want to add: ")
    print("task updated successfully")

def viwing_task():
 print("your To-do list: ")
for i in range(0, len(Todolist)):
        print(Todolist[i])


def deleting_task():
    old_task=input("enter the task you want to delete")
    idx=Todolist.index(old_task)
    Todolist.pop(idx)
    print("task deleted successfully")

   


while(True):
    choise=int(input("press 1 adding a task\npress 2 for updating a task \npress 3 for viwing the list\npress 4 for deleting task \npress 5 for exiting the system"))
  
    if(choise==1):
        add_task()

    elif(choise==2):
        update_task()

    elif(choise ==3):
        viwing_task()

    elif(choise==4):
        deleting_task()
        1
    elif(choise==5):
        print("exting from the system ")
        break
    else:
        print("invaild choise !\n vaild number")