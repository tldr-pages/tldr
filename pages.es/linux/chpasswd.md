# chpasswd

> Cambia las contraseñas de varios usuarios utilizando `stdin`.
> Vea también: `passwd`.
> Más información: <https://manned.org/chpasswd>.

- Cambia la contraseña de un usuario específico:

`printf "{{nombre_usuario}}:{{nueva_contraseña}}" | sudo chpasswd`

- Cambia las contraseñas de varios usuarios (el texto ingresado no debe contener espacios):

`printf "{{nombre_usuario_1}}:{{nueva_contraseña_1}}\n{{nombre_usuario_2}}:{{nueva_contraseña_2}}" | sudo chpasswd`

- Cambia la contraseña de un usuario específico y es especificada en forma cifrada:

`printf "{{nombre_usuario}}:{{nueva_contraseña_cifrada}}" | sudo chpasswd {{[-e|--encrypted]}}`

- Cambia la contraseña de un usuario específico y utiliza un cifrado específico para la contraseña almacenada:

`printf "{{nombre_usuario}}:{{nueva_contraseña}}" | sudo chpasswd {{[-c|--crypt-method]}} {{NONE|DES|MD5|SHA256|SHA512}}`
