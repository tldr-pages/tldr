# aws-google-auth

> CLI, um temporäre AWS credentials (STS) über Google Apps als Single Sign-On Dienstleister zu erhalten.
> Weitere Informationen: <https://github.com/cevoaustralia/aws-google-auth>.

- Einloggen mit Google SSO über IDP- und SP-Kennung für die Dauer einer Stunde:

`aws-google-auth -u {{beispiel@beispiel.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Einloggen mit der Option eine Rolle auszuwählen (im Falle mehrerer verfügbarer SAML Rollen):

`aws-google-auth -u {{beispiel@beispiel.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Löse Aliasse von AWS Accounts auf:

`aws-google-auth -u {{beispiel@beispiel.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Zeige Hilfs-Informationen:

`aws-google-auth -h`
