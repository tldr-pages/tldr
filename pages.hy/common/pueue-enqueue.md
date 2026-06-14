# pueue հերթ

> Հերթագրեք փակված առաջադրանքները:.
> Տես նաև՝ `pueue stash`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Nukesor/pueue#how-to-use-it>:.

- Հերթագրեք մի քանի գաղտնի առաջադրանքներ միանգամից.:

`pueue enqueue {{task_id}} {{task_id}}`

- Հերթագրեք փակված առաջադրանքը 60 վայրկյան հետո.:

`pueue enqueue {{[-d|--delay]}} {{60}} {{task_id}}`

- Հերթագրեք փակված առաջադրանքը հաջորդ չորեքշաբթի.:

`pueue enqueue {{[-d|--delay]}} {{wednesday}} {{task_id}}`

- Չորս ամիս հետո հերթագրեք փակված առաջադրանքը.:

`pueue enqueue {{[-d|--delay]}} "4 months" {{task_id}}`

- Հերթագրեք փակված առաջադրանքը 2021-02-19:

`pueue enqueue {{[-d|--delay]}} {{2021-02-19}} {{task_id}}`

- Թվարկեք բոլոր հասանելի ամսաթվի/ժամային ձևաչափերը.:

`pueue enqueue {{[-h|--help]}}`
