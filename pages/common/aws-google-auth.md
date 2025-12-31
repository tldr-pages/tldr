# aws-google-auth

> Acquire AWS temporary (STS) credentials using Google Apps as a federated (Single Sign-On) provider.
> More information: <https://github.com/cevoaustralia/aws-google-auth>.

- Log in with Google SSO using the specified username IDP and SP identifiers and set the credentials duration to one hour:

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}}`

- Log in asking which role to use (in case of several available SAML roles):

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}}`

- Resolve aliases for AWS accounts:

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}} --resolve-aliases`

- Display help:

`aws-google-auth {{[-h|--help]}}`
