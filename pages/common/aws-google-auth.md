# aws-google-auth

> Acquire AWS temporary (STS) credentials using Google Apps as a federated (Single Sign-On) provider.
> More information: <https://github.com/cevoaustralia/aws-google-auth>.

- Log in with Google SSO using the specified [u]sername [I]DP and [S]P identifiers and set the credentials [d]uration to one hour:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Log in [a]sking which role to use (in case of several available SAML roles):

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Resolve aliases for AWS accounts:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Display help:

`aws-google-auth -h`
