# planmaker

> SoftMaker Office's spreadsheet application.
> More information: <https://help.softmaker.com/planmaker2026/en/index.html>

- Launch the spreadsheet application (omitting the file path will create a new blank document):

`planmaker {{path\to\file.pmdx}}`

- Launch PlanMaker with [N]o open documents:

`planmaker -N`

- Launch PlanMaker with an interactive dialog to choose which [F]ile to [O]pen:

`planmaker -FO`

- Launch PlanMaker with an interactive dialog to choose which template [F]ile to create a [N]ew document:

`planmaker -FN`

- Directly [P]rint a document to the default printer:

`planmaker -P"{{path\to\file.pmdx}}"`

- Directly print a document to a specific printer:

`planmaker -Q"{{printer}}","{{path\to\file.pmdx}}"`
