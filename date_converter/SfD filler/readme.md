**fill SfD from schedule**

Easiest way for running this is by Visual Studio code Jupyter extension or using Jupyter notebook google chrome application which you can save as additional app on your pc

Script is using python library pytz for time zone calculation as we convert the time from schedule to *PST* time for our SfD format

Currently we use workbook.active which means that it opens the current active workbook inside Schedule sheet.

Script is asking for the range of rows which you choose from Schedule.

Scipt do not print anything in case of success

In this current version we specify the paths to two excel files inside .txt file and then read it and use line 0 as the file with the *Schedule* where we choose the range of rows and line 1 with *Calendar* sheet which we fill



There can be an error because of opened excel sheet which denies rewriting on top of it and needs to be closed for the scipt to update the file.