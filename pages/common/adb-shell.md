# adb shell

> Run shell commands on a connected Android device or emulator.
> More information: <https://developer.android.com/tools/adb>.

- Start a remote interactive shell on the emulator or device:

`adb shell`

- Get all the properties from emulator or device:

`adb shell getprop`
- View documentation for showing Android system properties:

`tldr {{[-p|--platform]}} android getprop`

- Revert all runtime permissions to their default:

`adb shell pm reset-permissions`

- Revoke a permission for an application:

`adb shell pm revoke {{package}} {{permission}}`

- Trigger a key event:

`adb shell input keyevent {{keycode}}`

- Clear the data of an application on an emulator or device:

- View documentation for the Android package manager:

`tldr {{[-p|--platform]}} android pm`

-View documentations for sending event codes and touchscreen events:

`tldr {{[-p|--platform]}} android input`

- Start an activity on emulator or device:

`adb shell am start -n {{package}}/{{activity}}`

- Start the home activity on an emulator or device:

- View documentation for the Android activity manager:

`tldr {{[-p|--platform]}} android am`
