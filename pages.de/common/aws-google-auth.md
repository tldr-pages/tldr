# aws-google-auth

> CLI, um temporäre AWS credentials (STS) über Google Apps als Single Sign-On Dienstleister zu erhalten.
> Weitere Informationen: <https://github.com/cevoaustralia/aws-google-auth>.

- Einloggen mit Google SSO über IDP- und SP-Kennung für die Dauer einer Stunde:

`aws-google-auth {{[-u|--username]}} {{beispiel@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}}`

- Einloggen mit der Option eine Rolle auszuwählen (im Falle mehrerer verfügbarer SAML Rollen):

`aws-google-auth {{[-u|--username]}} {{beispiel@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}}`

- Löse Aliasse von AWS Accounts auf:

`aws-google-auth {{[-u|--username]}} {{beispiel@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}} --resolve-aliases`

- Zeige Hilfs-Informationen:

`aws-google-auth {{[-h|--help]}}`
