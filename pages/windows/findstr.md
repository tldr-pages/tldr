# findstr

> Find specified text within one or more files.

- Find space-separated string(s) in all files:

`findstr "{{query}}" *`

- Find space-separated string(s) in all files recur[s]ively:

`findstr /s "{{query}}" *`

- Find strings using a case-insensitive search:

`findstr /i "{{query}}" *"`

- Find strings in all files using regular expressions:

`findstr /r "{{expression}}" *`

- Find a literal string (containing spaces) in all text files:

`findstr /c:"{{query}}" *.txt`

- Find only lines that match the query e[x]actly:

`findstr /x "{{query}}" *`

- Display the line number before each matching line:

`findstr /n "{{query}}" *`

- Display only the filenames that contain a match:

`findstr /m "{{query}}" *`
