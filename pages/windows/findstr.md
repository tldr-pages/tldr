# findstr

> Find specified text within one or more files.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/findstr>.

- Find one or more strings in all files:

`findstr "{{string1 string2 ...}}" *`

- Find one or more strings in a piped command's output:

`{{dir}} | findstr "{{string1 string2 ...}}"`

- Find one or more strings in all files recur[s]ively:

`findstr /s "{{string1 string2 ...}}" *`

- Find strings using a case-[i]nsensitive search:

`findstr /i "{{string1 string2 ...}}" *`

- Find strings in all files using `regex`:

`findstr /r "{{regex}}" *`

- Find a literal string (containing spaces) in all text files:

`findstr /c:"{{string1 string2 ...}}" *.txt`

- Display the line [n]umber before each matching line:

`findstr /n "{{string1 string2 ...}}" *`

- Display only the filenames that contain a [m]atch:

`findstr /m "{{string1 string2 ...}}" *`
