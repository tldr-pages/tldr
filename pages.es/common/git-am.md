# git am

> Aplica archivos de parche. Útil cuando se reciben commits por correo electrónico.
> Véase también `git format-patch`, comando que genera archivo de parche.
> Más información: <https://git-scm.com/docs/git-am>.

- Aplica un archivo de parche:

`git am {{ruta/del/archivo.patch}}`

- Aborta el proceso de aplicar un archivo de parche:

`git am --abort`

- Aplica todo lo posible de un archivo de parche y guarda los fragmentos fallidos para rechazar archivos:

`git am --reject {{ruta/del/archivo.patch}}`
