# gpupdate

> A tool to check and apply Windows Group Policy settings.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/gpupdate>.

- Check and apply updated Group Policy settings:

`gpupdate`

- Specify the target Group Policy settings to check for update:

`gpupdate /target:{{computer|user}}`

- Force all Group Policy settings to be reapplied:

`gpupdate /force`

- Display detailed usage information:

`gpupdate /?`
