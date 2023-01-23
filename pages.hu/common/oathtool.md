# oathtool

> OATH egyszer használatos jelszavas eszköz. További információ: <https://www.nongnu.org/oath-toolkit/oathtool.1.html>.

- TOTP token generálása (úgy viselkedik, mint a Google Authenticator):

`oathtool --totp --base32 "{{secret}}"`

- TOTP token generálása egy adott időpontra:

`oathtool --totp --now "{{2004-02-29 16:21:42}}" --base32 "{{secret}}"`

- TOTP token hitelesítése:

`oathtool --totp --base32 "{{secret}}" "{{token}}"`
