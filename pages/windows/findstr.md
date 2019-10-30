# findstr

> Find specified text within one or more files.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/findstr>.

- Find space-separated string(s) in all files:

`findstr "{{query}}" *`

- Find space-separated string(s) in all files recur[s]ively:

`findstr /s "{{query}}" *`

- Find a literal string (containing spaces) in all text files:

`findstr /c:"{{query}}" *.txt`

- Find only lines that match the query e[x]actly:

`findstr /x "{{query}}" *`

- Find case [i]nsensitive, [r]egex string(s) in all files recur[s]ively, with line [n]umbered results:

`findstr /rins "{{query}}" *`

- Find space-separated string(s) in a piped command's output:

`{{dir}} | findstr "{{query}}"`

- Display only the filenames that contain a match:

`findstr /m "{{query}}" *`
