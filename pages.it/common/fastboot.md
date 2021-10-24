# fastboot

> Comunica con il dispositivo Android connessione quando in modalità bootloader (la situazione in cui `adb` non funziona).
> Maggiori informazioni: <https://cs.android.com/android/platform/superproject/+/master:system/core/fastboot>.

- Sblocca il bootloader:

`fastboot oem unlock`

- Ri-blocca il bootloader:

`fastboot oem lock`

- Riavvia il dispositivo da modalità fastboot, nuovamente in modalità fastboot:

`fastboot reboot bootloader`

- Esegue in Flash di una data immagine:

`fastboot flash {{file.img}}`

- Esegue il Flash di una recovery image personalizzata:

`fastboot flash recovery {{file.img}}`

- Mostra i dispositivi connessi:

`fastboot devices`

- Mostra tutte le informazioni su un dispositivo:

`fastboot getvar all`
