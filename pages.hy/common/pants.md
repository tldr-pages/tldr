# տաբատ

> Արագ, մասշտաբային, օգտագործողի համար հարմար, բաց կոդով կառուցման և մշակողի աշխատանքային հոսքի գործիք:.
> Լրացուցիչ տեղեկություններ. <https://www.pantsbuild.org/stable/docs/using-pants/command-line-help>:.

- Նշեք բոլոր թիրախները.:

`pants list ::`

- Գործարկել բոլոր թեստերը.:

`pants test ::`

- Ուղղեք, ձևաչափեք և տեղադրեք միայն չհաստատված ֆայլերը.:

`pants --changed-since=HEAD fix fmt lint`

- Ստուգեք միայն չհաստատված ֆայլերը և դրանց կախյալները.:

`pants --changed-since=HEAD --changed-dependents=transitive check`

- Ստեղծեք բաշխվող փաթեթ նշված թիրախի համար.:

`pants package {{path/to/directory:target-name}}`

- Ավտոմատ ստեղծեք BUILD ֆայլի թիրախները նոր աղբյուրի ֆայլերի համար.:

`pants tailor ::`

- Ցուցադրել օգնությունը.:

`pants help`
