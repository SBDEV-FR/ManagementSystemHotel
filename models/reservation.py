# models/reservation.py

class Reservation:
    def __init__(self, reservation_id, client_id, room_number, check_in_date, check_out_date, status):
        self.reservation_id = reservation_id
        self.client_id = client_id
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = status

    def __str__(self):
        return f"Reservation {self.reservation_id} - Room {self.room_number} for Client {self.client_id}"

