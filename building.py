import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = "Joe Kennerly"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, str):
        self.owner = str

    def __str__(self):
        return(f"On {self.date_constructed}, {self.designer} constructed {self.address}, a {self.stories} building purchased by {self.owner}.")