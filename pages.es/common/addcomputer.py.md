# addcomputer.py

> Añade una cuenta de ordenador al dominio.
> Más información: <https://github.com/fortra/impacket>.

- Añade un ordenador con un nombre y una contraseña específicos:

`addcomputer.py -computer-name {{COMPUTER_NAME$}} -computer-pass {{contraseña_computadora}} {{dominio}}/{{nombre_usuario}}:{{contraseña}}`

- Establece solo una nueva contraseña en un ordenador existente:

`addcomputer.py -no-add -computer-name {{COMPUTER_NAME$}} -computer-pass {{contraseña_computadora}} {{dominio}}/{{nombre_usuario}}:{{contraseña}}`

- Elimina una cuenta de ordenador existente:

`addcomputer.py -delete -computer-name {{COMPUTER_NAME$}} {{dominio}}/{{nombre_usuario}}:{{contraseña}}`

- Añade un ordenador utilizando la autenticación Kerberos:

`addcomputer.py -k -no-pass {{dominio}}/{{nombre_usuario}}@{{hostname}}`

- Añade un ordenador a través de LDAPS (puerto 636) en lugar de SAMR (puerto 445):

`addcomputer.py -method LDAPS -port 636 {{dominio}}/{{nombre_usuario}}:{{contraseña}}`

- Especifica el controlador de dominio exacto cuando existen varios DC:

`addcomputer.py -dc-host {{hostname}} {{dominio}}/{{nombre_usuario}}:{{contraseña}}`
