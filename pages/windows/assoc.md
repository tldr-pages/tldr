# assoc

> Display or change the default program which handles specific file types 
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/assoc>.

- List all file types with their default program which uses them:

`assoc`

- Display the associated file type for a specific extension:

`assoc {{.txt}}`

- Set the associated file type for a specific extension:

`assoc .{{txt}}={{txtfile}}`
