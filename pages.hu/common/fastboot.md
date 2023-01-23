# fastboot

> Kommunikáció a csatlakoztatott Android eszközökkel bootloader módban (az egyetlen hely, ahol a `adb` nem működik). További információ: <https://cs.android.com/android/platform/superproject/+/master:system/core/fastboot>.

- A bootloader feloldása:

`fastboot oem unlock`

- A bootloader újbóli zárolása:

`fastboot oem lock`

- Indítsa újra a készüléket fastboot módból fastboot módba:

`fastboot reboot bootloader`

- Egy adott image flashelése:

`fastboot flash {{file.img}}`

- Egyéni helyreállítási kép flashelése:

`fastboot flash recovery {{file.img}}`

- Csatlakoztatott eszközök megjelenítése:

`fastboot devices`

- Egy eszköz összes információjának megjelenítése:

`fastboot getvar all`
