# ftype

> Print or modify file types used for file extension association.
> See also: `assoc`.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/ftype>.

- Print all file types:

`ftype`

- Print the associated program for a given file type (txtfile):

`ftype {{txtfile}}`

- Set/remove the associated program (Windows\System32\notepad.exe) for a given file type (txtfile):

`ftype {{txtfile}}="{{Windows\System32\notepad.exe|}}"`
