# Abstraction

# reduce complexity by hinding uncessary details 

# focuses on implementation hiding 


# Showing only what is necessary and hiding how it works.
# Driving a car 🚗
# You use the steering wheel, accelerator, and brakes without knowing how the engine works internally.

class BadEmailService:

    def connect(self):
        print("connecting to email server")

    def auth(self):
        print("authenticating ...")

    def send_email(self):
        print("sending email")

    def disconnect(self):
        print("disconnecting from email server")

# This is headache for user
e = BadEmailService()
e.auth()
e.connect()
e.send_email()
e.disconnect()

class EmailService:

    def _connect(self):
        print("connecting to email server")

    def _auth(self):
        print("authenticating ...")

    def send_email(self):
        self._auth()
        self._connect()
        print("sending email")
        self._disconnect()

    def _disconnect(self):
        print("disconnecting from email server")

e = EmailService()
e.send_email()