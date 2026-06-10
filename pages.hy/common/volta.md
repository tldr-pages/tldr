#վոլտա

> JavaScript Tool Manager-ը, որը տեղադրում է Node.js-ի գործարկման ժամանակները, npm և Yarn փաթեթների կառավարիչները կամ npm-ից ցանկացած երկուական:.
> Լրացուցիչ տեղեկություններ. <https://docs.volta.sh/reference/>:.

- Թվարկեք բոլոր տեղադրված գործիքները.:

`volta list`

- Տեղադրեք գործիքի վերջին տարբերակը.:

`volta install {{node|npm|yarn|package_name}}`

- Տեղադրեք գործիքի որոշակի տարբերակ.:

`volta install {{node|npm|yarn}}@version`

- Ծրագրի համար ընտրեք գործիքի տարբերակը (այն կպահի `package.json`-ում):

`volta pin {{node|npm|yarn}}@version`

- Ցուցադրել օգնությունը.:

`volta help`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`volta help {{fetch|install|uninstall|pin|list|completions|which|setup|run|help}}`
