# adb shell getprop

> Show information about adb devices and emulators.
> More information: <https://adbinstaller.com/commands/adb-shell-getprop-5b59efc4fe030a2fc178d839>.

- Print information about the Android system properties:

`adb shell getprop`

- Print information about a specific property:

`adb shell getprop {{prop}}`

- Print the SDK API level:

`adb shell getprop {{ro.build.version.sdk}}`

- Print the Android version:

`adb shell getprop {{ro.build.version.release}}`

- Print the Android device model:

`adb shell getprop {{ro.vendor.product.model}}`

- Print the OEM unlock status:

`adb shell getprop {{ro.oem_unlock_supported}}`

- Print the MAC address of the Android's WiFi card:

`adb shell getprop {{ro.boot.wifimacaddr}}`
