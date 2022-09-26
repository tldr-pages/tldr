# fastboot

> Se comunica com dispositivos Android conectados quando iniciados no modo _fastboot_ (o único lugar em que `adb` não funciona).
> Mais informações: <https://cs.android.com/android/platform/superproject/+/master:system/core/fastboot>.

- Desbloqueia o bootloader:

`fastboot oem unlock`

- Bloqueia o bootloader novamente:

`fastboot oem lock`

- Reinicia o dispositivo no modo fastboot para o modo fastboot novamente:

`fastboot reboot bootloader`

- Flasheia uma imagem:

`fastboot flash {{arquivo.img}}`

- Flasheia uma imagem de _recovery_ customizada:

`fastboot flash recovery {{arquivo.img}}`

- Exibe os dispositivos conectados:

`fastboot devices`

- Mostra todas as informações de um dispositivo:

`fastboot getvar all`
