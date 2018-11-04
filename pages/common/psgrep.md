# psgrep

> Search through processes with grep.

- Find process lines containing a specific string:

`psgrep {{'foo'}}`

- Find process lines containing a specific string excluding headers:

`psgrep -n {{'foo'}}`

- Search using simplified format (PID, user, command):

`psgrep -s {{'foo'}}`
