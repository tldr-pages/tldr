# oathtool

> OATH one-time password tool.
> More information: <https://www.nongnu.org/oath-toolkit/oathtool.1.html>.

- Generate TOTP token (behaves like Google Authenticator):

`oathtool --totp --base32 "{{secret}}"`

- Generate a TOTP token for a specific time:

`oathtool --totp --now "{{2004-02-29 16:21:42}}" --base32 "{{secret}}"`

- Validate a TOTP token:

`oathtool --totp --base32 "{{secret}}" "{{token}}"`
