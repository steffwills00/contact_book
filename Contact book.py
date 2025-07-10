class Contact:
    def __init__(self, name, number, email, pic):
        self.name = name.title().strip()
        self.number = number.strip()
        self.email = email.strip()
        self.pic = pic

    def __str__(self):
        return f"{self.name} : {self.number}, {self.email}"


#dictionary to store contacts
contacts = []

#loop through contacts
def loop_contacts():
    print('Here is a list of your contacts')
    if contacts:
        print('Here is a list of your contacts: ')
        for contact in contacts:
            print(contact)
    else:
        print('You have no contacts yet.')


#create new contact
def new_contact():
    print('Create a new contact')
    name = input('Enter name: ').strip().title()
    number = input('Enter number: ')
    email = input('Enter email: ')
    pic = input('Enter picture file name: ')

    contact = Contact(name, number, email, pic)
    contacts.append(contact)
    print(f'New contact created for {contact.name}')


#Delete a contact
def delete_contact():
    print('Delete a contact')
    who = input('Select who you want to delete: ').strip().title()
    for contact in contacts:
        if contact.name == who:
            contacts.remove(contact)
            print(f'Contact for {who} has been deleted.')
            return
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
            loop_contacts()

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
