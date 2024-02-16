# adb logcat

> Dump a log of system messages.
> More information: <https://developer.android.com/tools/logcat>.

- Display system logs:

`adb logcat`

- Display lines that match a regular [e]xpression:

`adb logcat -e {{regular_expression}}`

- Display logs for a tag in a specific mode ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), filtering other tags:

`adb logcat {{tag}}:{{mode}} *:S`

- Display logs for React Native applications in [V]erbose mode [S]ilencing other tags:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Display logs for all tags with priority level [W]arning and higher:

`adb logcat *:W`

- Display logs for a specific PID:

`adb logcat --pid={{pid}}`

- Display logs for the process of a specific package:

`adb logcat --pid=$(adb shell pidof -s {{package}})`

- Color the log (usually use with filters):

`adb logcat -v color`
