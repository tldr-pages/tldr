# chpass

> Añade o cambia la información de la base de datos del usuario, incluyendo el intérprete de comandos (shell) y la contraseña.
> Nota: no es posible cambiar la contraseña del usuario en sistemas Open Directory, utiliza `passwd` en su lugar.
> Vea también: `passwd`.
> Más información: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Añade o cambia la información de la base de datos del usuario actual de forma interactiva:

`su -c chpass`

- Establece un [s]hell de inicio de sesión específico para el usuario actual:

`chpass -s {{ruta/al/shell}}`

- Establece un inicio de sesión [s]hell para un usuario específico:

`chpass -s {{ruta/al/shell}} {{usuario}}`

- Edita el registro de usuario en el nodo de directorio en la ubicación dada:

`chpass -l {{ubicación}} -s {{ruta/al/shell}} {{nombre_de_usuario}}`

- Utiliza el nombre dado al autenticarse en el nodo de directorio que contiene al usuario:

`chpass -u {{nombre_de_usuario}} -s {{ruta/al/shell}} {{nombre_de_usuario}}`
