# Get-NodeVersions

> Ցանկ `ps-nvm`-ի համար տեղադրված և հասանելի Node.js տարբերակները:.
> `ps-nvm`-ի մի մասը և կարող է գործարկվել միայն PowerShell-ով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/aaronpowell/ps-nvm>:.

- Թվարկեք բոլոր տեղադրված Node.js տարբերակները.:

`Get-NodeVersions`

- Նշեք Node.js-ի բոլոր հասանելի տարբերակները.:

`Get-NodeVersions -Remote`

- Թվարկեք Node.js 20.x բոլոր հասանելի տարբերակները.:

`Get-NodeVersions -Remote -Filter ">=20.0.0 <21.0.0"`
