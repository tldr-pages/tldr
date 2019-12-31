# androguard

> Reverse engineering tool for Android applications. Written in Python.
> More information: <https://github.com/androguard/androguard>.

- Display Android app manifest:

`androguard axml {{path/to/app.apk}}`

- Display app metadata (version and app ID):

`androguard apkid {{path/to/app.apk}}`

- Decompile Java code from an app:

`androguard decompile {{path/to/app.apk}} --output {{path/to/directory}}`
