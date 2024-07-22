def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me name please."
        except IndexError:
            return "Contact not found."

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().casefold()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contact_dict = {name: phone}
    contacts.append(contact_dict)
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    for contact in contacts:
        if name in contact:
            contact[name] = phone
            return "Contact updated."


@input_error
def show_phone(args, contacts):
    return "\n".join([item.get(args[0]) for item in contacts])


@input_error
def show_all_phones(contacts):
    contact_list = contacts
    if len(contact_list) == 0:
        return "Contact list is empty"
    return "\n".join(f"{key}: {value}" for item in contact_list for key, value in item.items())


def main():
    contacts = []
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "hello":
                print("How can I help you?")

            case "close" | "exit":
                print("Good bye!")
                break

            case "add":
                print(add_contact(args, contacts))

            case "change":
                print(change_contact(args, contacts))

            case "phone":
                print(show_phone(args, contacts))

            case "all":
                print(show_all_phones(contacts))

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
