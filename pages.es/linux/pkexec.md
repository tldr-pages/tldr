# pkexec

> Ejecuta comandos como otro usuario.
> Solicita la contraseña a través de una interfaz gráfica de usuario, si está disponible.
> Vea también: `sudo`, `run0`, `doas`.
> Más información: <https://polkit.pages.freedesktop.org/polkit/pkexec.1.html>.

- Ejecuta el comando como root:

`pkexec {{comando}}`

- Cambia de usuario a root:

`pkexec`

- Ejecuta un comando como un usuario específico:

`pkexec --user {{nombre_de_usuario}} {{comando}}`
