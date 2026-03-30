# openssl x509

> Gestiona certificados X.509.
> Más información: <https://docs.openssl.org/master/man1/openssl-x509/>.

- Muestra información de un certificado:

`openssl x509 -in {{nombre_archivo.crt}} -noout -text`

- Muestra la fecha de vencimiento de un certificado:

`openssl x509 -enddate -noout -in {{nombre_archivo.pem}}`

- Convierte un certificado entre codificación binaria DER y codificación textual PEM:

`openssl x509 -inform {{der}} -outform {{pem}} -in {{archivo_certificado_original}} -out {{archivo_certificado_convertido}}`

- Almacena la clave pública de un certificado en un archivo:

`openssl x509 -in {{archivo_certificado}} -noout -pubkey -out {{archivo_salida}}`
