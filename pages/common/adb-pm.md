# pm

> Android Package Manager tool. Use via `adb shell pm` to manage packages, permissions, users, features, and system information.
> More information: <https://developer.android.com/tools/adb>.

- Print the path to the APK of a package:

`adb shell pm path {{package}}`

- Install an app package from a given path:

`adb shell pm install {{/path/to/app.apk}}`

- Uninstall a package from the device:

`adb shell pm uninstall {{package}}`

- Clear all app data for a package:

`adb shell pm clear {{package}}`

- Enable a package or component:

`adb shell pm enable {{package_or_class}}`

- Disable a package or component:

`adb shell pm disable {{package_or_class}}`

- Grant a permission for an app:

`adb shell pm grant {{package}} {{permission}}`

- Revoke a permission for an app:

`adb shell pm revoke {{package}} {{permission}}`
