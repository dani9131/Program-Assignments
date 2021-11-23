# create empty list
checklist = []

# CREATE
def create(item):
    # Create item code here
    checklist.append(item)

    return "added {} to checklist". format(item)

# READ
def read(index):

    # Read code here
    print(checklist[index])

    return checklist[index]

# UPDATE
def update(index, item):

    old = checklist[index]

    # Update code here
    checklist[index] = item

    return "changed {} to {}".format(old, item)

# DESTROY
def destroy(index):

    removed = checklist[index]

    # Destroy code here
    checklist.pop(index)

    return "removed {} from checklist".format(removed)

# get items on list
def all_items():

    items = []
    for el in checklist:
        print(el)
        items.append(el)

    return items

# add check mark to item
def checked(index):

    unchecked = checklist[index]

    checklist[index] = "√" + unchecked

    return checklist[index]

# give user input functions
def user_input(prompt):

    entry = input(prompt)

    return entry

#user choice function
def user_choice():

    #initialize variable for while loop
    editing = True

    while editing:

        choice = user_input("which function do you want to use? Enter C for create, R for read, U for update and D for destroy, A to view all items to currently and S to select an item with checkmart. ")

        if choice == "C" or choice == "c":

            item = user_input("what item do you want to create? Type the name of the item. ")

            create(item)

            continue

        elif choice == "R" or choice == "r":

            index = user_input("what items do you wish to read? give a number")

            read(int(index))

            continue

        elif choice == "U" or choice == "u":

            update_index = user_input("what item do you want to update? Give a number for the position. ")

            new_item = user_input("Type out the name of your item. ")

            update (int(update_index), new_item)

            continue

        elif choice == "D" or choice == "d":

            delete_index = user_input("what item do you want to delete? Give a number for the position. ")

            destroy(delete_index)

            continue

        elif choice == "A" or choice == "a":

            all_items()

        elif choice == "S" or choice == "s":

            checked_index = user_input("what items do you wish to read? give a number for the position of the item")

            checked(int(checked_index))
        else: 

            end = user_input("do you want to quit? Enter Y for yes or N for No")

            if end == "Y" or choice == "y":
                print(checklist)
                editing = False

            else:

                continue

def test():

   # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))
    # print(all_items())
    # print(checked(0))
    # print(user_input("work?"))
    user_choice()

user_choice()

