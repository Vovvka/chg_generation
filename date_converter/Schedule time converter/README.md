**convert_time_in_calendar**
------------------------

Easiest way for running this is by Visual Studio code Jupyter extension or using Jupyter notebook google chrome application which you can save as additional app on your pc <br>
https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter <br>
or <br>
https://jupyter.org/try-jupyter/lab/

Script is using python library pytz for time zone calculations, we have timezone_mapping variable where we specify custom time zones which are not in standartized format: 

    timezone_mapping = {
        
        'custom zone from our sheet': 'time zone from pytz zones list which can be found in pytz_timezones', 
    }

We choose to convert from the respective time zones to our main time zone *Europe/London* which is default in snow for our accounts.

Currently we use workbook.active which means that it opens the current active workbook.

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


Usual error for this step is misspelling of Start Description in excel sheet, or new time zone which we didn't already specify in our zone names collection.

In this current version we specify the paths to two excel files inside txt file and then read it and use line 0 as the file where we choose the range of rows and line 1 with sheet which we fill, it can be the same file specified two times but remember to close the sheet before running the script.

There can be an error because of opened excel sheet which denies rewriting on top of it and needs to be closed for the scipt to update the file.
