# git commit

> Realiza confirmaciones de los archivos al repositorio.
> Más información: <https://git-scm.com/docs/git-commit>.

- Realiza una confirmación de los archivos marcados al repositorio con un mensaje:

`git commit --message "{{mensaje}}"`

- Realiza una confirmación de los archivos marcados con un mensaje leído desde un archivo:

`git commit --file {{ruta/al/archivo_con_mensaje_de_la_confirmación}}`

- Marca automáticamente todos los archivos modificados y realiza una confirmación con un mensaje:

`git commit --all --message "{{mensaje}}"`

- Confirma todos los archivos preparados y los firma con una llave de GPG (o la llave en el archivo de configuración si no se especifica un argumento):

`git commit --gpg-sign {{identificador_de_llave}} --message "{{mensaje}}"`

- Sustituye la última confirmación con los cambios marcados actualmente, cambiando el hash de la confirmación:

`git commit --amend`

- Realiza una confirmación para archivos específicos (marcados previamente):

`git commit {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Crea una confirmación, incluso si no hay archivos marcados:

`git commit --message "{{mensaje}}" --allow-empty`
