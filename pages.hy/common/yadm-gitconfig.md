# yadm gitconfig

> Փոխանցել ընտրանքները `git config`-ին: Փոխեք yadm-ի կողմից կառավարվող պահեստի `.gitconfig`-ը:.
> Տես նաև՝ `git config`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>:.

- Թարմացրեք կամ սահմանեք Git-ի կազմաձևման արժեքը.:

`yadm gitconfig {{key.inner-key}} {{value}}`

- Ստացեք արժեք yadm-ի Git կոնֆիգուրացիայից.:

`yadm gitconfig --get {{key}}`

- Չեղարկեք արժեքը yadm-ի Git-ի կազմաձևում.:

`yadm gitconfig --unset {{key}}`

- Թվարկեք բոլոր արժեքները yadm-ի Git կազմաձևման մեջ.:

`yadm gitconfig --list`
