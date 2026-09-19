# basicmaker

> SoftMaker Office's BASIC macro editor application.
> More information: <https://help.softmaker.com/basicmaker2026/en/index.html>.

- Launch the macro editor (omitting the file path will create a new blank file):

`basicmaker {{path\to\file.bas}}`

- Open a script and navigate to a specific line:

`basicmaker -Line={{line_number}} "{{path\to\file.bas}}"`

- Run a specific macro script [S]ilently in the background:

`basicmaker -S "{{path\to\file.bas}}"`

- Launch PlanMaker with [N]o open macro scripts:

`basicmaker -N`

- Launch PlanMaker with an interactive dialog to choose which [F]ile to [O]pen:

`basicmaker -FO`

- Directly [P]rint a macro script to the default printer:

`basicmaker -P"{{path\to\file.bas}}"`

- Directly print a macro script to a specific printer:

`basicmaker -Q"{{printer}}","{{path\to\file.bas}}"`
