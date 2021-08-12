# modinfo

> Extrageţi informaţii despre un modul kernel Linux.

- Listează toate atributele unui modul kernel:

`modinfo {{kernel_module}}`

- Listează numai atributul specificat:

`modinfo -F {{author|description|license|parm|filename}} {{kernel_module}}`
