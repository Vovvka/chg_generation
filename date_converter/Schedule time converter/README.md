
# Convert Time in Calendar

This script is used to convert times in a calendar Excel sheet to a specific timezone. The easiest way to run this script is by using the Visual Studio Code Jupyter extension or the Jupyter Notebook application in Google Chrome, which you can save as an additional app on your PC.

## Prerequisites

### Option 1: Visual Studio Code Jupyter Extension
1. Install Visual Studio Code: [Download VS Code](https://code.visualstudio.com/download)
2. Install the Jupyter extension: [Visual Studio Marketplace - Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
3. Install Pip manager: [Pip manager](https://marketplace.visualstudio.com/items?itemName=slightc.pip-manager)

### Option 2: Jupyter Notebook in Google Chrome
1. Open Jupyter Lab in your browser: [Try Jupyter](https://jupyter.org/try-jupyter/lab/)
2. Save Jupyter Lab as an application on your PC for easy access.


## Script Explanation

The script uses the Python `pytz` library for timezone calculations. We define a `timezone_mapping` variable where we specify custom time zones that are not in the standardized format.

### Timezone Mapping

The `timezone_mapping` dictionary maps friendly time zone names from the sheet to `pytz` time zones:

```python
timezone_mapping = {
    'argentina': 'America/Argentina/Buenos_Aires',
    'pst': 'America/Los_Angeles',
    'pdt': 'America/Los_Angeles',
    'pst/pdt': 'America/Los_Angeles',
    # ... add other mappings as needed
}
```

### Default Timezone

We convert from the respective time zones to our main time zone, *Europe/London*, which is the default in SNOW for our accounts.

## Running the Script

1. **Prepare the Environment:**
   - Ensure you have Python installed on your system.
   - Ensure you have the following Python libraries installed:
    - `pytz`
    - `openpyxl`
    - `dateutil`
   - You can install them using pip:
    ```sh
    pip install pytz openpyxl python-dateutil
    ```
   - Or install it using **Pip manager** by pressing the plus icon and using the name.

2. **Set Up Your Files:**
   - Prepare your Excel workbooks. Ensure the file paths are correctly referenced in your "links_file_path = 'C:/linkspath.txt'" file, with the input & output file path on the first and third lines.
   - In this current version we specify the paths to excel file under variable **links_file_path = 'C:/linkspath.txt'** inside txt file and then read it and use line 1 as the file where we choose the range of rows and line 3 with Scheduled tasks file, remember to close the second sheet before running the script!!!

3. **Set Up Your current CMS Schedule sheet name:**
   - Input the correct name of this month sheet name like: 
   
    ```
    workbook_name = 'May2024'
    ```

Usual error for this step is misspelling of Start Description in excel sheet, or new time zone which we didn't already specify in our zone names collection.


4. **Execute the Script:**
   - Copy the script below into a Jupyter notebook code cell or a Python file.

5. **Run the Script:**
   - Execute the script in your chosen environment (Jupyter notebook or VS Code Jupyter extension).
   - Enter the start and end row numbers when prompted.

6. **Debugging**

Script is printing in console every row from the range you specify from the start/end row and skips the rows which includes our counting or blanks, you can troubleshoot the errors with this output, try to verify the correct format like:

> Collection name AWS68 Bravado Webshop Germany PROD <br>
> Start Description: 1st week after Patch Tuesday, Monday <br>
> Start Time: 2AM <br>
> Start Timezone: CET/CEST <br>
> Duration (hours): 4 <br>
> Found timezone: Europe/Berlin <br>
> Executing 'after Patch Tuesday' logic... <br>
> 
> Original Converted date to mapped Europe/Berlin Start Time Zone: <br>
> Start Date : 2024-03-18 02:00:00 <br>
> End Date: 2024-03-18 06:00:00 <br>
> 
> Converted to Europe/London Target Time Zone: <br>
> Start Date : 2024-03-18 01:00:00 <br>
> End Date: 2024-03-18 05:00:00 <br>

7. **Common Errors**

  - **Misspelled Start Description:** Ensure the start description in the Excel sheet is spelled correctly.
  - **New Time Zone:** Add any new time zones to the `timezone_mapping` dictionary.
  - **Opened Excel Sheet:** Close the Excel sheet before running the script to allow the script to update the file.

