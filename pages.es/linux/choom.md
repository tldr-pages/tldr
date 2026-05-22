# choom

> Muestra y cambia el ajuste del OOM-killer.
> Más información: <https://manned.org/choom>.

- Muestra la puntuación OOM-killer del proceso con un identificador específico:

`choom {{[-p|--pid]}} {{pid}}`

- Modifica la puntuación OOM-killer de un proceso específico:

`choom {{[-p|--pid]}} {{pid}} {{[-n|--adjust]}} {{-1000..+1000}}`

- Ejecuta un comando con una puntuación OOM-killer específica:

`choom {{[-n|--adjust]}} {{-1000..+1000}} {{comando}} {{argumento1 argumento2 ...}}`
