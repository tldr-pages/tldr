# fastboot

> Comunicați cu dispozitivele Android conectate atunci când sunt în modul bootloader (singurul loc `adb` nu funcționează).
> Mai multe informaţii: <https://android.googlesource.com/platform/system/core/+/master/fastboot/#fastboot>

- Deblocați bootloader-ul:

`fastboot oem unlock`

- Reblocați încărcătorul de boot:

`fastboot oem lock`

- Reporniți din nou dispozitivul din modul fastboot în modul fastboot:

`fastboot reboot bootloader`

- Flash o imagine dată:

`fastboot flash {{file.zip}}`

- Flash o imagine de recuperare personalizată:

`fastboot flash recovery {{file.img}}`

- Dispozitive conectate de afișare:

`fastboot devices`

- Afișează toate informațiile unui dispozitiv:

`fastboot getvar all`
