# aapt

> Android Asset Packaging Tool.
> Tool that compiles and packages Android app’s resources.
> More information: https://developer.android.com/studio/command-line/aapt2.

- List files contained in an APK archive:

`aapt list {{path/to/app.apk}}`

- Display app metadata (version, permissions, etc.):

`aapt dump badging {{path/to/app.apk}}`

- Create a new APK archive with files from the specified directory:

`aapt package -F {{path/to/app.apk}} {{path/to/directory}}`
