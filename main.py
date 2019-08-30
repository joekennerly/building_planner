from building import Building
from city import City

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

megalopolis = City()

megalopolis.add_building(three_o_one)
megalopolis.add_building(five_hundred)
megalopolis.add_building(executive_south)
megalopolis.add_building(curts_house)
megalopolis.add_building(large_skyscraper)

for building in megalopolis.buildings:
    print(building)