# aws-google-auth

> A command-line tool allows you to acquire AWS temporary (STS) credentials using Google Apps as a federated (Single Sign-On, or SSO) provider.
> More information: <https://github.com/cevoaustralia/aws-google-auth>.

- Login with Google SSO:

`aws-google-auth -u example@example.com -I $GOOGLE_IDP_ID -S $GOOGLE_SP_ID -d 3600`

- Ask, which role to use (in case you have several SAML roles):

`aws-google-auth -u example@example.com -I $GOOGLE_IDP_ID -S $GOOGLE_SP_ID -d 3600 -a`

- Resolve aliases for AWS accounts:

`aws-google-auth -u example@example.com -I $GOOGLE_IDP_ID -S $GOOGLE_SP_ID -d 3600 -a --resolve-aliases`

- Show help information:

`aws-google-auth -h`
