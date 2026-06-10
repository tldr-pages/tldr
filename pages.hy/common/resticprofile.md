# restiprofile

> Կազմաձևման պրոֆիլների կառավարիչ՝ ռեստիկ պահուստավորման համար:.
> Տես նաև՝ `restic`, `resticprofile-schedule`, `resticprofile-unschedule`:.
> Լրացուցիչ տեղեկություններ. <https://creativeprojects.github.io/resticprofile/configuration/getting_started/index.html#write-your-first-configuration-file>:.

- Թվարկեք բոլոր պահպանված նկարները.:

`resticprofile`

- Կատարեք կրկնօրինակում լռելյայն պրոֆիլում.:

`resticprofile backup`

- Աշխատեք հատուկ պրոֆիլով կրկնօրինակում (կանխադրված պրոֆիլը «կանխադրված» է).:

`resticprofile {{[-n|--name]}} "{{profile_name}}" backup`

- Գործարկեք չոր ռեժիմով և ցույց տվեք հիմքում ընկած մնացած հրամանները.:

`resticprofile --dry-run backup`

- Ցուցադրել բոլոր պրոֆիլների անունները կազմաձևման ֆայլից.:

`resticprofile profiles`

- Ստեղծեք կեղևի ավարտումներ.:

`resticprofile generate {{--bash-completion|--zsh-completion}}`

- Ցույց տալ պրոֆիլի բոլոր մանրամասները.:

`resticprofile show {{[-n|--name]}} "{{profile_name}}"`
