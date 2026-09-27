2from movies import show_movies, get_movie
from booking import show_seats, book_seat
from billing import show_bill


print("--------------------------------")
print("     THEATRE MANAGEMENT SYSTEM")
print("--------------------------------")

while True:

    print()
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. Show Seats")
    print("4. Exit")

    choice = input("Enter your choice: ")

   
    # SHOW MOVIES
    
    if choice == "1":

        show_movies()


   
    # BOOK TICKET
    
    elif choice == "2":

        show_movies()

        movie_number = int(
            input("Enter movie number: ")
        )

        movie = get_movie(movie_number)

        print()
        print("You selected:", movie)

        show_seats()

        number = int(
            input("How many tickets do you want? ")
        )

        booked_seats = []

        for i in range(number):

            seat = int(
                input("Enter seat number: ")
            )

            if book_seat(seat):

                print(
                    "Seat",
                    seat,
                    "booked successfully!"
                )

                booked_seats.append(seat)

            else:

                print(
                    "Seat",
                    seat,
                    "is already booked!"
                )

        show_bill(
            movie,
            booked_seats
        )


   
    # SHOW SEATS
   

    elif choice == "3":

        show_seats()


   
    # EXIT
    

    elif choice == "4":

        print()
        print("Thank you for using")
        print("Theatre Management System!")

        break


   
    # INVALID CHOICE
   
    else:

        print(
            "Invalid choice! Please enter 1 to 4."
        )