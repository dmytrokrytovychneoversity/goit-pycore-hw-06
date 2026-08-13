# goit-pycore-hw-06

Homework 6 — basics of working with classes.

An address book built with OOP: records with a name and a list of phones.
Standard library only, no extra setup is needed.

## Classes

| Class         | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| `Field`       | base class for record fields                                         |
| `Name`        | contact name, a required field                                       |
| `Phone`       | phone number with validation (exactly 10 digits)                     |
| `Record`      | one contact: `add_phone`, `remove_phone`, `edit_phone`, `find_phone` |
| `AddressBook` | storage for records: `add_record`, `find`, `delete`                  |

## Run

```bash
python3 address_book.py
```

The `if __name__ == "__main__":` block runs the usage example from the task.
