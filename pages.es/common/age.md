# age

> Una herramienta de encriptación de archivos sencilla, moderna y segura.
> Vea también: `age-keygen` para generar pares de claves.
> Más información: <https://github.com/FiloSottile/age>.

- Genera un archivo cifrado que se puede descifrar con una frase de contraseña:

`age --passphrase --output {{ruta/al/archivo_encriptado}} {{ruta/al/archivo_no_cifrado}}`

- Cifra un archivo con una o varias claves públicas introducidas como literales (repite el indicador `--recipient` para especificar varias claves públicas):

`age --recipient {{clave_publica}} --output {{ruta/al/archivo_cifrado}} {{ruta/al/archivo_no_cifrado}}`

- Cifra un archivo a uno o más destinatarios con sus claves públicas especificadas en un archivo (una por línea):

`age --recipients-file {{ruta/a/archivo_recipientes}} --output {{ruta/al/archivo_encriptado}} {{ruta/al/archivo_no_cifrado}}`

- Descifra un archivo con una frase de contraseña:

`age --decrypt --output {{ruta/al/archivo_descifrado}} {{ruta/para/archivo_cifrado}}`

- Descifra un archivo con un archivo de clave privada:

`age --decrypt --identity {{ruta/al/archivo_de_clave_privada}} --output {{ruta/para/archivo_descifrado}} {{ruta/a/archivo_cifrado}}`
