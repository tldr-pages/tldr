# Set-NodeVersion

> Սահմանեք Node.js-ի կանխադրված տարբերակը `ps-nvm`-ի համար:.
> `ps-nvm`-ի մի մասը և կարող է գործարկվել միայն PowerShell-ով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/aaronpowell/ps-nvm>:.

- Օգտագործեք Node.js-ի հատուկ տարբերակը ընթացիկ PowerShell նիստում.:

`Set-NodeVersion {{node_version}}`

- Օգտագործեք վերջին տեղադրված Node.js տարբերակը 20.x:

`Set-NodeVersion ^20`

- Սահմանեք Node.js-ի լռելյայն տարբերակը ընթացիկ օգտագործողի համար (կիրառվում է միայն ապագա PowerShell նիստերի համար).:

`Set-NodeVersion {{node_version}} -Persist User`

- Սահմանեք Node.js-ի լռելյայն տարբերակը բոլոր օգտատերերի համար (պետք է գործարկվի որպես Administrator/root և կիրառելի է միայն PowerShell-ի ապագա նիստերին).:

`Set-NodeVersion {{node_version}} -Persist Machine`
