# pkg

> Gestor de paquetes de FreeBSD.
> Más información: <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>.

- Instala un nuevo paquete:

`pkg install {{paquete}}`

- Elimina un paquete:

`pkg delete {{paquete}}`

- Actualiza todos los paquetes:

`pkg upgrade`

- Busca un paquete:

`pkg search {{palabra_clave}}`

- Lista los paquetes instalados:

`pkg info`

- Elimina dependencias innecesarias:

`pkg autoremove`
