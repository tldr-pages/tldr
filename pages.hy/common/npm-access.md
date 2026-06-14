# npm մուտք

> Սահմանել մուտքի մակարդակը հրապարակված փաթեթների վրա:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-access/>:.

- Ցուցակեք փաթեթները օգտվողի կամ շրջանակի համար.:

`npm access list packages {{user|scope|scope:team}} {{package_name}}`

- Թվարկեք համահեղինակներին փաթեթում.:

`npm access list collaborators {{package_name}} {{username}}`

- Ստացեք փաթեթի կարգավիճակ.:

`npm access get status {{package_name}}`

- Սահմանեք փաթեթի կարգավիճակը (հանրային կամ մասնավոր).:

`npm access set status={{public|private}} {{package_name}}`

- Փաթեթի հասանելիության տրամադրում.:

`npm access grant {{read-only|read-write}} {{scope:team}} {{package_name}}`

- Չեղյալ համարել փաթեթի հասանելիությունը.:

`npm access revoke {{scope:team}} {{package_name}}`

- Կազմաձևեք երկու գործոն նույնականացման պահանջը.:

`npm access set mfa={{none|publish|automation}} {{package_name}}`
