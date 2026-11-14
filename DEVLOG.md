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

Expected result: Clicking Load CSV responds to the user's input.

Actual result: The Load CSV button responded successfully when tested in the current GUI.

Status: Passed.

**Test 2: Show Graph Button**

Expected result: Clicking Show Graph responds to the user's input.

Actual result: The Show Graph button responded successfully when tested in the current GUI.

Status: Passed.

**Test 3: Exit Button**

Expected result: Clicking Exit closes the application.

Actual result: The application closed successfully.

Status: Passed.

**Test 4: Window Close Button**

Expected result: Clicking the window's X button closes the application without errors.

Actual result: The application closed successfully using the window's X button.

Status: Passed.

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

Actual result: Cancelling the file selection worked successfully.

Status: Passed.


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

Actual result: The application successfully appended the compatible CSV, increasing the record count from 15 to 30.

Status: Passed.

**Test 3: Cancel CSV Selection**

Expected result: Cancelling the file selection leaves the current dataset unchanged.

Actual result: Cancelling the append file selection worked successfully.

Status: Passed.

## Development Entry 7 – 10 November 2026

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

## Development Entry 8 – 13 November 2026

### Task: Embedded Matplotlib Graphs in Local GUI

**Work completed:**
- Rewrote some parts of the devlog document
- Added a Matplotlib canvas to the FreeSimpleGUI window.
- Implemented the `show_graph()` method to display graphs directly inside the application.
- Connected the Show Graph button to the new method.
- Implemented `clear_graph()` to remove previously displayed graphs.
- Updated CSV loading and appending to clear outdated graphs.
- Added error handling for missing datasets, required columns and graph generation failures.

### Challenges Encountered

The original Show Graph button only updated the status message and did not display a graph.

To resolve this, `FigureCanvasTkAgg` was used to embed the Matplotlib figure inside the FreeSimpleGUI canvas.

Another consideration was preventing multiple graphs from stacking when the Show Graph button was clicked repeatedly.

### Design Decisions

I decided to display the graph inside the main application rather than opening a separate Matplotlib window.

A separate `clear_graph()` method was created to manage existing figures and prevent outdated graphs from remaining visible after the dataset changes.

I reused the existing `create_line_chart()` method in `data_visualiser.py` to keep graph generation separate from the GUI.

The graph currently uses the `Period` and `Count` columns from the population dataset. Allowing users to select different columns will be implemented in a later development iteration.

### Testing

**Test 1: Display Embedded Graph**

Expected result: After loading the population CSV and clicking Show Graph, the graph should appear inside the application window.

Actual result: The embedded graph displayed successfully inside the Local Data Explorer window.

Status: Passed.

**Test 2: Graph Replacement**

Expected result: Clicking Show Graph again should replace the existing graph rather than creating multiple graphs.

Actual result: Clicking Show Graph multiple times successfully replaced the existing graph without creating duplicates.

Status: Passed.

**Test 3: Clear Graph After Dataset Change**

Expected result: Loading or appending CSV data should clear the previously displayed graph.

Actual result: The graph was cleared successfully after changing the dataset.

Status: Passed.

**Test 4: Show Graph Without Dataset**

Expected result: An error message should appear when Show Graph is clicked without loading a CSV file.

Actual result: The application successfully displayed an error popup when no dataset was loaded.

Status: Passed.

## Development Entry 9 – 14 November 2026

### Task: Matplotlib Zoom and Pan Controls

**Work completed:**
- Imported `NavigationToolbar2Tk` from Matplotlib.
- Added a separate toolbar canvas to the FreeSimpleGUI layout.
- Added a `toolbar` attribute to the `LocalGUI` class.
- Updated `show_graph()` to display the Matplotlib navigation toolbar above the embedded graph.
- Updated `clear_graph()` to remove the existing toolbar when clearing a graph.
- Added access to zoom, pan, Home, Back, Forward and Save controls.
- Preserved the existing CSV loading, appending and graph display functionality.

### Challenges Encountered

The existing Local GUI displayed Matplotlib graphs but did not provide controls for interacting with them.

To resolve this, I used `NavigationToolbar2Tk` to add Matplotlib's built-in navigation tools directly into the FreeSimpleGUI window.

