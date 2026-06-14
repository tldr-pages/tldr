# tldr

> Ցուցադրել պարզ օգնության էջեր tldr-pages նախագծի հրամանի տող գործիքների համար:.
> Նշում. `--language` և `--list` ընտրանքները չեն պահանջվում հաճախորդի հատկորոշմամբ, սակայն հաճախորդների մեծամասնությունը դրանք իրականացնում է:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>:.

- Տպեք tldr էջը կոնկրետ հրամանի համար (հուշում. ահա թե ինչպես եք այստեղ հայտնվել):

`tldr {{command}}`

- Տպեք tldr էջը հատուկ ենթահրամանի համար.:

`tldr {{command}} {{subcommand}}`

- Տպեք tldr էջը տվյալ լեզվով հրամանի համար (եթե առկա է, հակառակ դեպքում վերադարձեք անգլերեն).:

`tldr {{[-L|--language]}} {{language_code}} {{command}}`

- Տպեք tldr էջը հատուկ հարթակից հրամանի համար.:

`tldr {{[-p|--platform]}} {{android|cisco-ios|common|dos|freebsd|linux|netbsd|openbsd|osx|sunos|windows}} {{command}}`

- Թարմացրեք tldr էջերի տեղական քեշը.:

`tldr {{[-u|--update]}}`

- Թվարկե՛ք ընթացիկ հարթակի բոլոր էջերը և `common`՝:

`tldr {{[-l|--list]}}`

- Թերթիր tldr էջերը տերմինալի պատուհանում (`fzf` պետք է հասանելի լինի):

`tldr {{[-l|--list]}} | fzf --preview "tldr {1} --color=always" --preview-window=right,70% | xargs tldr`

- Տպեք tldr էջը պատահական հրամանի համար.:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
