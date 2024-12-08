
# Fill SfD from Schedule

This guide will help you use the provided Python script to fill SFD table with CR numbers and dates. The easiest way to run this script is by using the Visual Studio Code Jupyter extension or the Jupyter notebook application for Google Chrome.

## Prerequisites

### Option 1: Visual Studio Code Jupyter Extension
1. Install Visual Studio Code: [Download VS Code](https://code.visualstudio.com/download)
2. Install the Jupyter extension: [Visual Studio Marketplace - Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
3. Install Pip manager : [Pip manager](https://marketplace.visualstudio.com/items?itemName=slightc.pip-manager)

### Option 2: Jupyter Notebook in Google Chrome
1. Open Jupyter Lab in your browser: [Try Jupyter](https://jupyter.org/try-jupyter/lab/)
2. Save Jupyter Lab as an application on your PC for easy access.

## Running the Script

1. **Prepare the Environment:**
   - Script is using python library pytz for time zone calculation, we specify it under start_timezone and tasks_timezone variables.
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
   
   - Prepare your Excel sheets. Ensure that the folder path with actual downloaded tables is correctly referenced in your "file_path = r'C:/folder/path/excels'".

4. **Set Up Your current CMS Schedule sheet name:**
   - Input the correct name of this month sheet name like: 
   
    ```
    input_sheet_name = 'December2024'
    ```

5. **Execute the Script:**

   - Copy the repository in VS Code or simply Copy the script below into a Jupyter notebook code cell or a Python file

6. **Run the Script:**

   - Execute the script in your chosen environment (Jupyter notebook or VS Code Jupyter extension - .ipynb file extension).
   - Enter the start and end row numbers when prompted.

8. **Printing on execution**

   - Scipt do not print anything in case of success

10. **Copying to the sharepoint excels:**

   - If you decide to merge local excels with Sharepoint(not neccessary), proceed as instructed below:
       - Press CTRL + A and CTRL + C inside updated sheet
       - Press CTRL + A and paste with ctrl+shift+v into needed excel

11. **Errors during the script execution**
    
   - There might be None under CR number because of blank cell in CMS schedule.
   - There can be an error because of opened Calendar excel sheet which denies rewriting on top of it and needs to be closed for the scipt to update the file.
