import FreeSimpleGUI as sg


class LocalGUI:
    def __init__(self):
        """Create the Local Data Explorer window."""
        sg.theme("DarkBlue3")

        self.layout = [
            [sg.Text("Local Data Explorer", font=("Arial", 20))],
            [sg.Text("Welcome to the Local Data Explorer.", key="-STATUS-")],
            [sg.Button("Load CSV", key="-LOAD-"), sg.Button("Show Graph", key="-GRAPH-"), sg.Button("Exit", key="-EXIT-")]
        ]

        self.window = sg.Window(
            "SDV602 - Local Data Explorer",
            self.layout,
            size=(800, 500),
            finalize=True
        )

    def run(self):
        """Handle events from the Local Data Explorer window."""
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "-EXIT-"):
                break

            if event == "-LOAD-":
                self.window["-STATUS-"].update(
                    "Load CSV button clicked."
                )

            if event == "-GRAPH-":
                self.window["-STATUS-"].update(
                    "Show Graph button clicked."
                )

        self.window.close()
