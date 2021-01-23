# aws-google-auth

> Kommandozeilen Werkzeug um temporäre AWS credentials (STS) über Google Apps als Single Sign-On Dienstleister zu erhalten.
> Mehr Informationen: <https://github.com/cevoaustralia/aws-google-auth>.

- Einloggen mit Google SSO über IDP- und SP-Kennung für die Dauer einer Stunde:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Einloggen mit der Option eine Rolle auszuwählen  (im Falle mehrerer verfügbarer SAML Rollen):

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Auflösen von Aliases von AWS Accounts:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Anzeigen von Hilfs-Informationen:

`aws-google-auth -h`
