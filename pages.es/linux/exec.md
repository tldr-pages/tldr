# exec

> Ejecuta un comando sin crear un proceso hijo.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- Ejecuta un comando específico:

`exec {{comando -con -opciones}}`

- Ejecuta un comando con un entorno (en su mayoría) vacío:

`exec -c {{comando -con -opciones}}`

- Ejecuta un comando como un shell de inicio de sesión:

`exec -l {{comando -con -opciones}}`

- Ejecuta un comando con un nombre diferente:

`exec -a {{nombre}} {{comando -con -opciones}}`
