# aws-google-auth

> Herramienta de línea de comandos para adquirir credenciales temporales de AWS (STS) utilizando Google Apps como proveedor federado (Single Sign-On).
> Más información: <https://github.com/cevoaustralia/aws-google-auth>.

- Inicia sesión con Google SSO utilizando los identificadores IDP y SP y establece la duración de las credenciales en una hora:

`aws-google-auth {{[-u|--username]}} {{ejemplo@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}}`

- Inicia sesión preguntando qué rol usar (en caso de varios roles disponibles SAML):

`aws-google-auth {{[-u|--username]}} {{ejemplo@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}}`

- Resuelve alias para cuentas AWS:

`aws-google-auth {{[-u|--username]}} {{ejemplo@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}} --resolve-aliases`

- Muestra información de ayuda:

`aws-google-auth {{[-h|--help]}}`
