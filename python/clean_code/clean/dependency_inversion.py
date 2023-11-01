from abc import ABC, abstractmethod


# ABSTRACTION
class Switchable(ABC):
    @abstractmethod
    def __init__(self):
        self.type: str = "Type"
    
    def print_state(self, state: str) -> None:
        print(f"{self.type}: {state}")
    
    @abstractmethod
    def turn_on(self) -> None:
        pass
    
    @abstractmethod
    def turn_off(self) -> None:
        pass


# LOW LEVEL
class Lightbulb(Switchable):
    def __init__(self):
        self.type: str = "Light"

    def turn_on(self) -> None:
        self.print_state("On")

    def turn_off(self) -> None:
        self.print_state("Off")

class Fan(Switchable):
    def __init__(self):
        self.type: str = "Fan"

    def turn_on(self) -> None:
        self.print_state("On")

    def turn_off(self) -> None:
        self.print_state("Off")


# HIGH LEVEL
class Switch:
    def __init__(self, switchable: Switchable) -> None:
        self.is_on: bool = False
        self.switchable = switchable

    def flip_switch(self) -> None:
        if self.is_on:
            self.switchable.turn_off()
            self.is_on = False
        else:
            self.switchable.turn_on()
            self.is_on = True


# EXAMPLE
l = Lightbulb()
f = Fan()
s = Switch(f)

s.flip_switch()
s.flip_switch()
