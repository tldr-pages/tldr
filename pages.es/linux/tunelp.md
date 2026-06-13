# tunelp

> Establece varios parámetros para dispositivos de puerto paralelo para la solución de problemas o para un mejor rendimiento.
> Parte de `util-linux`.
> Más información: <https://manned.org/tunelp>.

- Comprueba el e[s]tado de un dispositivo de puerto paralelo:

`tunelp {{[-s|--status]}} {{/dev/lp0}}`

- Restablece un puerto paralelo:

`tunelp {{[-r|--reset]}} {{/dev/lp0}}`

- Utiliza un [i]RQ dado para un dispositivo, cada uno representando una línea de interrupción:

`tunelp {{[-i|--irq]}} 5 {{/dev/lp0}}`

- Intenta imprimir varias veces un [c]arácter en la impresora antes de permanecer inactiva durante un [t]iempo determinado:

`tunelp {{[-c|--chars]}} {{veces}} {{[-t|--time]}} {{tiempo_en_centisegundos}} {{/dev/lp0}}`

- Activa o desactiva el [a]bortar por error (desactivado por defecto):

`tunelp {{[-a|--abort]}} {{on|off}}`
