def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    name, phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = phone
    else:
        return "Invalid name"
    return "Contact changed."

def phone_username(args, contacts):
    name = args
    name[0] = name[0].lower()
    if name[0] in contacts:
        return contacts[name[0]]
    else:
        return "Invalid name"
      
def all_phone_print(contacts):
    str=''
    for keys, value in contacts.items():
        str = str + keys + ": " + value + "\n"
    return str[:-1]  

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            print(contacts)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts)) 
        elif command == "all":
            print(all_phone_print(contacts))             
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()