I also needed to ensure that the toolbar was removed when a graph was cleared or replaced, preventing duplicate toolbars from appearing.

### Design Decisions

I decided to use Matplotlib's existing navigation toolbar instead of creating custom zoom and pan buttons. This provides standard graph navigation functionality while keeping the implementation simple.

I placed the toolbar in a separate canvas above the graph to keep the interface organised. I also updated the existing `clear_graph()` method to manage both the graph and toolbar, keeping the cleanup functionality in one place.

### Testing

**Test 1: Display Navigation Toolbar**

Expected result: After loading a CSV and clicking Show Graph, the navigation toolbar appears above the embedded graph.

Actual result: The navigation toolbar displayed successfully.

Status: Passed.

**Test 2: Zoom Functionality**

Expected result: Selecting Zoom allows the user to zoom into a specific area of the graph.

Actual result: The zoom controls worked successfully.

Status: Passed.

**Test 3: Pan Functionality**

Expected result: Selecting Pan allows the user to move around the graph.

Actual result: The pan controls worked successfully.

Status: Passed.

## Development Entry 10 – 14 November 2026

### Task: Display Dataset Descriptions in Local GUI

**Work completed:**
- Connected the existing `get_dataset_description()` method from `data_visualiser.py` to the Local GUI.
- Added a dataset description section to the FreeSimpleGUI interface.
- Implemented `update_dataset_description()` to display information about the loaded dataset.
- Displayed the total number of records, column names and numerical statistics.
- Updated the CSV loading functionality to refresh the dataset description.
- Updated the CSV append functionality to refresh the description when additional records are added.
- Replaced the original text description with a scrollable, read-only `sg.Multiline` element.
- Preserved the existing embedded Matplotlib graph and navigation toolbar functionality.

### Challenges Encountered

The original dataset description was displayed using a `sg.Text` element, which made longer column names and numerical statistics difficult to read.

I replaced this with a scrollable `sg.Multiline` element to improve readability and allow more information to be displayed without taking up too much space in the interface.

### Design Decisions

I decided to reuse the existing `get_dataset_description()` method rather than calculate dataset statistics directly in the GUI. This keeps the data processing functionality separate from the user interface.

I also used a read-only multiline element to prevent users from accidentally editing the displayed dataset information. The dataset description automatically refreshes when CSV files are loaded or appended, ensuring that the displayed information reflects the current dataset.

### Testing

**Test 1: Display Dataset Description**

Expected result: Loading a CSV file displays the record count, column names and numerical statistics.

Actual result: The dataset description displayed successfully.

Status: Passed.

**Test 2: Dataset Description Readability**

Expected result: Longer dataset descriptions can be viewed without text being cut off.

Actual result: The scrollable description area displayed the information correctly.

Status: Passed.

**Test 3: Update Description After Appending CSV**

Expected result: Appending compatible CSV data updates the record count and numerical statistics.

Actual result: The dataset description updated successfully after appending data.

Status: Passed.

**Test 4: Embedded Graph Compatibility**

Expected result: The embedded graph and Matplotlib navigation toolbar continue functioning after adding dataset descriptions.

Actual result: The graph and navigation toolbar continued working correctly.

Status: Passed.

## Development Entry 11 – 14 November 2026

### Task: Dynamic Graph Column Selection

**Work completed:**
- Added X-axis and Y-axis dropdown menus to the Local Data Explorer.
- Implemented `update_column_selection()` to populate the dropdowns using the loaded CSV column names.
- Configured the population dataset to automatically select `Period` for the X-axis and `Count` for the Y-axis.
- Updated `load_csv()` to refresh the available graph columns when a new dataset is loaded.
- Updated `show_graph()` to use the selected X-axis and Y-axis columns instead of fixed column names.
- Added validation to check that the selected Y-axis contains numerical values.
- Preserved the existing population graph series grouping when using the original columns.
- Maintained compatibility with the embedded Matplotlib graph and navigation toolbar.

### Challenges Encountered

While implementing the dropdown menus, I encountered an `AttributeError` because I initially used `sg.text()` instead of `sg.Text()`. I corrected the capitalisation to use the correct FreeSimpleGUI element.

I also encountered a `TypeError` when checking whether the dataset was empty. This happened because I accidentally used `data()` instead of `data`, which attempted to call a Python list as a function.

