# reg

> Administra claves y sus valores en el registro de Windows.
> Algunos subcomandos como `add` tienen su propia documentación de uso.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg>.

- Ejecutar un comando del registro:

`reg {{comando}}`

- Ver la documentación para agregar y copiar subclaves:

`tldr reg {{add|copy}}`

- Ver la documentación para eliminar claves y subclaves:

`tldr reg {{delete|unload}}`

- Ver la documentación para buscar, ver y comparar claves:

`tldr reg {{compare|query}}`

- Ver la documentación para exportar e importar claves del registro sin preservar la propiedad ni las ACLs de las claves:

`tldr reg {{export|import}}`

- Ver la documentación para guardar, restaurar y descargar claves del registro preservando la propiedad y las ACLs de las claves:

`tldr reg {{save|restore|load|unload}}`

- Mostrar ayuda:

`reg /?`

- Mostrar ayuda para un comando específico:

`reg {{comando}} /?`
