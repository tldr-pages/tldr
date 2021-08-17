# aws-google-auth

> instrument de linie de comandă pentru a achiziționa acreditările temporare AWS (STS) utilizând Google Apps ca furnizor federalizat (Single Sign-On).
> Mai multe informaţii: <https://github.com/cevoaustralia/aws-google-auth>

- Conectați-vă cu Google SSO utilizând identificatorii IDP și SP și setați durata acreditărilor la o oră:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Conectați-vă [a] întrebănd ce rol să utilizați (în cazul mai multor roluri SAML disponibile):

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Rezolvarea aliasurilor pentru conturile AWS:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Afișează informații de ajutor:

`aws-google-auth -h`
