# aws acm

> AWS Certificate Manager.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- Importa un certificado:

`aws acm import-certificate --certificate-arn {{certificado_arn}} --certificate {{certificado}} --private-key {{clave_privada}} --certificate-chain {{certificado_cadena}}`

- Lista certificados:

`aws acm list-certificates`

- Describe un certificado:

`aws acm describe-certificate --certificate-arn {{certificado_arn}}`

- Solicita un certificado:

`aws acm request-certificate --domain-name {{nombre_dominio}} --validation-method {{método_de_validación}}`

- Elimina un certificado:

`aws acm delete-certificate --certificate-arn {{certificate_arn}}`

- Lista validaciones de certificados:

`aws acm list-certificates --certificate-statuses {{estado}}`

- Obtén detalles del certificado:

`aws acm get-certificate --certificate-arn {{certificado_arn}}`

- Actualiza las opciones del certificado:

`aws acm update-certificate-options --certificate-arn {{certificado_arn}} --options {{opciones}}`
