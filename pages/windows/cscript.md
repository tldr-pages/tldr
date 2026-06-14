# cscript

> Run Windows Script Host programs in the command-line interface (CLI).
> See also: `wscript` for graphical user interface (GUI).
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cscript>.

- Set `cscript` (CLI) or `wscript` (GUI) as the default interpreter to run Windows Script Host programs:

`cscript //h:{{cscript|wscript}}`

- Run a script:

`cscript {{path\to\file}}`

- Run script in the [i]nteractive or [b]atch mode (enable or suppress alerts, prompts, and scripting errors):

`cscript //{{i|b}} {{path\to\file}}`

- Show or hide the Windows Script Host logo before running (useful to get Host version / suppress outputs):

`cscript {{//logo|//nologo}} {{path\to\file}}`

- Specify an custom execution engine to run the script (useful for using custom script filenames):

`cscript //e:{{jscript|vbscript|custom_engine}} {{path\to\file}}`

- Set a [t]imeout for running a given script (in seconds):

`cscript //t:{{timeout}} {{path\to\file}}`

- Start [d]ebugger and wait until a scripting error occurs:

`cscript //d {{path\to\file}}`

- Start debugging from the first script line in an IDE (e.g., Visual Studio):

`cscript //x {{path\to\file}}`
