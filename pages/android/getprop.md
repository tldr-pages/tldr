# getprop

> Show information about adb devices and emulators.
> More information: <https://manned.org/getprop>.

- Display information about the Android system properties:

`getprop`

- Display information about a specific property:

`getprop {{prop}}`

- Display the SDK API level:

`getprop {{ro.build.version.sdk}}`

- Display the Android version:

`getprop {{ro.build.version.release}}`

- Display the Android device model:

`getprop {{ro.vendor.product.model}}`

- Display the OEM unlock status:

`getprop {{ro.oem_unlock_supported}}`

- Display the MAC address of the Android's WiFi card:

`getprop {{ro.boot.wifimacaddr}}`
