# oathtool

> OATH one-time password tool.

- Generate TOTP token (behaves like Google Authenticator):

`oathtool --totp --base32 {{secret}}`

- Validate TOTP token:

`oathtool --totp --base32 {{secret}} {{token}}`
