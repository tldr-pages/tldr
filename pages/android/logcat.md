# logcat

> Dump a log of system messages, including stack traces when the device throws an error and messages that you have written from your app with the Log class.
> More information: <https://developer.android.com/studio/command-line/logcat>.

- Display system logs:

`logcat`

- Write system logs to a file:

`logcat -f {{path/to/file}}`

- Display lines that match a regular expression:

`logcat --regex {{regular_expression}}`
