# pm

> Android package manager.
> More information: <https://developer.android.com/studio/command-line/adb.html#pm>.

- Display a list of installed packages:

`pm list packages`

- Display a list of users on this system:

`pm list users`

- Get the path to the APK file of an installed package:

`pm path {{com.android.contacts}}`

- Install a package:

`pm install {{path/to/file.apk}}`

- Uninstall a package:

`pm uninstall {{com.android.contacts}}`
