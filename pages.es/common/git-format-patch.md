# git format-patch

> Prepara archivos .patch. Es útil cuando se envían commits por correo electrónico.
> Vea también `git-am`, comando que puede aplicar los archivos .patch generados.
> Más información: <https://git-scm.com/docs/git-format-patch>.

- Crea un archivo `.patch` con nombre automático para todos los cambios que no están en el push:

`git format-patch {{origen}}`

- Escribe un archivo `.patch` para todos los commits entre dos revisiones a `stdout`:

`git format-patch {{revisión_1}}..{{revisión_2}}`

- Escribe un archivo `.patch` para los 3 últimos commits:

`git format-patch -{{3}}`
