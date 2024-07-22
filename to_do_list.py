to_do=[]
def new_list():
    task=[]
    print(task)
def new_task():
    task_new=input("enter the task you want to add ")
    to_do.append(task_new)
    print(" task added")

def update_task():
    task_to_update=input(" enter the task ypu wqant to update")
    task_old=("enter the task  you want to remove ")
    to_do.replace(task_old,task_to_update)
    print(to_do)

def delete_task():
    dele=input("enter te task you want to delete")
    to_do.remove(dele)
   
def whole_dele():
    to_do.clear()

def view_tasks():
    if not to_do:
        print("Your to-do list is empty!")
    else:
        print("Your tasks:")
        for index, task in enumerate(to_do):
            print(f"{index+1}. {to_do}")

def complete_task():
    view_tasks()
    task_index = int(input("Enter the number of the task to complete: ")) - 1
    if 0 <= task_index < len(to_do):
        del to_do[task_index]
        print("Task completed!")
    else:
        print("Invalid task number.")

print("**********WELCOME TO ENCRYPTIX TASK_NAVIGATOR**********")
print("**IT IS A TASK MANAGING, NAVGATING AND REMEMBERING TOOL THAT HELPS TO MANAGE YOUR TASKS.**")
print("WHAT OPERATIONS DO YOU WANT TO PERFORM USING OUR NAVIGATOR?")
OPERATION=int(input("PRESS 1 FOR OPERATIONS OR PRESS 0 TO EXIT THE TOOL"))
if(OPERATION==1):
    
    print("***WHICH OPERATIONS DO YOU WANT TO PERFORM?***")
    print("1.CREATE NEW LIST")
    print("2.ADD NEW TASK IN YOUR LIST")
    print("3.UPDATE TASK IN YOUR LIST")
    print("4.DELETE AN EXISTING TASK")
    print("5.DELETE WHOLE LIST")
    print("6.COMPLETE TASK")
    print("7.view TASK")
    print("8.EXIT")
else:
    print("**** thank you for using sir****")
while True :
    task=input("** enter the task you want to perform**")
    if(task=="1"):
        new_list()
    elif(task=="2"):
        new_task()
    elif(task=="3"):
        update_task()
    elif(task=="4"):
        delete_task()
    elif(task=="5"):
        whole_dele()
    elif(task=="6"):
        complete_task()
    elif(task=="7"):
        view_tasks()
    elif(task=="8"):
        break
    else:
        print("invalid operation")





