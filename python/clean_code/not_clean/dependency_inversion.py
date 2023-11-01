# LOW LEVEL
class Lightbulb:
    def __init__(self):
        self.type: str = "Light"

    def print_state(self, state: str) -> None:
        print(f"{self.type}: {state}")

    def turn_on(self) -> None:
        self.print_state("On")

    def turn_off(self) -> None:
        self.print_state("Off")


# HIGH LEVEL
class Switch:
    def __init__(self, light: Lightbulb) -> None:
        self.is_on: bool = False
        self.light = light

    def flip_switch(self) -> None:
        if self.is_on:
            self.light.turn_off()
            self.is_on = False
        else:
            self.light.turn_on()
            self.is_on = True


# EXAMPLE
l = Lightbulb()
s = Switch(l)

s.flip_switch()
s.flip_switch()