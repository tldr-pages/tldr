# getprop

> Show information about adb devices and emulators.
> More information: <https://adbinstaller.com/commands>.

- Print information about the Android system properties:

`getprop`

- Print information about a specific property:

`getprop {{prop}}`

- Print the SDK API level:

`getprop {{ro.build.version.sdk}}`

- Print the Android version:

`getprop {{ro.build.version.release}}`

- Print the Android device model:

`getprop {{ro.vendor.product.model}}`

- Print the OEM unlock status:

`getprop {{ro.oem_unlock_supported}}`

- Print the MAC address of the Android's WiFi card:

`getprop {{ro.boot.wifimacaddr}}`
