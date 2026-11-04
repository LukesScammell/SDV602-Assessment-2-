from data_visualiser import DataVisualiser

if __name__ == "__main__":
    data_visualiser = DataVisualiser()

    data_visualiser.load_csv("data/bd-natural-increase-2010-2014.csv")

    data_visualiser.plot_line_chart(
        "Period", "Count", "Population Natural Increase", "Births_Deaths_or_Natural_Increase")
