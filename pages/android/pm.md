# pm

> Android Package Manager tool.
> More information: <https://developer.android.com/tools/adb#pm>.

- List installed packages:

`pm list packages`

- Install an app package from a given path:

`pm install /{{path/to/app}}.apk`

- Uninstall a package from the device:

`pm uninstall {{package}}`

- Clear all app data for a package:

`pm clear {{package}}`

- Enable a package or component:

`pm enable {{package_or_class}}`

- Disable a package or component:

`pm disable-user {{package_or_class}}`

- Grant a permission for an app:

`pm grant {{package}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Revoke a permission for an app:

`pm revoke {{package}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
