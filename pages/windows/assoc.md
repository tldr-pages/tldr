# assoc

> Display or modify file extension associations.
> See also: `ftype`.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/assoc>.

- Print all associated filetypes:

`assoc`

- Print the associated filetype for a given extension (.txt):

`assoc {{.txt}}`

- Set/remove the associated filetype (txtfile) for a given extension (.txt):

`assoc {{.txt}}={{txtfile| }}`
