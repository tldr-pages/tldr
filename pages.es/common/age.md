# age

> Una herramienta de encriptación de archivos sencilla, moderna y segura.
> Vea también: `age-keygen` para generar pares de claves.
> Más información: <https://github.com/FiloSottile/age#usage>.

- Genera un archivo cifrado que se puede descifrar con una frase de contraseña:

`age  {{[-p|--passphrase]}} {{[-o|--output]}} {{ruta/al/archivo_encriptado}} {{ruta/al/archivo_no_cifrado}}`

- Cifra un archivo con una o varias claves públicas introducidas como literales (repite el indicador `--recipient` para especificar varias claves públicas):

`age {{[-r|--recipient]}} {{clave_publica}} {{[-o|--output]}} {{ruta/al/archivo_cifrado}} {{ruta/al/archivo_no_cifrado}}`

- Cifra un archivo a uno o más destinatarios con sus claves públicas especificadas en un archivo (una por línea):

`age {{[-R|--recipients-file]}}  {{ruta/a/archivo_recipientes}} {{[-o|--output]}} {{ruta/al/archivo_encriptado}} {{ruta/al/archivo_no_cifrado}}`

- Descifra un archivo con una frase de contraseña:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{ruta/al/archivo_descifrado}} {{ruta/para/archivo_cifrado}}`

- Descifra un archivo con un archivo de clave privada:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{ruta/al/archivo_de_clave_privada}} {{[-o|--output]}} {{ruta/para/archivo_descifrado}} {{ruta/a/archivo_cifrado}}`
