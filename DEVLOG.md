# SDV602 Assessment 2 – Development Log

## Project Overview

This project involves developing a Data Exploration System (DES) using Python. The application will allow users to load and visualise datasets in both local and remote modes.

The application is being developed using the starter code provided by the tutor. Additional functionality will be implemented to meet the assessment requirements and follow the interface designs created during Phase 1.

## Development Entry 1 – 4 November 2026

### Task: Initial Project Setup

**Work completed:**
- Created the project folder and opened it in Visual Studio Code.
- Set up a Python virtual environment (`.venv`).
- Installed Matplotlib for data visualisation.
- Added the tutor's starter code to the project.
- Successfully ran `app.py`.
- Confirmed that the population data was displayed using a Matplotlib line graph.
- Started setting up project documentation and Git version control.

### Challenges Encountered

During the initial setup, two virtual environments were created (`.venv` and `.venv-1`). I checked which Python interpreter was active and confirmed that `.venv` was being used.

Another issue occurred when running `app.py`, because the starter files had not yet been copied into the project folder. After adding the files, the application ran successfully.


### Testing

**Test:** Run the starter application using `python app.py`.

**Expected result:** A Matplotlib graph displaying the sample population dataset.

**Actual result:** The graph displayed successfully, showing Births, Deaths and Natural Increase.

**Status:** Passed.

## Development Entry 2 – 9 November 2026

### Task: Local Dataset Management

**Work completed:**
- Updated the existing `DataVisualiser` class.
- Modified `load_csv()` to return a Boolean indicating whether loading succeeded.
- Added `append_csv()` to append records from another CSV file.
- Added column validation to prevent incompatible datasets from being combined.
- Added `get_data()` to retrieve the currently loaded dataset.
- Preserved the tutor's original graphing functionality.

### Challenges Encountered

When testing the updated application, Python could not find the Matplotlib module. I checked the Python environment and resolved the dependency issue. After this, the application displayed the original graph successfully.

### Design Decisions

I decided to extend the existing `DataVisualiser` class rather than create a separate class for dataset management. This allows the same class to manage the currently loaded data while keeping file operations in `FileManager`.

I also added a check to compare CSV column names before appending data, to avoid combining datasets with different structures.

### Testing

**Test 1: Original graph**

Expected result: The original population graph displays correctly.

Actual result: The graph displayed successfully.

Status: Passed.

**Test 2: Append CSV data**

Expected result: Appending the same CSV file increases the number of records from 15 to 30.

Actual result:
- Initial records: 15
- Records after append: 30

Status: Passed.

**Test 3: Load a nonexistent CSV file**

Expected result: The application handles the missing file without crashing, returns `False`, and keeps the dataset empty.

Actual result:
- The file manager displayed a file-not-found error.
- `load_csv()` returned `False`.
- The dataset contained 0 records.

Status: Passed.

**Test 4: Append a CSV file with incompatible columns**

Expected result: The application rejects the incompatible CSV file and preserves the existing dataset.

Actual result:
- Initial records: 15
- The application displayed "The CSV columns do not match."
- `append_csv()` returned `False`.
- Records after append: 15

Status: Passed.

## Development Entry 3 – 9 November 2026

### Task: Basic Local Data Explorer GUI

**Work completed:**
- Created `local_gui.py` using FreeSimpleGUI.
- Implemented the `LocalGUI` class to manage the graphical interface.
- Added a basic layout containing a heading and welcome message.
- Created the application window using `sg.Window()`.
- Added a `run()` method containing the event loop.
- Updated `app.py` to launch the Local GUI.
- Committed the initial GUI implementation to Git.

### Challenges Encountered

No major issues were encountered during the initial GUI implementation.

### Design Decisions

I decided to create a separate `LocalGUI` class rather than place the interface code directly inside `app.py`.

This keeps the application's entry point separate from the GUI implementation and makes it easier to add new features without changing the main application file.

I also started with a basic window before adding CSV loading, graphing and other functionality so that each feature could be developed and tested individually.

### Testing

**Test 1: Launch the Local GUI**

Expected result: Running `python app.py` opens the Local Data Explorer window.

Actual result: The application opened the FreeSimpleGUI window successfully.

Status: Passed.

**Test 2: Close the Local GUI**

Expected result: Closing the window ends the application without errors.

Actual result: The window closed successfully.

Status: Passed.

## Development Entry 4 – 9 November 2026

### Task: Buttons and Event Handling

