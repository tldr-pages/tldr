# WMIC

> Interactive shell for detailed information about running processes.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/wmic>.

- Fundamental grammar:

`wmic [alias] [where claus] [verb clause]`

- Brief details about running processes:

`wmic process list brief`

- Full details about running processes:

`wmic process list full`

- Access specific fields such as process name, process ID and parent process ID:

`wmic process get name,processid,parentprocessid`

- Focus on a specific process:

`wmic process where name="example.exe" list full`

- Access specific fields for a a specific process:

`wmic process where processid=pid get name,commandline`

- Kill a process:

`wmic process PID delete`
