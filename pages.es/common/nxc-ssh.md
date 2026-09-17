# nxc ssh

> Prueba y explota servidores SSH.
> Vea también: `hydra`.
> Más información: <https://www.netexec.wiki/ssh-protocol/password-spraying>.

- Pulveriza la contraseña especificada contra una lista de nombres de usuario en el objetivo especificado:

`nxc ssh {{192.168.178.2}} {{[-u|--username]}} {{ruta/a/nombres_de_usuario.txt}} {{[-p|--password]}} {{contraseña}}`

- Busca credenciales válidas probando todas las combinaciones de nombres de usuario y contraseñas de las listas especificadas:

`nxc ssh {{192.168.178.2}} {{[-u|--username]}} {{ruta/a/nombres_de_usuario.txt}} {{[-p|--password]}} {{ruta/a/contraseñas.txt}}`

- Utiliza la clave privada especificada para la autenticación, utilizando la contraseña suministrada como frase de contraseña de la clave:

`nxc ssh {{192.186.178.2}} {{[-u|--username]}} {{ruta/a/nombres_de_usuario.txt}} {{[-p|--password]}} {{contraseña}} --key-file {{ruta/a/id_rsa}}`

- Prueba una combinación de nombres de usuario y contraseñas en una serie de objetivos:

`nxc ssh {{192.168.178.0/24}} {{[-u|--username]}} {{usuario}} {{[-p|--password]}} {{contraseña}}`

- Comprueba los privilegios `sudo` en un inicio de sesión correcto:

`nxc ssh {{192.168.178.2}} {{[-u|--username]}} {{usuario}} {{[-p|--password]}} {{ruta/a/contraseñas.txt}} --sudo-check`
