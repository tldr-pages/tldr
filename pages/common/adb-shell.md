# adb shell

> Android Debug Bridge Shell: Run remote shell command with an Android emulator instance or connected Android devices.
> More information: <https://developer.android.com/studio/command-line/adb>.

- Start a remote interactive shell in the emulator/device:

`adb shell`

- Reset dangerous permissions to an application:

`adb shell pm reset-permissions {{package}}`

- Revoke a dangerous permission to an application:

`adb shell pm revoke {{package}} {{permission}}`

- Trigger a key event:

`adb shell input keyevent {{keycode}}`

- Clear the data from an emulator/device's application:

`adb shell pm clear {{package}}`

- Start an activity on emulator/device:

`adb shell am start -n {{package}}/{{activity}}`

- Start home activity on emulator/device:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
