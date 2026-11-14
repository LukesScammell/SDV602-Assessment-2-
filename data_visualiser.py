from file_manager import FileManager
import matplotlib.pyplot as plt


class DataVisualiser:
    def __init__(self):
        self.file_manager = FileManager()
        self.data = []

    def load_csv(self, file_name):
        """Load a CSV file and replace the current dataset."""
        data = self.read_csv_safely(file_name)

        if data is None:
            return False

        self.data = data
        return True
    
    def read_csv_safely(self, file_name):
        """Read a CSV file and handle common file errors."""
        try:
            data = self.file_manager.read_csv(file_name)
        except (OSError, UnicodeError, ValueError) as error:
            print(f"Unable to read CSV file: {error}")
            return None

        if not data:
            print(f"No data loaded from file: {file_name}")
            return None

        return data

    def append_csv(self, file_name):
        """Append records from a compatible CSV file."""
        new_data = self.read_csv_safely(file_name)

        if new_data is None:
            return False

        if self.data:
            current_columns = set(self.data[0].keys())
            new_columns = set(new_data[0].keys())

            if current_columns != new_columns:
                print("The CSV columns do not match.")
                return False

        self.data.extend(new_data)
        return True

    def get_data(self):
        """Return the currently loaded dataset."""
        return self.data

    def get_dataset_description(self):
        """Return record counts, column names and numerical statistics."""
        if not self.data:
            return {
                "records": 0,
                "columns": [],
                "statistics": {}
            }

        columns = list(self.data[0].keys())
        statistics = {}

        for column in columns:
            values = []

            for row in self.data:
                value = row.get(column, "")

                if value is None or value.strip() == "":
                    continue

                try:
                    values.append(float(value))
                except ValueError:
                    values = []
                    break

            if values:
                statistics[column] = {
                    "minimum": min(values),
                    "maximum": max(values),
                    "average": sum(values) / len(values)
                }

        return {
            "records": len(self.data),
            "columns": columns,
            "statistics": statistics
        }

    def create_line_chart(self, x_key, y_key, title, series_key=None):
        """Create a line chart with appropriate X-axis sorting."""
        if not self.data:
            return None

        columns = self.data[0].keys()

        if x_key not in columns or y_key not in columns:
            raise KeyError("The selected graph columns do not exist.")

        series = {}

        for row in self.data:
            name = row.get(series_key) if series_key else "Data"
            series.setdefault(name, []).append(row)

        # Determine whether all X-axis values are numeric.
        numeric_x = True

        for row in self.data:
            try:
                float(row[x_key])
            except (ValueError, TypeError):
                numeric_x = False
                break

        fig, ax = plt.subplots(figsize=(8, 5))

        for name, rows in series.items():
            if numeric_x:
                rows = sorted(rows, key=lambda row: float(row[x_key]))
                x_values = [float(row[x_key]) for row in rows]
            else:
                rows = sorted(rows, key=lambda row: str(row[x_key]))
                x_values = [row[x_key] for row in rows]

            y_values = [float(row[y_key]) for row in rows]

            ax.plot(
                x_values,
                y_values,
                marker="o",
                label=name
            )

        if series_key:
            ax.legend()

        ax.set_xlabel(x_key)
        ax.set_ylabel(y_key)
        ax.set_title(title)

        fig.tight_layout()

        return fig

    def plot_line_chart(self, x_key, y_key, title, series_key=None):
        """Display a line chart in a separate Matplotlib window."""
        if not self.data:
            print("No data to plot!")
            return

        figure = self.create_line_chart(
            x_key,
            y_key,
            title,
            series_key
        )

        if figure is not None:
            plt.show()
