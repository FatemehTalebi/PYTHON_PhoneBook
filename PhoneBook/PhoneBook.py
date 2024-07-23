# author:Fatemeh Talebi
class Person:
    def __init__(self, code, name, lastName, phoneNumber, email):
        self._code = code
        self._name = name
        self._lastName = lastName
        self._phoneNumber = phoneNumber
        self._email = email
        self._person_dict = {}
        self.__add_to_dictionary()


    # similarly we can use __dict__
    def __add_to_dictionary(self):
        self._person_dict["code"] = self._code
        self._person_dict["name"] = self._name
        self._person_dict["lastName"] = self._lastName
        self._person_dict["phoneNumber"] = self._phoneNumber
        self._person_dict["email"] = self._email

    def show_info(self):
        return f"code:{self._code}\tname:{self._name}\tlast name:{self._lastName}\tphone number:{self._phoneNumber}\temail:{self._email}"


# ------------------------------------------------------------------------------------------------
class Address:
    def __init__(self, city, street, unit):
        self._city = city
        self._street = street
        self._unit = unit
        self._address_dict = {}
        self.__add_to_dictionary()

    def __add_to_dictionary(self):
        self._address_dict["city"] = self._city
        self._address_dict["street"] = self._street
        self._address_dict["unit"] = self._unit

    def show_info(self):
        return f"city:\t{self._city}\tstreet:{self._street}\tunit{self._unit}"


# -------------------------------------------------------------------------------------------------
class Contact(Person, Address):
   
    def __init__(self, code, name, lastName, phoneNumber, email, city, street, unit):
        Person.__init__(self, code, name, lastName, phoneNumber, email)
        Address.__init__(self, city, street, unit)
        self.contactDictionary = {}
        self.__combine_dictionaries()  # to combine address and person dictionaries
       
    def show_info(self):
        return (
            f"code: {self._code:<4} name: {self._name:<10} last name: {self._lastName:<10} "
            f"phone number: {self._phoneNumber:<13} email: {self._email:<20} "
            f"city: {self._city:<10} street: {self._street:<10} unit: {self._unit}"
        )

    # merge person and address info
    def __combine_dictionaries(self):
        self.contactDictionary.update(self._person_dict)
        self.contactDictionary.update(self._address_dict)


# ------------------------------------------------------------------------------------------------
class PhoneBook:
    phone_book = []

    # add contact to phone book
    def add_contact(self, contact):
        PhoneBook.phone_book.append(contact)

    # search a contact
    def search_customer(self, lastName):
        lowerLastName = lastName.lower()
        search_result = []
        for contact in PhoneBook.phone_book:
            if contact.contactDictionary["lastName"].lower() == lowerLastName:
                search_result.append(contact.show_info())
            else:
                pass
        if not search_result:
            print("Customer not found")
        else:
            print("\n".join(search_result))

    def show_info(self):
        if PhoneBook.phone_book:
            for contact in PhoneBook.phone_book:
                print(contact.show_info())
        else:
            print("not found")


# ------------------------------------------------------------------------

# main app
phoneBook1 = PhoneBook()

while True:
    menue=int(input('Main menu:\nexit 0\nadd contact press 1\nsearch contact press 2\nshow all contacts press 3\n'))
    if menue==0:
        print('Good Bye')
        break
    elif menue==1:
        code=input('enter code:')
        name=input('enter name:')
        lastname=input('enter last name:')
        phoneNumber=input('enter phone number:')
        email=input('enter email:')
        city=input('enter city:')
        street=input('enter street:')
        unit=input('enter unit:')
        contact = Contact(
    code, name, lastname, phoneNumber ,email ,city, street, unit
)
        phoneBook1.add_contact(contact)
    elif menue==2:
        search=input('enter last name:')
        phoneBook1.search_customer(search)
        
    elif menue==3:
         phoneBook1.show_info()
         
    else:
        print('enter vali number')
    
