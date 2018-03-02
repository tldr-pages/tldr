# yank

> Read input from stdin and display a selection interface that allows a field to be selected and copied to the clipboard.

- Yank an environment variable key or value:

`env | yank -d =`

- Yank a field from a CSV file:

`yank -d \", <file.csv`

- Yank a whole line using the -l option:

`make 2>&1 | yank -l`

- If stdout is not a terminal the selected field will be written to stdout and exit without invoking the yank command. Kill the selected PID:

`ps ux | yank -g [0-9]+ | xargs kill`

- Yank the selected field to the clipboard as opposed of the default primary clipboard:

`yank -- xsel -b`
