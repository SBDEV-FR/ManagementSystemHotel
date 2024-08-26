 # models/client.py

class Client:
    def __init__(self, client_id, first_name, last_name, email, phone_number):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
