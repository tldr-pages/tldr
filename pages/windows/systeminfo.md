# systeminfo

> Display operating system configuration for a local or remote machine.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/systeminfo>.

- Display system configuration for the local machine:

`systeminfo`

- Display system configuration in a specified output format:

`systeminfo /fo {{table|list|csv}}`

- Display system configuration for a remote machine:

`systeminfo /s {{remote_name}} /u {{username}} /p {{password}}`

- Display detailed usage information:

`systeminfo /?`
