def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "\033[32m{}\033[0m".format("Contact added.")

def change_username_phone(args, contacts):
    name, phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = phone
    else:
        return "\033[31m{}\033[0m".format("Invalid name.")
    return "\033[32m{}\033[0m".format("Contact changed.")

def phone_username(args, contacts):
    name = args
    name[0] = name[0].lower()
    if name[0] in contacts:
        return contacts[name[0]]
    else:
        return "\033[31m{}\033[0m".format("Invalid name.")
      
def all_phone_print(contacts):
    str=''
    for keys, value in contacts.items():
        str = str + "\033[1m{}\033[0m".format(keys) + ": " + value + "\n"
    return str[:-1]  

def main():
    contacts = {}
    print("\033[1m\033[34m{}\033[0m".format("Welcome to the assistant bot!"))
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("\033[34m{}\033[0m".format("Good bye!"))
            break
        elif command == "hello":
            print("\033[34m{}\033[0m".format("How can I help you?"))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts)) 
        elif command == "all":
            print(all_phone_print(contacts))             
        else:
            print("\033[31m{}\033[0m".format("Invalid command."))

if __name__ == "__main__":
    main()

