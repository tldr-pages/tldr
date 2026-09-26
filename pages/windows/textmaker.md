# textmaker

> SoftMaker Office's word processor application.
> More information: <https://help.softmaker.com/textmaker2026/en/index.html>.

- Launch the word processor application (omitting the file path will create a new blank document):

`textmaker {{path\to\file.tmdx}}`

- Launch TextMaker with [N]o open documents:

`textmaker -N`

- Launch TextMaker with an interactive dialog to choose which [F]ile to [O]pen:

`textmaker -FO`

- Launch TextMaker with an interactive dialog to choose which template [F]ile to create a [N]ew document:

`textmaker -FN`

- Directly [P]rint a document to the default printer:

`textmaker -P"{{path\to\file.tmdx}}"`

- Directly print a document to a specific printer:

`textmaker -Q"{{printer}}","{{path\to\file.tmdx}}"`
