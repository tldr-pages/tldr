# w32tm

> Query and control the w32time time synchronization service.
> More information: <https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings>.

- Show the current status of time synchronization:

`w32tm /query /status /verbose`

- Show a time offset graph against a time server:

`w32tm /stripchart /computer:{{time_server}}`

- Show an NTP reply from a time server:

`w32tm /stripchart /packetinfo /samples:1 /computer:{{time_server}}`

- Show the state of the currently used time servers:

`w32tm /query /peers`

- Show configuration of the w32time service (run in elevated console):

`w32tm /query /configuration`

- Force time resynchronization immediately (run in elevated console):

`w32tm /resync /force`

- Write w32time debug logs into a file (run in elevated console):

`w32tm /debug /enable /file:{{path\to\debug.log}} /size:{{10000000}} /entries:{{0-300}}`
