# git ռեհեղինակ

> Փոխել մանրամասները հեղինակի ինքնության մասին: Քանի որ այս հրամանը վերագրում է Git պատմությունը, հաջորդ անգամ սեղմելիս անհրաժեշտ կլինի `--force`:.
> `git-extras`-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tj/git-extras/blob/main/Commands.md#git-reauthor>:.

- Փոխեք հեղինակի էլ.փոստը և անունը ամբողջ Git պահոցում.:

`git reauthor {{[-o|--old-email]}} {{old@example.com}} {{[-e|--correct-email]}} {{new@example.com}} {{[-n|--correct-name]}} "{{name}}"`

- Փոփոխեք էլփոստը և անունը Git կոնֆիգուրայում սահմանվածներին.:

`git reauthor {{[-o|--old-email]}} {{old@example.com}} {{[-c|--use-config]}}`

- Փոխեք բոլոր պարտավորությունների էլ.փոստը և անունը՝ անկախ դրանց սկզբնական հեղինակից.:

`git reauthor {{[-a|--all]}} {{[-e|--correct-email]}} {{name@example.com}} {{[-n|--correct-name]}} {{name}}`
