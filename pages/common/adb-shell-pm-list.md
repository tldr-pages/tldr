# adb shell pm list

> Android Package Manager tool. List users, packages, permissions, instrumentation, permission groups, features and libraries.
> More information: <https://developer.android.com/tools/adb>.

- List all installed packages

`adb shell pm list packages`

- Print all users on the system

`adb shell pm list users`

- Print all known permission groups

`adb shell pm list permission-groups`

- Print all known permissions

`adb shell pm list permissions`

- List all test packages

`adb shell pm list instrumentation`

- Print all features of the system

`adb shell pm list features`

- Print all the libraries supported by the current device

`adb shell pm list libraries`
