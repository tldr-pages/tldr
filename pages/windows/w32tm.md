# w32tm

> Query and control w32time time synchronization service on Windows from the command-line.
> More information: <https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings>.

- Get packet info:

`w32tm /stripchart /packetinfo /samples:1 /computer:{{time_server}}`

- 2 seconds:

`w32tm /stripchart /computer:{{time_server}}`

- State of the time syncronization:

`w32tm /query /status /verbose`

- Peer statistics:

`w32tm /query /peers`

- (run in elevated console):

`w32tm /query /configuration`

- (run in elevated console):

`w32tm /resync /force`

- (run in elevated console):

`w32tm /debug /enable /file:{{path\to\debug.log}} /size:{{10000000}} /entries:{{0-300}}`
