# wscript

> Run Windows Script Host programs in the graphical user interface (GUI).
> See also: `cscript` for command-line interface (CLI).
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cscript>.

- Set `cscript` (CLI) or `wscript` (GUI) as the default interpreter to run Windows Script Host programs:

`wscript //h:{{cscript|wscript}}`

- Run a script:

`wscript {{path\to\file}}`

- Run script in the [i]nteractive or [b]atch mode (enable or suppress alerts, prompts, and scripting errors):

`wscript //{{i|b}} {{path\to\file}}`

- Show or hide the Windows Script Host logo before running (useful to get Host version / suppress outputs):

`wscript {{//logo|//nologo}} {{path\to\file}}`

- Specify an custom execution engine to run the script (useful for using custom script filenames):

`wscript //e:{{jscript|vbscript|custom_engine}} {{path\to\file}}`

- Set a [t]imeout for running a given script (in seconds):

`wscript //t:{{timeout}} {{path\to\file}}`

- Start [d]ebugger and wait until a scripting error occurs:

`wscript //d {{path\to\file}}`

- Start debugging from the first script line in an IDE (e.g., Visual Studio):

`wscript //x {{path\to\file}}`