After correcting these issues, the application ran successfully.

### Design Decisions

I decided to populate the dropdown menus dynamically using the column names from the loaded CSV file.

This allows the application to support datasets with different column structures without requiring changes to the graph generation code.

I also retained the default `Period` and `Count` selections for the population dataset to preserve the original graph functionality.

Numerical validation was added to prevent users from selecting unsuitable Y-axis data.

### Testing

**Test 1: Load CSV and Populate Dropdowns**

Expected result: Loading a CSV file populates both dropdowns with the available column names.

Actual result: The dropdowns populated successfully.

Status: Passed.

**Test 2: Default Column Selection**

Expected result: Loading the population dataset automatically selects `Period` and `Count`.

Actual result: The correct default columns were selected.

Status: Passed.

**Test 3: Generate Graph Using Selected Columns**

Expected result: Clicking Show Graph generates a graph using the selected X-axis and Y-axis columns.

Actual result: The graph displayed successfully.

Status: Passed.

## Development Entry 12 – 14 November 2026

### Task: Flexible CSV Graph Handling and Numerical Sorting

**Work completed:**
- Updated `create_line_chart()` in `data_visualiser.py` to support numerical and text-based X-axis values.
- Added validation to check that the selected X-axis and Y-axis columns exist in the dataset.
- Implemented automatic detection of numerical X-axis values.
- Added numerical sorting to ensure values such as 1, 2, 3, 10 and 20 appear in the correct order.
- Preserved alphabetical sorting for text-based X-axis values.
- Maintained support for multiple graph series.
- Created `data/test_numeric_sorting.csv` to test numerical sorting.
- Confirmed compatibility with dynamic graph column selection and the existing Matplotlib navigation toolbar.

### Challenges Encountered

The original graph generation method sorted all X-axis values as strings. This caused numerical values to appear in alphabetical order rather than numerical order.

For example, the values 1, 10, 2, 20 and 3 were sorted incorrectly.

To resolve this, I added a check to determine whether all X-axis values could be converted into floating-point numbers.

When the values are numerical, the application now sorts them numerically. Otherwise, it uses alphabetical sorting.

### Design Decisions

I decided to implement the sorting functionality inside `data_visualiser.py` rather than `local_gui.py`. This keeps data processing separate from the graphical user interface and allows the same functionality to be reused elsewhere in the application.

I also retained the existing `create_line_chart()` method instead of creating a separate method for numerical datasets. This allows the application to support different CSV structures without introducing unnecessary complexity.

### Testing

**Test 1: Original Population Dataset**

Expected result: The population dataset continues to display correctly using Period and Count.

Actual result: The population graph displayed successfully.

Status: Passed.

**Test 2: Numerical X-axis Sorting**

Expected result: Numerical X-axis values are sorted in ascending numerical order.

Actual result: The test dataset displayed the X-axis values in the correct numerical order.

Status: Passed.

**Test 3: Text-based X-axis Values**

Expected result: Text-based X-axis values continue to display correctly.

Actual result: The graph displayed text-based categories successfully.

Status: Passed.

**Test 4: Invalid Y-axis Data**

Expected result: Selecting a non-numerical Y-axis displays an error popup instead of generating a graph.

Actual result: The application displayed the expected error popup.

Status: Passed.

**Test 5: Matplotlib Navigation Toolbar**

Expected result: Zoom, Pan and Home continue working with the updated graph generation method.

Actual result: The navigation controls worked successfully.

Status: Passed.

**Test 6: Dynamic Column Selection**

Expected result: Loading a different CSV file updates the available X-axis and Y-axis dropdown selections.

Actual result: The dropdowns updated correctly for the new dataset.

Status: Passed.

## Development Entry 13 – 14 November 2026

### Task: Local Mode Improvements and CSV Error Handling

**Work completed:**
- Added `read_csv_safely()` to `data_visualiser.py` to handle common CSV file errors.
- Updated `load_csv()` to use the new error-handling method.
- Updated `append_csv()` to use the same error-handling method while preserving column validation.
- Ensured unsuccessful CSV loading does not replace the existing dataset.
- Ensured incompatible CSV files cannot be appended to the current dataset.
- Verified that switching between CSV datasets updates the displayed information and graph.
- Confirmed that the existing graph navigation tools continue working.