**Work completed:**
- Added Load CSV, Show Graph and Exit buttons to the Local GUI.
- Assigned unique keys to each button so the application can identify which button was clicked.
- Updated the `run()` method to handle button events.
- Added a status message that changes when the Load CSV or Show Graph button is clicked.
- Implemented the Exit button to close the application.
- Kept the existing basic GUI layout and window functionality.

### Challenges Encountered

No major issues were encountered while implementing the buttons and event handling.

### Design Decisions

I decided to use FreeSimpleGUI event keys such as `-LOAD-`, `-GRAPH-` and `-EXIT-` to identify button interactions.

I also kept the event handling inside the `run()` method because this is where the application continuously checks for user input.

At this stage, the Load CSV and Show Graph buttons only updated the status message. Their actual functionality would be implemented in later development iterations.

### Testing

**Test 1: Load CSV Button**

Expected result: Clicking Load CSV updates the status message.

Actual result: To be confirmed.

Status: Pending.

**Test 2: Show Graph Button**

Expected result: Clicking Show Graph updates the status message.

Actual result: To be confirmed.

Status: Pending.

**Test 3: Exit Button**

Expected result: Clicking Exit closes the application.

Actual result: To be confirmed.

Status: Pending.

**Test 4: Window Close Button**

Expected result: Clicking the window's X button closes the application without errors.

Actual result: To be confirmed.

Status: Pending.

## Development Entry 5 – 9 November 2026

### Task: Loading CSV Files Through the Local GUI

**Work completed:**
- Imported the existing `DataVisualiser` class into `local_gui.py`.
- Created a `DataVisualiser` instance inside the `LocalGUI` class.
- Added a `load_csv()` method to allow users to select a CSV file.
- Used `sg.popup_get_file()` to open a file selection dialog.
- Connected the Load CSV button to the new method.
- Added a text element to display the selected dataset filename.
- Updated the status message to display the number of records loaded.
- Added handling for cancelled file selection and unsuccessful loading.

### Challenges Encountered

No major issues were encountered when implementing the CSV loading functionality.

### Design Decisions

I decided to reuse the existing `DataVisualiser.load_csv()` method instead of adding CSV processing directly to the GUI.

This keeps the interface code separate from the dataset management functionality and avoids duplicating code.

I also added a status message to provide feedback when a dataset is loaded successfully.

### Testing

**Test 1: Load a CSV File**

Expected result: Selecting a valid CSV file loads the dataset and displays the filename and record count.

Actual result: The CSV file loaded successfully, and the GUI displayed the dataset information.

Status: Passed.

**Test 2: Cancel File Selection**

Expected result: Cancelling the file dialog leaves the application open without changing the dataset.

Actual result: To be confirmed.

Status: Pending.

**Test 3: Load an Invalid CSV File**

Expected result: If the dataset cannot be loaded, the application displays an error message without crashing.

Actual result: To be confirmed.

Status: Pending.

## Development Entry 6 – 9 November 2026

### Task: Append CSV Files Through the Local GUI

**Work completed:**
- Added an Append CSV button to the Local GUI.
- Created an `append_csv()` method inside the `LocalGUI` class.
- Connected the button to the existing `DataVisualiser.append_csv()` method.
- Added validation to prevent appending before a dataset has been loaded.
- Added a file selection dialog for choosing CSV files to append.
- Updated the status message to display the total number of records after a successful append.
- Added an error popup when the selected CSV cannot be appended.

### Challenges Encountered

While testing the append functionality, I initially thought the application had accepted a CSV file with incompatible columns. After checking the error message, I confirmed that the application correctly rejected the file.

### Design Decisions

I reused the existing `DataVisualiser.append_csv()` method instead of duplicating the CSV validation inside the GUI.

This keeps dataset processing separate from the interface and allows the GUI to display feedback based on whether the operation succeeds.

I also added a check to prevent users from appending records when no dataset has been loaded.

### Testing

**Test 1: Append CSV With Incompatible Columns**

Expected result: The application rejects the incompatible CSV file and displays an error message.

Actual result: The application displayed an error indicating that the CSV could not be appended.

Status: Passed.

**Test 2: Append Compatible CSV**

Expected result: Appending the original population CSV increases the record count from 15 to 30.

Actual result: To be confirmed.

Status: Pending.

**Test 3: Append Without Loading a Dataset**

Expected result: The application displays an error asking the user to load a CSV first.

Actual result: To be confirmed.

Status: Pending.

**Test 4: Cancel CSV Selection**

