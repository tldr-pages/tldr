# adb shell pm

> Android Package Manager tool.
> More information: <https://developer.android.com/tools/adb>.

- List installed packages:

`adb shell pm list packages`

- Install an app package from a given path:

`adb shell pm install /{{path/to/app.apk}}`

- Uninstall a package from the device:

`adb shell pm uninstall {{package}}`

- Clear all app data for a package:

`adb shell pm clear {{package}}`

- Enable a package or component:

`adb shell pm enable {{package_or_class}}`

- Disable a package or component:

`adb shell pm disable-user {{package_or_class}}`

- Grant a permission for an app:

`adb shell pm grant {{package}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Revoke a permission for an app:

`adb shell pm revoke {{package}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
