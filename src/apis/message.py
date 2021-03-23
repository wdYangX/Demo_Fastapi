class Message:
    def __init__(self, status_code, message):
        _status_code = status_code
        _message = message

    @property
    def status_code(self):
        return self.status_code

    @status_code.setter
    def status_code(self, status_code):
        self.status_code = status_code

    @property
    def message(self):
        return self.status_code

    @message.setter
    def message(self, message):
        self.message = message

    def __call__(self, *args, **kwargs):
        return {"status_code": self.status_code,
                "message": self.message}

    def __str__(self):
        return self().__str__()

    def __repr__(self):
        return self().__str__()