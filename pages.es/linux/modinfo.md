# modinfo

> Extrae información sobre un módulo del núcleo Linux.
> Vea también: `kmod`.
> Más información: <https://manned.org/modinfo>.

- Lista todos los atributos de un módulo del núcleo:

`modinfo {{módulo_del_núcleo}}`

- Lista solo el atributo especificado:

`modinfo -F {{author|description|license|parm|filename}} {{módulo_del_núcleo}}`
