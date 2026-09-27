ticket_price = 200


def calculate_bill(number_of_tickets):

    total = number_of_tickets * ticket_price

    return total


def show_bill(movie, seats_booked):

    total = calculate_bill(len(seats_booked))

    print()
    print("------ TICKET BILL ------")

    print("Movie :", movie)

    print("Seats :", seats_booked)

    print("Number of Tickets :", len(seats_booked))

    print("Ticket Price :", ticket_price)

    print("Total Amount :", total)

    print("-------------------------")