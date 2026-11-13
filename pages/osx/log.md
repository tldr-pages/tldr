# log

> View, export, and configure macOS unified logs.
> More information: <https://keith.github.io/xcode-man-pages/log.1.html>.

- Show logs from the past 30 minutes in a compact format:

`log show --last 30m --style compact`

- Show logs from a specific process during the past hour:

`log show --last 1h --predicate 'process == "{{process_name}}"'`

- Search messages from the past hour for text, ignoring case and including info and debug messages:

`log show --info --debug --last 1h --predicate 'eventMessage CONTAINS[c] "{{search_text}}"'`

- Show logs between two dates and times:

`log show --start "{{YYYY-MM-DD HH:MM:SS}}" --end "{{YYYY-MM-DD HH:MM:SS}}"`

- Stream live system logs:

`log stream`

- Stream live logs from a process with a specific PID:

`log stream --process {{process_id}}`

- Export logs from the past hour to an archive:

`sudo log collect --last 1h --output {{path/to/file.logarchive}}`
