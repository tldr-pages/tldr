# adb-install

> Android Debug Bridge Install: Push packages to an Android emulator instance or connected Android devices.
> More information: <https://developer.android.com/studio/command-line/adb>.

- Push an Android application to an emulator/device:

`adb install {{path/to/file.apk}}`

- Reinstall an existing app, keeping its data:

`adb install -r {{path/to/file.apk}}`

- Grant all permissions listed in the app manifest:

`adb install -g {{path/to/file.apk}}`

- Quickly update an installed package by only updating the parts of the APK that changed:

`adb install --fastdeploy {{path/to/file.apk}}`
