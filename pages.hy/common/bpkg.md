# bpkg

> Փաթեթի կառավարիչ Bash սկրիպտների համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/bpkg/bpkg>:.

- Թարմացրեք տեղական ինդեքսը.:

`bpkg update`

- Տեղադրեք փաթեթ ամբողջ աշխարհում.:

`bpkg install --global {{package}}`

- Տեղադրեք փաթեթ ընթացիկ գրացուցակի ենթագրքում.:

`bpkg install {{package}}`

- Տեղադրեք փաթեթի որոշակի տարբերակ գլոբալ.:

`bpkg install {{package}}@{{version}} -g`

- Ցույց տալ մանրամասներ կոնկրետ փաթեթի մասին.:

`bpkg show {{package}}`

- Գործարկեք հրաման՝ ցանկության դեպքում նշելով դրա արգումենտները.:

`bpkg run {{command}} {{argument1 argument2 ...}}`
