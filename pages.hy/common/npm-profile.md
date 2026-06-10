# npm պրոֆիլ

> Կառավարեք npm պրոֆիլը և հարակից կարգավորումները:.
> Նշում. այս հրամանը տեղյակ չէ աշխատանքային տարածքների մասին:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-profile/>:.

- Դիտեք npm պրոֆիլի մանրամասները.:

`npm profile get`

- Դիտեք պրոֆիլի որոշակի հատկություն.:

`npm profile get {{property}}`

- Սահմանել կամ թարմացնել պրոֆիլի հատկությունը.:

`npm profile set {{property}} {{value}}`

- Սահմանեք հանրային էլփոստի հասցեն.:

`npm profile set email {{email}}`

- Սահմանեք հանրային անունը.:

`npm profile set fullname {{name}}`

- Սահմանեք նոր գաղտնաբառ ինտերակտիվ կերպով.:

`npm profile set password`

- Միացնել երկու գործոնով նույնականացումը (2FA) (կանխադրված է `auth-and-writes`):

`npm profile enable-2fa {{auth-only|auth-and-writes}}`

- Անջատել երկգործոն նույնականացումը (2FA).:

`npm profile disable-2fa`
