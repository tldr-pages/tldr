# excel

> Microsoft Office's spreadsheet application.
> More information: <https://support.microsoft.com/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6#category=excel>.

- Launch the spreadsheet application (omitting the file path will launch the File page):

`excel {{path\to\file.xlsx}}`

- Create a new workbook with a [m]acro-enabled sheet:

`excel /m`

- Open a workbook as a [t]emplate:

`excel {{[/n|/t]}} {{path\to\file.xlsx}}`

- Start Microsoft Excel in [s]afe Mode:

`excel {{[/s|/safemode]}}`
