# երդման գործիք

> OATH մեկանգամյա գաղտնաբառի գործիք:.
> Լրացուցիչ տեղեկություններ. <https://www.nongnu.org/oath-toolkit/oathtool.1.html>:.

- Ստեղծեք TOTP նշան (գործում է Google Authenticator-ի նման).:

`oathtool --totp {{[-b|--base32]}} "{{secret}}"`

- Ստեղծեք TOTP նշան որոշակի ժամանակի համար.:

`oathtool --totp {{[-N|--now]}} "{{2004-02-29 16:21:42}}" {{[-b|--base32]}} "{{secret}}"`

- Վավերացրեք TOTP նշանը.:

`oathtool --totp {{[-b|--base32]}} "{{secret}}" "{{token}}"`
