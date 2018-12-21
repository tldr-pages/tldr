# psgrep

> Search through processes with grep.

- Find process lines containing a specific string:

`psgrep {{process_name}}`

- Find process lines containing a specific string, do not include headers:

`psgrep -n {{process_name}}`

- Search using simplified format (PID, user, command):

`psgrep -s {{process_name}}`
