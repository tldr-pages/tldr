# adb-logcat

> Dump a log of system messages.
> More information: <https://developer.android.com/studio/command-line/logcat>.

- Display system logs:

`adb logcat`

- Display lines that match a regular expression:

`adb logcat -e {{regular_expression}}`

- Filter the log with filterspecs(`{{complete_tag:[V | D | I | W | E | F | S]}}`), `*` for all but not a wildcard(`*:S` suppresses others):

`adb logcat {{tag0:V}} {{tag1:D}} *:S`

- Color the log(usually use with filters):

`adb logcat -v color`