# assoc

> Display or change associations of file names.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/assoc>.

- List all associated file types:

`assoc`

- Display the associated file type for a specific extension:

`assoc {{.txt}}`

- Set the associated file type for a specific extension:

`assoc .{{txt}}={{txtfile}}`
