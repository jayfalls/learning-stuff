"""
This module represents an example of the Model-View-Controller (MVC) architecture
"""
from time import sleep

class Model:
    """
    This class provides methods for handling data and performing operations on the handled
    """
    @staticmethod
    def handle_data(identifier: int) -> str:
        """
        A static method that handles data

        Args:
            identifier (int): The identifier for the data

        Returns:
            str: A string indicating that the data has been handled
        """
        return f"Handled Data {str(identifier)}"

    def processed_data(self) -> list[str]:
        """
        Returns a list of processed data

        Returns:
            list[str]: A list of processed data
        """
        return [self.handle_data(index) for index in range(6)]

class View:
    """
    A class that provides methods for processing and displaying data
    """
    @staticmethod
    def display_data(data: list[str]) -> None:
        """
        Displays the data by printing each item in the given list with a delay of 0.2 seconds between each item

        Parameters:
            data (list[str]): A list of strings containing the data to be displayed

        Returns:
            None
        """
        for item in data:
            print(item, flush=True)
            sleep(0.2)

class Controller:
    """
    A class that handles the model and view
    """
    def __init__(self, model: Model, view: View) -> None:
        """
        Initializes a new instance of the class

        Parameters:
            model (model): The model object
            view (view): The view object

        Returns:
            None
        """
        self.model = model
        self.view = view

    def run(self) -> None:
        """
        Run the model and display using view

        Parameters:
            None

        Returns:
            None
        """
        data = self.model.processed_data()
        self.view.display_data(data)

model = Model()
view = View()
controller = Controller(model, view)
controller.run()
