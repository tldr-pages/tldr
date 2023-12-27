# fastboot

> Communicate with connected Android devices when in bootloader mode (the one place `adb` doesn't work).
> More information: <https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

- Unlock the bootloader:

`fastboot oem unlock`

- Relock the bootloader:

`fastboot oem lock`

- Reboot the device from fastboot mode into fastboot mode again:

`fastboot reboot bootloader`

- Flash a given image:

`fastboot flash {{path/to/file.img}}`

- Flash a custom recovery image:

`fastboot flash recovery {{path/to/file.img}}`

- Display connected devices:

`fastboot devices`

- Display all information of a device:

`fastboot getvar all`
