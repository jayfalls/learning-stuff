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
        Displays the data by printing each item in the given list with a delay of 
        0.2 seconds between each item

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
    def __init__(self, data_processer: Model, user_output: View) -> None:
        """
        Initializes a new instance of the class

        Parameters:
            data_processer (Model): An instance of the Model class
            user_output (View): An instance of the View class

        Returns:
            None
        """
        self.data_processer = data_processer
        self.user_output = user_output

    def run(self) -> None:
        """
        Run the model and display using view

        Parameters:
            None

        Returns:
            None
        """
        data = self.data_processer.processed_data()
        self.user_output.display_data(data)

processer = Model()
output = View()
controller = Controller(processer, output)
controller.run()
