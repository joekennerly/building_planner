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

    def declare(self):
        print(f"On {self.date_constructed}, {self.designer} constructed {self.address}, a {self.stories} building purchased by {self.owner}.")

three_o_one = Building("301 Plus Park", 4)
five_hundred = Building("500 Interstate Blvd S", 5)
executive_south = Building("1 Executive South", 10)
curts_house = Building("100 Curt's House", 2)
large_skyscraper = Building("3030 Oprah Rd", 100)

three_o_one.purchase("Dr. Phil")
five_hundred.purchase("Joe Shep")
executive_south.purchase("Drew Pazola")
curts_house.purchase("Curt Cato")
large_skyscraper.purchase("Oprah")

three_o_one.construct()
five_hundred.construct()
executive_south.construct()
curts_house.construct()
large_skyscraper.construct()

three_o_one.declare()
five_hundred.declare()
executive_south.declare()
curts_house.declare()
large_skyscraper.declare()