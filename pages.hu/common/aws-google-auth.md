# aws-google-auth

> Parancssori eszköz az AWS ideiglenes (STS) hitelesítő adatok megszerzéséhez a Google Apps mint föderált (Single Sign-On) szolgáltató használatával. További információ: <https://github.com/cevoaustralia/aws-google-auth>.

- Jelentkezzen be a Google SSO-val az IDP és SP azonosítók használatával, és állítsa be a hitelesítő adatok időtartamát egy órára:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Jelentkezzen be \[a\]sking melyik szerepet kívánja használni (több rendelkezésre álló SAML-szerepkör esetén):

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Az AWS-fiókok aliasainak feloldása:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Súgóinformációk megjelenítése:

`aws-google-auth -h`
