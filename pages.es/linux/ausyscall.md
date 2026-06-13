# ausyscall

> Mapea los nombres y números de las llamadas al sistema (syscalls).
> Más información: <https://manned.org/ausyscall>.

- Muestra el número de llamada al sistema de una llamada específica:

`ausyscall {{patrón_de_búsqueda}}`

- Muestra el nombre de una llamada al sistema específico a partir de su número:

`ausyscall {{número_de_llamada_al_sistema}}`

- Muestra todas las llamadas al sistema para una arquitectura específica:

`ausyscall {{arquitectura}} --dump`
