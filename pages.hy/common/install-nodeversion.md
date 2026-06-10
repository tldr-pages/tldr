# Install-NodeVersion

> Տեղադրեք Node.js գործարկման ժամանակի տարբերակները `ps-nvm`-ի համար:.
> Այս հրամանը `ps-nvm`-ի մասն է և կարող է գործարկվել միայն PowerShell-ի տակ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/aaronpowell/ps-nvm>:.

- Տեղադրեք հատուկ Node.js տարբերակ.:

`Install-NodeVersion {{node_version}}`

- Տեղադրեք Node.js բազմաթիվ տարբերակներ.:

`Install-NodeVersion {{node_version1 , node_version2 , ...}}`

- Տեղադրեք Node.js 20-ի վերջին հասանելի տարբերակը:

`Install-NodeVersion ^20`

- Տեղադրեք Node.js-ի x86 (x86 32-bit) / x64 (x86 64-bit) / arm64 (ARM 64-bit) տարբերակը:

`Install-NodeVersion {{node_version}} -Architecture {{x86|x64|arm64}}`

- Node.js-ը ներբեռնելու համար օգտագործեք HTTP վստահված անձ:

`Install-NodeVersion {{node-version}} -Proxy {{http://example.com}}`
