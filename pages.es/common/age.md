# age

> Una herramienta de encriptación de archivos sencilla, moderna y segura.
> Más información: <https://github.com/FiloSottile/age>.

- Genera un archivo cifrado que se puede descifrar con una frase de contraseña:

`age --passphrase --output {{ruta/al/archivo_encriptado}} {{ruta/al/archivo_no_encriptado}}`

- Genera un par de claves, guardando la clave privada en un archivo no cifrado e imprimiendo la clave pública en `stdout`:

`age-keygen --output {{ruta/al/archivo}}`

- Cifra un archivo con una o más claves públicas que se introducen como literales:

`age --recipient {{clave_publica_1}} --recipient {{clave_publica_2}} {{ruta/al/archivo_sin_cifrar}} --output {{ruta/al/archivo_cifrado}}`

- Cifra un archivo con una o varias claves públicas especificadas en un archivo de destinatarios:

`age --recipients-file {{ruta/al/archivo_recipientes}} {{ruta/para/archivo_sin_cifrar}} --output {{ruta/al/archivo_encriptado}}`

- Descifra un archivo con una frase de contraseña:

`age --decrypt --output {{ruta/al/archivo_descifrado}} {{ruta/para/archivo_cifrado}}`

- Descifra un archivo con un archivo de clave privada:

`age --decrypt --identity {{ruta/al/archivo_de_clave_privada}} --output {{ruta/para/archivo_descifrado}} {{ruta/para/archivo_cifrado}}`
