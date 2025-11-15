# oathtool

> OATH 일회성 비밀번호 도구.
> 더 많은 정보: <https://www.nongnu.org/oath-toolkit/oathtool.1.html>.

- TOTP 토큰 생성 (Google Authenticator처럼 동작):

`oathtool --totp --base32 "{{비밀}}"`

- 특정 시간에 대한 TOTP 토큰 생성:

`oathtool --totp --now "{{2004-02-29 16:21:42}}" --base32 "{{비밀}}"`

- TOTP 토큰 검증:

`oathtool --totp --base32 "{{비밀}}" "{{토큰}}"`
