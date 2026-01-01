# hotel_operations.py

from database import rooms, bookings, CURRENCY
from models import Booking
from utils import get_integer_input, print_header
from debug_log import log_info, log_warning


def show_rooms():
    """Display all available rooms"""
    print_header("AVAILABLE ROOMS")
    for room_no, details in rooms.items():
        if details["available"]:
            print(
                f"Room {room_no} ({details['type']}) - "
                f"{CURRENCY}{details['price']}/night"
            )

def book_room():
    print_header("ROOM BOOKING")

    show_rooms()

    room_no = get_integer_input("\nEnter room number to book: ")

    if room_no not in rooms or not rooms[room_no]["available"]:
        print("❌ Room not available or invalid room number")
        return

    # Customer details
    name = input("Enter  customer name: ")
    mobile = input("Enter mobile number: ")
    email = input("Enter email ID: ")

    # Dates
    check_in_date = input("Enter Check-in Date (DD-MM-YYYY): ")
    check_out_date = input("Enter Check-out Date (DD-MM-YYYY): ")

    # -------- PAYMENT FIRST --------
    while True:
        payment_type = input(
            "Select payment method (Cash / Online): "
        ).strip().lower()

        if payment_type in ["cash", "online"]:
            break
        print("❌ Invalid payment method. Choose Cash or Online.")

    upi_id = None
    if payment_type == "online":
        upi_id = input("Enter UPI ID: ")
        print("Processing online payment...")
        print("Payment successful ✅")
    else:
        print("Cash payment selected")

    # -------- CREATE BOOKING --------
    booking = Booking(
        room_no=room_no,
        customer_name=name,
        price=rooms[room_no]["price"],
        mobile_number=mobile,
        email=email,
        payment_type=payment_type,
        check_in_date=check_in_date,
        check_out_date=check_out_date,
        upi_id=upi_id
    )

    bookings[room_no] = booking
    rooms[room_no]["available"] = False

    # -------- FINAL CONFIRMATION --------
    print("\n✅ Room booked successfully!")
    print(f"Room No    : {room_no}")
    print(f"Customer  : {name}")
    print(f"Check-in  : {check_in_date}")
    print(f"Check-out : {check_out_date}")
    print(f"Amount    : {CURRENCY}{rooms[room_no]['price']}")
    print("\n🙏 Thank you for booking with Hotel Hubb!")
    

def view_bookings():
    print_header("CURRENT BOOKINGS")

    if not bookings:
        print("No bookings found")
        return

    for booking in bookings.values():
        print(
            f"Room {booking.room_no} | "
            f"{booking.customer_name} | "
            f"{CURRENCY}{booking.price} | "
            f"{booking.payment_type.upper()}"
        )


def cancel_booking():
    print_header("CANCEL BOOKING")

    room_no = get_integer_input("Enter room number to cancel: ")

    if room_no in bookings:
        rooms[room_no]["available"] = True
        del bookings[room_no]
        print("✅ Booking cancelled successfully")
        log_info(f"Booking cancelled for room {room_no}")
    else:
        print("❌ No booking found for this room")
