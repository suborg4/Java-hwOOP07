from HW.model.products.VolumeComparator import VolumeComparator

class BottleOfWater(VolumeComparator):
    def __init__(self, name, price, volume):
        super().__init__(name, price, volume)

    def __str__(self):
        return super().__str__()