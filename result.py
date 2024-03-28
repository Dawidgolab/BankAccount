class Result:
    def __init__(self,message):
        self.isSuccess = None
        self.message = message

    def is_ok(self):
        return self.isSuccess

class Ok(Result):
    def __init__(self, message):
        self.isSuccess = True
        super().__init__(message)

class Error(Result):
    def __init__(self, message):
        self.isSuccess = False
        super().__init__(message)
