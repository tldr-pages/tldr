# pm

> Display information about apps on an Android device.
> More information: <https://developer.android.com/tools/adb#pm>.

- List all installed apps:

`pm list packages`

- List all installed [s]ystem apps:

`pm list packages -s`

- List all installed [3]rd-party apps:

`pm list packages -3`

- List apps matching specific keywords:

`pm list packages {{keyword1 keyword2 ...}}`

- Display a path of the APK of a specific app:

`pm path {{app}}`
