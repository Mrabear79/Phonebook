dictionary = {
    'chris': {'name': 'Chris', 'phone': "503-277-1234"},
    'sam': {'name': 'Sam', 'phone': "503-277-4321"}
}

def main():
    print("Welcome to the Phone Book!")
    while True:
        print("-" * 40)
        print("Press 1 to search.")
        print("Press 2 to add.")
        print("Press 3 to change an entry.")
        print("Press 4 to remove.")
        print("Press 5 to exit.")
        print("-" * 40)
        try:
            choice = int(input('> '))
            if choice == 1:
                search()
            if choice == 2:
                add()
            if choice == 3:
                change()
            if choice == 4:
                remove()
            if choice == 5:
                exit()
        except ValueError:
            print("That is not a valid entry. Please try again.")

def search():
    name = input("Enter name you are searching for: ").lower()
    try:
        print(dictionary[name]["name"])
        print(dictionary[name]["phone"])
    except KeyError:
        print("Entry does not exsist try again")


def add():
    name = input("What name do you want to add to the phonebook:")
    phone = input("What is the phone number:")
    dictionary[name.lower()] = {'name': name, "phone": phone}
    print(dictionary[name.lower()]["name"])
    print(dictionary[name.lower()]["phone"])
    print("New person entered")

def change():
    change = input("What name do you want to change: ")
    try:
        dictionary[change]
        user_input = input("confirm name change. Y or N:").lower()
        if user_input == "y" or user_input == "yes":
            name = input("Add a new name to the phonebook:")
            phone = input("What is the phone number:")
            dictionary[name.lower()] = {'name': name, "phone": phone}
            del dictionary[change]

    except KeyError:
        print("Entry does not exsist try again")


def remove():
    remove = input("What contact do you want to remove:")
    try:
        dictionary[remove.lower()]
        user_input = input("confirm removal. Y or N:").lower()
        if user_input == "y" or user_input == "yes":
            del dictionary[remove.lower()]

    except KeyError:
        print("Entry does not exsist try again")

main()
