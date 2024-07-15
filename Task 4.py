
def main():
    phone_book = {}

    def add_contact(args):
        name, phone = args
        phone_book[name] = phone
        print("Contact added.")

    def change_contact(args):
        name, phone = args
        if name in phone_book:
            phone_book[name] = phone
            print("Contact updated.")
        else:
            print("Contact does not exist.")

    def show_all():
        if phone_book:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    def show(name):
        if name in phone_book:
            number = phone_book.get(name)
            print(number)
        else:
            print("Error. Could not find contact.")

    def parse_input(user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    print("Welcome to the assistant bot!")
    print("Enter a command:")

    while True:
        user_input = input("> ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            show_all()
        elif command == "add" and len(args)==2:
            add_contact(args)
        elif command == "change" and len(args)==2:
            change_contact(args)
        elif command == show and len(args)==1:
            show(args)
        else: 
            print("Invalid command.")

if __name__ == "__main__":
    main()