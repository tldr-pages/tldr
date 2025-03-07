# logread

> Lee el registro de la memoria cíclica `logd`.
> Más información: <https://openwrt.org/docs/guide-user/base-system/log.essentials>.

- Imprime el registro:

`logread`

- Imprime un número determinado de mensajes:

`logread -l {{N}}`

- Filtra los mensajes por (palabra clave/expresión regular):

`logread -e {{patrón}}`

- Imprime los mensajes de registro a medida que se producen:

`logread -f`