Expected result: Cancelling the file selection leaves the current dataset unchanged.

Actual result: To be confirmed.

Status: Pending.

## Development Entry 7 – 10 November 2026

### Task: Dataset Descriptions and Reusable Chart Generation

**Work completed:**
- Added a `get_dataset_description()` method to the `DataVisualiser` class.
- Added functionality to retrieve the number of records and column names from the loaded dataset.
- Added numerical statistics including minimum, maximum and average values.
- Created a `create_line_chart()` method that generates and returns a Matplotlib figure.
- Updated `plot_line_chart()` to reuse the new chart generation method.
- Kept the existing CSV loading and appending functionality unchanged.

### Challenges Encountered## Development Entry 7 – 10 November 2026

### Task: Dataset Descriptions and Reusable Chart Generation

**Work completed:**
- Added a `get_dataset_description()` method to the `DataVisualiser` class.
- Added functionality to retrieve the number of records and column names from the loaded dataset.
- Added numerical statistics including minimum, maximum and average values.
- Created a `create_line_chart()` method that generates and returns a Matplotlib figure.
- Updated `plot_line_chart()` to reuse the new chart generation method.
- Kept the existing CSV loading and appending functionality unchanged.

### Challenges Encountered

When running the initial test, Python displayed a `ModuleNotFoundError` for Matplotlib. I checked the Python interpreter and confirmed that Matplotlib was already installed in the project's `.venv` virtual environment.

After using the correct environment, the test ran successfully.

### Design Decisions

I decided to separate chart generation from chart display by creating a `create_line_chart()` method.

This allows the application to generate a Matplotlib figure that can later be embedded directly into the FreeSimpleGUI window instead of always opening a separate graph window.

I also added dataset descriptions to the existing `DataVisualiser` class because it already manages the loaded dataset.

### Testing

**Test 1: Empty Dataset Description**

Expected result: An empty dataset returns zero records, no columns and no statistics.

Actual result: The method returned `{'records': 0, 'columns': [], 'statistics': {}}`.

Status: Passed.

**Test 2: Load CSV and Retrieve Dataset Description**

Expected result: Loading the population CSV returns 15 records, three column names and numerical statistics.

Actual result: The CSV loaded successfully and returned 15 records with the columns `Period`, `Births_Deaths_or_Natural_Increase` and `Count`. Numerical statistics were generated for `Period` and `Count`.

Status: Passed.

**Test 3: Create Matplotlib Figure**

Expected result: The `create_line_chart()` method successfully generates a Matplotlib figure using the population dataset.

Actual result: The method returned a figure successfully, and the test displayed `Figure created: True`.

Status: Passed.

**Test 4: Display Graph Through Local GUI**

Expected result: The Local GUI displays the generated Matplotlib figure when the Show Graph button is clicked.

Actual result: To be confirmed.

Status: Pending.

When running the initial test, Python displayed a `ModuleNotFoundError` for Matplotlib. I checked the Python interpreter and confirmed that Matplotlib was already installed in the project's `.venv` virtual environment.

After using the correct environment, the test ran successfully.

### Design Decisions

I decided to separate chart generation from chart display by creating a `create_line_chart()` method.

This allows the application to generate a Matplotlib figure that can later be embedded directly into the FreeSimpleGUI window instead of always opening a separate graph window.

I also added dataset descriptions to the existing `DataVisualiser` class because it already manages the loaded dataset.

### Testing

**Test 1: Empty Dataset Description**

Expected result: An empty dataset returns zero records, no columns and no statistics.

Actual result: The method returned `{'records': 0, 'columns': [], 'statistics': {}}`.

Status: Passed.

**Test 2: Load CSV and Retrieve Dataset Description**

Expected result: Loading the population CSV returns 15 records, three column names and numerical statistics.

Actual result: The CSV loaded successfully and returned 15 records with the columns `Period`, `Births_Deaths_or_Natural_Increase` and `Count`. Numerical statistics were generated for `Period` and `Count`.

Status: Passed.

**Test 3: Create Matplotlib Figure**

Expected result: The `create_line_chart()` method successfully generates a Matplotlib figure using the population dataset.

Actual result: The method returned a figure successfully, and the test displayed `Figure created: True`.

Status: Passed.

**Test 4: Display Graph Through Local GUI**

Expected result: The Local GUI displays the generated Matplotlib figure when the Show Graph button is clicked.

Actual result: To be confirmed.

Status: Pending.


## Final Reflection
