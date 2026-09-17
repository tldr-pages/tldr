# aws-google-auth

> Acquisisce credenziali AWS temporanee (STS) utilizzando Google Apps come fornitore federato (Single Sign-On).
> Maggiori informazioni: <https://github.com/cevoaustralia/aws-google-auth>.

- Accedi con Google SSO utilizzando l'identificativo username IDP e SP specificati e imposta la durata delle credenziali a un'ora:

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}}`

- Accedi chiedendo quale ruolo utilizzare (in caso di più ruoli SAML disponibili):

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}}`

- Risolve gli alias per gli account AWS:

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}} --resolve-aliases`

- Visualizza l'aiuto:

`aws-google-auth {{[-h|--help]}}`
