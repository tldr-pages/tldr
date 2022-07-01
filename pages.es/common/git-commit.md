# git commit

> Realiza commits de los archivos al repositorio.
> Más información: <https://git-scm.com/docs/git-commit>.

- Realiza un commit de los archivos marcados al repositorio con un mensaje:

`git commit -m "{{mensaje}}"`

- Realiza un commit de los archivos marcados con un mensaje leído desde un archivo:

`git commit --file {{ruta/al/archivo_del_mensaje_del_commit}}`

- Marca automáticamente todos los archivos modificados y realiza un commit con un mensaje:

`git commit -a -m "{{mensaje}}"`

- Sustituye el último commit con los cambios marcados actualmente, cambiando el hash del commit:

`git commit --amend`

- Realiza un commit para archivos específicos (marcados previamente):

`git commit {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Crea un commit, incluso si no hay archivos marcados:

`git commit -m "{{mensaje}}" --allow-empty`
