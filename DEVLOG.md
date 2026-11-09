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

## Final Reflection
