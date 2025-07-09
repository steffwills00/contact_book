#dictionary to store contacts
contacts = {}

#create new contact
def new_contact():
    print('Create a new contact')
    contact_name = input('Enter name: ').strip().title()
    contact_number = input('Enter number: ')
    contacts[contact_name] = contact_number
    print(f'New contact created for {contact_name}')


#Delete a contact
def delete_contact():
    print('Delete a contact')
    who = input('Select who you want to delete: ')
    if who in contacts:
        contacts.pop(who)
    else:
        print('Contact not found!')


#start, what to do?
def start():
    while True:
        print('What would you like do do?'
              '\n[1] See your current contacts'
              '\n[2] Create a new contact'
              '\n[3] Delete a contact'
              '\n[4] Exit the program')
        choice = input('Select an option: ')

        if choice == '1':
            print('Here is a list of your contacts')
            if contacts:
                print('Here is a list of your contacts: ')
                for name, number in contacts.items():
                    print(f'{name} : {number}')
            else:
                print('You have no contacts yet.')

        elif choice == '2':
            new_contact()

        elif choice == '3':
            delete_contact()

        elif choice == '4':
            print('Chao for now!')
            break

        else:
            print('Invalid option, try again.')

start()

print('hello')