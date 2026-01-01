# main.py


from hotel_operations import (
    show_rooms,
    book_room,
    view_bookings,
    cancel_booking
)
from utils import pause, print_header
from debug_log import log_info, log_invalid_action


def display_menu():
    print_header("HOTEL HUBB MANAGEMENT SYSTEM")
    print("1. Show Available Rooms")
    print("2. Book a Room")
    print("3. View Bookings")
    print("4. Cancel Booking")
    print("5. Exit")


def main():
    log_info("Hotel Hubb application started")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            log_info("User selected: Show Available Rooms")
            show_rooms()
            pause()

        elif choice == "2":
            log_info("User selected: Book a Room")
            book_room()   # 👉 payment method asked inside this
            pause()

        elif choice == "3":
            log_info("User selected: View Bookings")
            view_bookings()
            pause()

        elif choice == "4":
            log_info("User selected: Cancel Booking")
            cancel_booking()
            pause()

        elif choice == "5":
            log_info("User exited the application")
            print("\n🙏 Thank you for using Hotel Hubb")
            break

        else:
            log_invalid_action(choice)
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
            pause()


# Program execution starts here
if __name__ == "__main__":
    main()
