#ստիկ

> Արագ և ապահով պահուստավորման ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://restic.readthedocs.io/en/stable/manual_rest.html#usage-help>:.

- Նախաձեռնեք պահեստային պահոցը նշված տեղական գրացուցակում.:

`restic init {{[-r|--repo]}} {{path/to/repository}}`

- Կրկնօրինակեք գրացուցակը պահեստում.:

`restic {{[-r|--repo]}} {{path/to/repository}} backup {{path/to/directory}}`

- Ցույց տալ պահուստում պահվող պահուստային նկարները.:

`restic {{[-r|--repo]}} {{path/to/repository}} snapshots`

- Վերականգնել հատուկ պահուստային նկարը թիրախային գրացուցակում.:

`restic {{[-r|--repo]}} {{path/to/repository}} restore {{latest|snapshot_id}} --target {{path/to/target}}`

- Վերականգնել հատուկ ուղին հատուկ պահուստից մինչև թիրախային գրացուցակ.:

`restic {{[-r|--repo]}} {{path/to/repository}} restore {{snapshot_id}} --target {{path/to/target}} --include {{path/to/restore}}`

- Մաքրեք պահեստը և պահեք յուրաքանչյուր եզակի կրկնօրինակի միայն ամենավերջին նկարը.:

`restic forget --keep-last 1 --prune`
