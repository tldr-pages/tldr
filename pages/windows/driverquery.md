# driverquery

> Display information about installed device drivers.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- Print all drivers:

`driverquery`

- Print all drivers in the specified format:

`driverquery /fo {{table|list|csv}}`

- Print all drivers with the column to indicate if they are signed:

`driverquery /si`

- Exclude the header in the output list:

`driverquery /nh`

- Print all drivers for the remote machine:

`driverquery /s {{hostname}} /u {{username}} /p {{password}}`

- Print all drivers in the verbose format:

`driverquery /v`

- Print the help:

`driverquery /?`
