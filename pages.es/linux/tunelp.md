# tunelp

> Establece varios parámetros para dispositivos de puerto paralelo para la solución de problemas o para un mejor rendimiento.
> Parte de `util-linux`.
> Más información: <https://manned.org/tunelp>.

- Comprueba el e[s]tado de un dispositivo de puerto paralelo:

`tunelp --status {{/dev/lp0}}`

- Restablece un puerto paralelo determinado:

`tunelp --reset {{/dev/lp0}}`

- Utiliza un [i]RQ dado para un dispositivo, cada uno representando una línea de interrupción:

`tunelp -i 5 {{/dev/lp0}}`

- Intenta un número determinado de veces imprimir un [c]arácter en la impresora antes de permanecer inactiva durante un [t]iempo determinado:

`tunelp --chars {{veces}} --time {{tiempo_en_centisegundos}} {{/dev/lp0}}`

- Activa o desactiva el [a]bortaje por error (desactivado por defecto):

`tunelp --abort {{on|off}}`
