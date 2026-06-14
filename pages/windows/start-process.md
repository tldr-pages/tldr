# Start-Process

> Start a command in a new console.
> Can also be used to run Windows programs registered in the `App Paths` Windows Registry despite not registered in `PATH` environment variable.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/start-process>.

- Open a specific directory on Windows Explorer (equivalent to `explorer {{path\to\directory}}`):

`start {{path\to\directory}}`

- Start a specific Windows program file (command-line programs will open on a new console window):

`start {{path\to\file}}`

- Start a registered Windows program name and pass its command arguments:

`start {{msedge}} {{--inprivate example.com}}`

- Start a Windows program in minimized or maximized window mode:

`Start-Process -WindowStyle {{Minimized|Maximized}} {{program}}`

- Start a command or Windows program with a specified working directory:

`Start-Process -WorkingDirectory {{path\to\directory}} {{command_or_program}}`

- Do not finish this command until the target command or program exits:

`Start-Process -Wait {{command_or_program}}`
