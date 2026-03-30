# openssl dgst

> Genera valores de resumen (digest) y realiza operaciones de firma.
> Más información: <https://docs.openssl.org/master/man1/openssl-dgst/>.

- Calcula el digest SHA256 de un archivo y guarda el resultado en un archivo específico:

`openssl dgst -sha256 -binary -out {{archivo_salida}} {{archivo_entrada}}`

- Firma un archivo usando una clave RSA y guarda el resultado en un archivo específico:

`openssl dgst -sign {{archivo_clave_privada}} -sha256 -sigopt rsa_padding_mode:pss -out {{archivo_salida}} {{archivo_entrada}}`

- Verifica una firma RSA:

`openssl dgst -verify {{archivo_clave_publica}} -signature {{archivo_firma}} -sigopt rsa_padding_mode:pss {{archivo_mensaje_firmado}}`

- Firma un archivo usando una clave ECDSA:

`openssl dgst -sign {{archivo_clave_privada}} -sha256 -out {{archivo_salida}} {{archivo_entrada}}`

- Verifica una firma ECDSA:

`openssl dgst -verify {{archivo_clave_publica}} -signature {{archivo_firma}} {{archivo_mensaje_firmado}}`
