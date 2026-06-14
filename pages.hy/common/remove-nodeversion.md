# Remove-NodeVersion

> Տեղահանել Node.js գործարկման ժամանակի տարբերակները `ps-nvm`-ի համար:.
> Այս հրամանը `ps-nvm`-ի մասն է և կարող է գործարկվել միայն PowerShell-ի տակ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/aaronpowell/ps-nvm>:.

- Տեղահանեք տրված Node.js տարբերակը.:

`Remove-NodeVersion {{node_version}}`

- Տեղահանեք Node.js-ի բազմաթիվ տարբերակներ.:

`Remove-NodeVersion {{node_version1 , node_version2 , ...}}`

- Տեղահանեք Node.js 20.x-ի ներկայումս տեղադրված բոլոր տարբերակները:

`Get-NodeVersions -Filter ">=20.0.0 <21.0.0" | Remove-NodeVersion`

- Տեղահանել Node.js-ի բոլոր ներկայումս տեղադրված տարբերակները.:

`Get-NodeVersions | Remove-NodeVersion`
