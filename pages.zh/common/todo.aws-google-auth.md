# aws-google-auth

> Command line tool to acquire AWS temporary (STS) credentials using Google Apps as a federated (Single Sign-On) provider.
> More information: <https://github.com/cevoaustralia/aws-google-auth>.

- Login with Google SSO using the IDP and SP identifiers and set the credentials duration to one hour:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Login [a]sking which role to use (in case of several available SAML roles):

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Resolve aliases for AWS accounts:

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Show help information:

`aws-google-auth -h`
