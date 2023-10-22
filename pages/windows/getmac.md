# getmac

> Display the MAC addresses of a system.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>.

- Display the MAC addresses for the current system:

`getmac`

- Display the details in a specific format:

`getmac /fo {{table|list|csv}}`

- Exclude the header in the output list:

`getmac /nh`

- Display the MAC addresses for a remote machine:

`getmac /s {{hostname}} /u {{username}} /p {{password}}`

- Display the MAC addresses with verbose information:

`getmac /v`

- Display detailed usage information:

`getmac /?`
