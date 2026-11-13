import FreeSimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_visualiser import DataVisualiser


class LocalGUI:
    def __init__(self):
        """Create the Local Data Explorer window."""
        sg.theme("DarkBlue3")

        self.visualiser = DataVisualiser()
        self.figure = None
        self.figure_canvas = None

        self.layout = [
            [sg.Text("Local Data Explorer", font=("Arial", 20))],
            [sg.Text("Welcome to the Local Data Explorer.", key="-STATUS-")],
            [sg.Text("Dataset: No file loaded", key="-DATASET-")],
            [sg.Button("Load CSV", key="-LOAD-"), sg.Button("Append CSV", key="-APPEND-"), sg.Button("Show Graph", key="-GRAPH-"), sg.Button("Exit", key="-EXIT-")],
            [sg.Canvas(key="-CANVAS-", size=(760, 350))]
        ]

        self.window = sg.Window(
            "SDV602 - Local Data Explorer",
            self.layout,
            size=(850, 550),
            finalize=True
        )

    def clear_graph(self):
        """Remove the currently displayed graph."""
        if self.figure_canvas is not None:
            self.figure_canvas.get_tk_widget().destroy()
            self.figure_canvas = None

        if self.figure is not None:
            plt.close(self.figure)
            self.figure = None

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

            self.clear_graph()
            self.window["-DATASET-"].update(f"Dataset: {file_name}")
            self.window["-STATUS-"].update(f"Successfully loaded {records} records.")
        else:
            sg.popup_error("Unable to load the selected CSV file.")

    def append_csv(self):
        """Append records from another CSV file to the current dataset."""
        if not self.visualiser.get_data():
            sg.popup_error("Please load a CSV file before appending data.")
            return

        file_name = sg.popup_get_file(
            "Select a CSV file to append",
            file_types=(("CSV Files", "*.csv"),)
        )

        if not file_name:
            return

        if self.visualiser.append_csv(file_name):
            records = len(self.visualiser.get_data())

            self.clear_graph()
            self.window["-STATUS-"].update(
                f"CSV appended successfully. Total records: {records}."
            )
        else:
            sg.popup_error("Unable to append CSV. Check that the columns match.")

    def show_graph(self):
        """Display the loaded dataset as an embedded Matplotlib graph."""
        if not self.visualiser.get_data():
            sg.popup_error("Please load a CSV file before displaying a graph.")
            return

        columns = self.visualiser.get_data()[0].keys()

        if not {"Period", "Count"}.issubset(columns):
            sg.popup_error("The dataset must contain Period and Count columns.")
            return

        self.clear_graph()

        try:
            self.figure = self.visualiser.create_line_chart(
                "Period",
                "Count",
                "Population Data",
                "Births_Deaths_or_Natural_Increase" if "Births_Deaths_or_Natural_Increase" in columns else None
            )
        except (ValueError, KeyError, TypeError) as error:
            sg.popup_error(f"Unable to create graph: {error}")
            return

        if self.figure is None:
            sg.popup_error("Unable to create graph.")
            return

        canvas = self.window["-CANVAS-"].TKCanvas
        self.figure_canvas = FigureCanvasTkAgg(self.figure, master=canvas)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        self.window["-STATUS-"].update("Graph displayed successfully.")

    def run(self):
        """Handle events from the Local Data Explorer window."""
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "-EXIT-"):
                break

            if event == "-LOAD-":
                self.load_csv()

            if event == "-APPEND-":
                self.append_csv()

            if event == "-GRAPH-":
                self.show_graph()

        self.clear_graph()
        self.window.close()
