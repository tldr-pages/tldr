# zapier

> Ստեղծեք, ավտոմատացրեք և կառավարեք zapier ինտեգրումները:.
> Որոշ ենթահրամաններ, ինչպիսիք են `build`, `init`, `scaffold`, `push`, `test` և այլն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md>:.

- Միացեք Zapier հաշվին.:

`zapier login`

- Նախաձեռնեք նոր Zapier ինտեգրումը նախագծի ձևանմուշով.:

`zapier init {{path/to/directory}}`

- Ավելացրեք մեկնարկային գործարկիչ, ստեղծեք, որոնեք կամ ռեսուրս ձեր ինտեգրմանը.:

`zapier scaffold {{trigger|create|search|resource}} {{name}}`

- Փորձարկել ինտեգրումը.:

`zapier test`

- Կառուցեք և վերբեռնեք ինտեգրում Zapier-ին.:

`zapier push`

- Ցուցադրել օգնությունը.:

`zapier help`

- Ցուցադրել օգնություն կոնկրետ հրամանի համար.:

`zapier help {{command}}`
