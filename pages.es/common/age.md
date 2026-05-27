# age

> Una herramienta de cifrado de archivos sencilla, moderna y segura.
> Vea también: `age-keygen`, `age-inspect`.
> Más información: <https://github.com/FiloSottile/age#usage>.

- Genera un archivo cifrado que se puede descifrar con una frase de contraseña:

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{ruta/al/archivo_cifrado.age}} {{ruta/al/archivo_no_cifrado}}`

- Cifra un archivo con una o más claves públicas introducidas como literales (repetir `--recipient` para varias claves):

`age {{[-r|--recipient]}} {{clave_publica}} {{[-o|--output]}} {{ruta/al/archivo_cifrado.age}} {{ruta/al/archivo_no_cifrado}}`

- Cifra un archivo con las claves públicas especificadas en un archivo de destinatarios (una por línea):

`age {{[-R|--recipients-file]}} {{ruta/al/archivo_destinatarios.txt}} {{[-o|--output]}} {{ruta/al/archivo_cifrado.age}} {{ruta/al/archivo_no_cifrado}}`

- Descifra un archivo con una frase de contraseña:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{ruta/al/archivo_descifrado}} {{ruta/al/archivo_cifrado.age}}`

- Descifra un archivo con un archivo de clave privada:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{ruta/al/archivo_clave_privada}} {{[-o|--output]}} {{ruta/al/archivo_descifrado}} {{ruta/al/archivo_cifrado.age}}`
