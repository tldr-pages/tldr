# aws-google-auth

> Herramienta de línea de comandos para adquirir credenciales temporales de AWS (STS) utilizando Google Apps como proveedor federado (Single Sign-On).
> Más información: <https://github.com/cevoaustralia/aws-google-auth>.

- Inicia sesión con Google SSO utilizando los identificadores IDP y SP y establece la duración de las credenciales en una hora:

`aws-google-auth -u {{ejemplo@ejemplo.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Inicia sesión pregunt[a]ndo qué rol usar (en caso de varios roles disponibles  SAML):

`aws-google-auth -u {{ejemplo@ejemplo.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Resuelve alias para cuentas AWS:

`aws-google-auth -u {{ejemplo@ejemplo.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Muestra información de ayuda:

`aws-google-auth -h`
