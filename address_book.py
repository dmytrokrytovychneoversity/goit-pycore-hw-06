from collections import UserDict


class Field:
    """Base class for all record fields."""

    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """Contact name, a required field."""

    pass


class Phone(Field):
    """Phone number, must be exactly 10 digits."""

    def __init__(self, value: str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain exactly 10 digits.")

        super().__init__(value)


class Record:
    """A single contact: one name and a list of phones."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        found = self.find_phone(phone)
        if found is None:
            raise ValueError(f"Phone {phone} not found.")

        self.phones.remove(found)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        found = self.find_phone(old_phone)
        if found is None:
            raise ValueError(f"Phone {old_phone} not found.")

        self.phones[self.phones.index(found)] = Phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        for p in self.phones:
            if p.value == phone:
                return p

        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Address book that stores records by contact name."""

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.data.values())


if __name__ == "__main__":
    # Create a new address book
    book = AddressBook()

    # Create a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add the John record to the address book
    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Print all records in the book
    for name, record in book.data.items():
        print(record)

    # Find and edit a phone for John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Contact name: John, phones: 1112223333; 5555555555

    # Find a specific phone in the John record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # John: 5555555555

    # Delete the Jane record
    book.delete("Jane")

    print(book)
