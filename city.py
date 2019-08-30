class City:

    def __init__(self):
        self.name = ""
        self.mayor = ""
        self.established = ""
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)