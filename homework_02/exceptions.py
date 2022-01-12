"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):

    def __str__(self) -> str:
        return "LowFuelError"


class NotEnoughtFuel(Exception):

    def __str__(self) -> str:
        return "NotEnoughtFuel"


class CargoOverload(Exception):

    def __str__(self) -> str:
        return "CargoOverload"
