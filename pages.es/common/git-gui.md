# git gui

> Una GUI para Git para gestionar ramas, remotos, confirmaciones de cambio y realizar fusiones locales.
> Vea también: `git-cola`, `gitk`.
> Más información: <https://git-scm.com/docs/git-gui>.

- Inicia la GUI:

`git gui`

- Muestra un archivo específico con el nombre del autor y el hash de confirmación en cada línea:

`git gui blame {{ruta/al/archivo}}`

- Abre `git gui blame` en una revisión específica:

`git gui blame {{revisión}} {{ruta/al/archivo}}`

- Abre `git gui blame` y desplaza la vista para centrarla en una línea específica:

`git gui blame --line={{línea}} {{ruta/al/archivo}}`

- Abre una ventana para hacer una confirmación y vuelve al intérprete de comandos cuando se haya completado:

`git gui citool`

- Abre `git gui citool` en modo "Modificar la última confirmación":

`git gui citool --amend`

- Abre `git gui citool` en modo de solo lectura:

`git gui citool --nocommit`

- Muestra un navegador para el árbol de una rama específica, abriendo la herramienta de autoría al hacer clic en los archivos:

`git gui browser maint`
