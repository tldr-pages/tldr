# getprop

> Obtém informações sobre propriedades do sistema (system props) Android.
> Mais informações: <https://manned.org/getprop>.

- Mostrar todas as propriedades do sistema:

`getprop`

- Mostrar o valor de uma propriedade específica:

`getprop {{prop}}`

- Mostrar o nível de API:

`getprop {{ro.build.version.sdk}}`

- Mostrar a versão do Android:

`getprop {{ro.build.version.release}}`

- Mostrar o modelo do dispositivo:

`getprop {{ro.vendor.product.model}}`

- Mostrar o status de desbloqueio OEM:

`getprop {{ro.oem_unlock_supported}}`

- Mostrar o endereço MAC da placa de Wi-Fi do dispositivo:

`getprop {{ro.boot.wifimacaddr}}`
