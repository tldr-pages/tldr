# presentations

> SoftMaker Office's presentation application.
> See also: `basicmaker`, `planmaker`, `textmaker`.
> More information: <https://help.softmaker.com/presentations2026/en/index.html>.

- Launch the presentation application (omitting the file path will create a new blank document):

`presentations {{path\to\file.prdx}}`

- Launch Presentations with [N]o open documents:

`presentations -N`

- Launch Presentations with an interactive dialog to choose which [F]ile to [O]pen:

`presentations -FO`

- Launch Presentations with an interactive dialog to choose which template [F]ile to create a [N]ew document:

`presentations -FN`

- Directly [P]rint a document to the default printer:

`presentations -P"{{path\to\file.prdx}}"`

- Directly print a document to a specific printer:

`presentations -Q"{{printer}}","{{path\to\file.prdx}}"`