### Challenges Encountered

The original CSV loading and appending methods handled empty datasets but relied on the file-reading functionality to manage other errors.

I added a reusable helper method to handle common file-reading problems, including missing files, permission errors and invalid text encoding. This reduced repeated validation code in the loading and appending methods.

### Design Decisions

I decided to centralise CSV error handling in `read_csv_safely()` rather than implementing separate exception handling in both `load_csv()` and `append_csv()`.

This makes the code easier to maintain and ensures both operations handle errors consistently. I also kept the existing dataset unchanged when a CSV file cannot be loaded successfully, preventing accidental data loss.

### Testing

**Test 1: Load Valid CSV**

Expected result: A valid CSV file loads successfully.

Actual result: The CSV file loaded correctly.

Status: Passed.

**Test 2: Switch Dataset**

Expected result: Loading a different CSV replaces the existing dataset.

Actual result: The previous dataset was replaced successfully.

Status: Passed.

**Test 3: Append Compatible CSV**

Expected result: Compatible CSV records are appended to the current dataset.

Actual result: Records were appended successfully.

Status: Passed.

**Test 4: Append Incompatible CSV**

Expected result: An error appears and the existing dataset remains unchanged.

Actual result: The incompatible CSV was rejected without changing the dataset.

Status: Passed.

**Test 5: Invalid or Missing CSV**

Expected result: An error appears and the existing dataset remains unchanged.

Actual result: The invalid file was rejected and the existing dataset was preserved.

Status: Passed.

**Test 6: Cancel File Selection**

Expected result: Cancelling file selection does not modify the dataset.

Actual result: The dataset remained unchanged.

Status: Passed.

**Test 7: Graph After Switching Datasets**

Expected result: The graph displays information from the newly loaded dataset.

Actual result: The graph displayed the correct dataset.

Status: Passed.

**Test 8: Graph Navigation Controls**

Expected result: Zoom and Pan continue working after the CSV handling changes.

Actual result: Both controls worked successfully.

Status: Passed.

## Development Entry 14 – 14 November 2026

### Task: Remote Mode Setup and MongoDB Atlas Integration

**Work completed:**
- Updated `app.py` to support Local and Remote modes using command-line arguments.
- Added `argparse` to allow users to select the application mode.
- Preserved Local Mode as the default application mode.
- Installed PyMongo and its required dependencies.
- Configured the application to connect to MongoDB Atlas using an environment variable.
- Connected the existing Remote Mode chat application to MongoDB Atlas.
- Tested saving and retrieving chat messages from the database.
- Verified saved chat messages using MongoDB Compass.

### Challenges Encountered

Initially, the application attempted to connect to a local MongoDB server on port 27017, resulting in a connection error. The application was then configured to use MongoDB Atlas.

An invalid connection string also caused a PyMongo URI error. This was resolved by correcting the environment variable containing the MongoDB Atlas connection string.

### Design Decisions

- Used `argparse` to separate Local and Remote modes while keeping a single application entry point.
- Kept Local Mode as the default to preserve existing functionality.
- Used an environment variable to avoid storing MongoDB credentials directly in the source code.
- Reused the teacher-provided database and chat classes rather than rewriting existing functionality.
- Used MongoDB Atlas for remote database storage.

### Testing

**Test 1: Command-Line Help**

Expected result: Display available application modes.

Actual result: Both Local and Remote modes were displayed.

Status: Passed.

**Test 2: Local Mode**

Expected result: `python app.py local` launches the Local Data Explorer.

Actual result: The Local GUI opened successfully.

Status: Passed.

**Test 3: Default Mode**

Expected result: `python app.py` launches Local Mode.

Actual result: The Local GUI opened successfully.

Status: Passed.

**Test 4: MongoDB Atlas Connection**

Expected result: Python successfully connects to MongoDB Atlas.

Actual result: The database connection succeeded.

Status: Passed.

**Test 5: Save Chat Message**

Expected result: A message sent through Remote Mode is saved in MongoDB.

Actual result: The message was stored successfully and verified in MongoDB Compass.

Status: Passed.

**Test 6: Retrieve Chat Messages**

Expected result: Previously saved messages appear when Remote Mode is restarted.

Actual result: The previous message appeared after restarting the application.

Status: Passed.