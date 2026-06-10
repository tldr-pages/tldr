# shellcheck

> Ստատիկ կերպով ստուգեք shell-ի սկրիպտները սխալների, հնացած/անապահով գործառույթների օգտագործման և վատ պրակտիկայի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/koalaman/shellcheck/wiki>:.

- Ստուգեք shell script-ը.:

`shellcheck {{path/to/script.sh}}`

- Ստուգեք shell script-ը` այն մեկնաբանելով որպես նշված shell-ի բարբառ (գերակայում է սկրիպտի վերևում գտնվող shebang-ը).:

`shellcheck {{[-s|--shell]}} {{sh|bash|dash|ksh}} {{path/to/script.sh}}`

- Անտեսեք մեկ կամ մի քանի սխալի տեսակներ.:

`shellcheck {{[-e|--exclude]}} {{SC1009,SC1073,...}} {{path/to/script.sh}}`

- Նաև ստուգեք ցանկացած աղբյուրի կեղևի սցենար.:

`shellcheck {{[-a|--check-sourced]}} {{path/to/script.sh}}`

- Ցուցադրել ելքը նշված ձևաչափով (կանխադրված է `tty`):

`shellcheck {{[-f|--format]}} {{tty|checkstyle|diff|gcc|json|json1|quiet}} {{path/to/script.sh}}`

- Միացնել մեկ կամ մի քանի [o]ընտրովի ստուգումներ.:

`shellcheck {{[-o|--enable]}} {{add-default-case,avoid-nullary-conditions,...}} {{path/to/script.sh}}`

- Թվարկեք բոլոր առկա կամընտիր ստուգումները, որոնք անջատված են լռելյայնորեն.:

`shellcheck --list-optional`

- Կարգավորեք խստության մակարդակը, որը պետք է դիտարկել (կանխադրված է `style`):

`shellcheck {{[-S|--severity]}} {{error|warning|info|style}} {{path/to/script.sh}}`
