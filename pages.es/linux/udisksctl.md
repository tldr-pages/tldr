# udisksctl

> Interactúa con `udisksd` para consultar y manipular dispositivos de almacenamiento.
> Vea también: `mount`.
> Más información: <https://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- Muestra información general sobre unidades de disco y dispositivos de bloque:

`udisksctl status`

- Muestra información detallada sobre un dispositivo:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdX}}`

- Muestra información detallada sobre una partición de un dispositivo:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdXN}}`

- Monta una partición de un dispositivo y muestra el punto de montaje:

`udisksctl mount {{[-b|--block-device]}} {{/dev/sdXN}}`

- Desmonta una partición de un dispositivo:

`udisksctl unmount {{[-b|--block-device]}} {{/dev/sdXN}}`

- Apaga un dispositivo para extraerlo de forma segura:

`udisksctl power-off {{[-b|--block-device]}} {{/dev/sdX}}`

- Supervisa el programa residente en busca de eventos:

`udisksctl monitor`
