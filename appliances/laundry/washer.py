

class Washer:

    def __init__(self, color, heat_method):
        self.color = color
        self.heat_method = heat_method

    def wash_clothes(self, setting):
        if setting == "delicates":
            print("Time to wash the undies")
        elif setting == "super_scrub":
            print("Washing your diapers and bibs")
        else:
            print("Hope you didn't mix your colors and whites")


