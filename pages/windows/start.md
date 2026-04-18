# start

> Start a command in a new console.
> Can also be used to run Windows programs registered in the `App Paths` Windows Registry despite not registered in `PATH` environment variable.
> In PowerShell, this command is an alias of `Start-Process`. This documentation is based on the Command Prompt (`cmd`) version of `start`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/start>

- View the documentation of the equivalent PowerShell command:

`tldr start-process`

- Start a new shell window with a custom title:

`start "{{window_title}}" {{cmd|powershell|python|...}}`

- Open a specific directory on Windows Explorer (equivalent to `explorer {{path\to\directory}}`):

`start {{path\to\directory}}`

- Start a specific Windows program file (command-line programs will open on a new console window):

`start {{path\to\file}}`

- Start a registered Windows program name and pass its command arguments:

`start {{msedge}} {{--inprivate example.com}}`

- Start a Windows program in minimized or maximized window mode:

`start {{/min|/max}} {{program}}`

- Start a command or Windows program with a specified working directory:

`start /d {{path\to\directory}} {{command_or_program}}`

- Do not finish this command until the target command or program exits:

`start /wait {{command_or_program}}`
