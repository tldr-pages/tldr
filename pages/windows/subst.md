# subst

> Associates a path with a virtual drive letter.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/subst>.

- List active associations:

`subst`

- Add an association:

`subst {{Z:}} {{C:\Python2.7}}`

- Remove an association:

`subst {{Z:}} /d`
