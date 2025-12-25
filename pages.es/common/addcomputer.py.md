# addcomputer.py

> Añade una cuenta de ordenador al dominio.
> Más información: <https://github.com/fortra/impacket>.

- Añade un ordenador con un nombre y una contraseña específicos:

`addcomputer.py -computer-name {{COMPUTER_NAME$}} -computer-pass {{computer_password}} {{domain}}/{{username}}:{{password}}`

- Establece solo una nueva contraseña en un ordenador existente:

`addcomputer.py -no-add -computer-name {{COMPUTER_NAME$}} -computer-pass {{computer_password}} {{domain}}/{{username}}:{{password}}`

- Elimina una cuenta de ordenador existente:

`addcomputer.py -delete -computer-name {{COMPUTER_NAME$}} {{domain}}/{{username}}:{{password}}`

- Añade un ordenador utilizando la autenticación Kerberos:

`addcomputer.py -k -no-pass {{domain}}/{{username}}@{{hostname}}`

- Añade un ordenador a través de LDAPS (puerto 636) en lugar de SAMR (puerto 445):

`addcomputer.py -method LDAPS -port 636 {{domain}}/{{username}}:{{password}}`

- Especifica el controlador de dominio exacto cuando existen varios DC:

`addcomputer.py -dc-host {{hostname}} {{domain}}/{{username}}:{{password}}`
