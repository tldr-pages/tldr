# logcat

> Dump a log of system messages, including stack traces when an error occurred, and information messages logged by applications.
> More information: <https://developer.android.com/tools/logcat>.

- Display system logs:

`logcat`

- Write system logs to a [f]ile:

`logcat -f {{path/to/file}}`

- Display lines that match a regular expression:

`logcat --regex {{regular_expression}}`

- Display logs for a specific PID:

`logcat --pid={{pid}}`

- Display logs for the process of a specific package:

`logcat --pid=$(pidof -s {{package}})`
