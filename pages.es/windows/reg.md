# reg

> Administra claves y sus valores en el registro de Windows.
> Algunos subcomandos como `add` tienen su propia documentación de uso.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg>.

- Ejecuta un comando del registro:

`reg {{comando}}`

- Visualiza la documentación para agregar y copiar subclaves:

`tldr reg {{add|copy}}`

- Visualiza la documentación para eliminar claves y subclaves:

`tldr reg {{delete|unload}}`

- Visualiza la documentación para buscar, ver y comparar claves:

`tldr reg {{compare|query}}`

- Visualiza la documentación para exportar e importar claves del registro sin preservar la propiedad ni las ACLs de las claves:

`tldr reg {{export|import}}`

- Visualiza la documentación para guardar, restaurar y descargar claves del registro preservando la propiedad y las ACLs de las claves:

`tldr reg {{save|restore|load|unload}}`

- Muestra la ayuda:

`reg /?`

- Muestra la ayuda para un comando específico:

`reg {{comando}} /?`
