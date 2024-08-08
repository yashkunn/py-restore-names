from app.restore_names import restore_names


def test_restore_names_updates_missing_first_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]

    restore_names(users)

    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"
         },
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"
         },
    ]


def test_restore_names_does_not_change_existing_first_names() -> None:
    users = [
        {"first_name": "Alice",
         "last_name": "Wonderland",
         "full_name": "Alice Wonderland"
         },
        {"first_name": "Bob",
         "last_name": "Builder",
         "full_name": "Bob Builder"
         },
    ]

    restore_names(users)

    assert users == [
        {"first_name": "Alice",
         "last_name": "Wonderland",
         "full_name": "Alice Wonderland"
         },
        {"first_name": "Bob",
         "last_name": "Builder",
         "full_name": "Bob Builder"
         },
    ]


def test_restore_names_with_empty_list() -> None:
    users = []

    restore_names(users)

    assert users == []
