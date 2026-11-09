import FreeSimpleGUI as sg
from data_visualiser import DataVisualiser


class LocalGUI:
    def __init__(self):
        """Create the Local Data Explorer window."""
        sg.theme("DarkBlue3")

        self.visualiser = DataVisualiser()

        self.layout = [
            [sg.Text("Local Data Explorer", font=("Arial", 20))],
            [sg.Text("Welcome to the Local Data Explorer.", key="-STATUS-")],
            [sg.Text("Dataset: No file loaded", key="-DATASET-")],
            [sg.Button("Load CSV", key="-LOAD-"), sg.Button("Show Graph", key="-GRAPH-"), sg.Button("Exit", key="-EXIT-")]
        ]

        self.window = sg.Window(
            "SDV602 - Local Data Explorer",
            self.layout,
            size=(800, 500),
            finalize=True
        )

    def load_csv(self):
        """Allow the user to select and load a CSV file."""
        file_name = sg.popup_get_file(
            "Select a CSV file",
            file_types=(("CSV Files", "*.csv"),)
        )

        if not file_name:
            return

        if self.visualiser.load_csv(file_name):
            records = len(self.visualiser.get_data())

            self.window["-DATASET-"].update(f"Dataset: {file_name}")
            self.window["-STATUS-"].update(f"Successfully loaded {records} records.")
        else:
            sg.popup_error("Unable to load the selected CSV file.")

    def run(self):
        """Handle events from the Local Data Explorer window."""
        while True:
            event, values = self.window.read()
            # If the exit button is pressed it will run this
            if event in (sg.WIN_CLOSED, "-EXIT-"):
                break
            # If the Load button is pressed it will run this which will load the csv that is selected 
            if event == "-LOAD-":
                self.load_csv()
                
            if event == "-GRAPH-":
                self.window["-STATUS-"].update("Show Graph button clicked.")

        self.window.close()
