# git am

> Aplica archivos de parche. Útil cuando se reciben commits por correo electrónico.
> Vea también `git format-patch`, comando que genera archivos de parche.
> Más información: <https://git-scm.com/docs/git-am>.

- Aplica un archivo de parche:

`git am {{ruta/al/archivo.patch}}`

- Aplica un archivo de parche remoto:

`curl -L {{https://ejemplo.com/file.patch}} | git apply`

- Aborta el proceso de aplicar un archivo de parche:

`git am --abort`

- Aplica todo lo posible de un archivo de parche y guarda los fragmentos fallidos para rechazar archivos:

`git am --reject {{ruta/al/archivo.patch}}`
