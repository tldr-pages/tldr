# inxi

> Muestra un resumen de la información y los recursos del sistema con fines de depuración.
> Vea también: `lshw`, `hwinfo`, `dmidecode`.
> Más información: <https://manned.org/inxi>.

- Muestra un resumen de la información sobre la CPU, la memoria, el disco duro y el núcleo:

`inxi`

- Muestra una descripción completa de la información sobre la CPU, la memoria, el disco, la red y los procesos, y filtra la información confidencial:

`inxi {{[-ez|--expanded --filter]}}`

- Muestra un resumen de la información de la CPU:

`inxi {{[-C|--cpu]}}`

- Muestra un resumen de la información gráfica:

`inxi {{[-G|--graphics]}}`

- Muestra un resumen de la RAM del sistema:

`inxi {{[-m|--memory]}}`

- Muestra un resumen del audio del sistema:

`inxi {{[-A|--audio]}}`

- Muestra los datos de los sensores disponibles:

`inxi {{[-s|--sensors]}}`

- Muestra información sobre los repositorios de la distribución:

`inxi {{[-r|--repos]}}`
