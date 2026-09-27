seats = [
    "Available",
    "Available",
    "Available",
    "Available",
    "Available",
    "Available",
    "Available",
    "Available",
    "Available",
    "Available"  # Added the 10th seat to match range(10) in show_seats()
]


def show_seats():

    print()
    print("------ SEATS ------")

    for i in range(10):

        if seats[i] == "Available":
            print(i + 1, "- Available")

        else:
            print(i + 1, "- Booked")


def book_seat(i):

    if seats[i - 1] == "Available":

        seats[i - 1] = "Booked"

        return True

    else:

        return False