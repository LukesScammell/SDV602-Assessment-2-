import FreeSimpleGUI as sg


class LocalGUI:
    def __init__(self):
        """Create the Local Data Explorer window."""
        sg.theme("DarkBlue3")

        self.layout = [
            [
                sg.Text(
                    "Local Data Explorer",
                    font=("Arial", 20)
                )
            ],
            [
                sg.Text(
                    "Welcome to the Local Data Explorer."
                )
            ]
        ]

        self.window = sg.Window(
            "SDV602 - Local Data Explorer",
            self.layout,
            size=(800, 500),
            finalize=True
        )

    def run(self):
        """Keep the window open until the user closes it."""
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

        self.window.close()
