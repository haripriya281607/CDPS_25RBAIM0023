# models.py

class Booking:
    def __init__(
        self,
        room_no,
        customer_name,
        price,
        mobile_number,
        email,
        payment_type,
        check_in_date,
        check_out_date,
        upi_id=None
    ):
        self.room_no = room_no
        self.customer_name = customer_name
        self.price = price
        self.mobile_number = mobile_number
        self.email = email
        self.payment_type = payment_type
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.upi_id = upi_id
        self.payment_status = "SUCCESS"
