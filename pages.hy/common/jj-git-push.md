# jj git հրում

> Հրել դեպի Git հեռակառավարման վահանակ:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-git-push>:.

- Սեղմեք էջանիշը տվյալ հեռակառավարման վրա (կանխադրված է `git.push` կարգավորումը):

`jj git push {{[-b|--bookmark]}} {{bookmark}} --remote {{remote}}`

- Հրել նոր էջանիշ.:

`jj git push {{[-b|--bookmark]}} {{bookmark}} {{[-N|--allow-new]}}`

- Հրել բոլոր հետևված էջանիշները.:

`jj git push --tracked`

- Հպեք բոլոր էջանիշները (ներառյալ նոր էջանիշները).:

`jj git push --all`

- Հրել բոլոր էջանիշները, որոնք մատնանշում են տրված վերանայումները.:

`jj git push {{[-r|--revisions]}} {{revset}}`

- Հրել փոփոխությունները/պարտավորությունները՝ ստեղծելով նոր էջանիշներ (Անվան ձևաչափը ըստ `templates.git_push_bookmark` պարամետրի, լռելյայն՝ `"push-" ++ change_id.short()`):

`jj git push {{[-c|--change]}} {{revset}}`

- Հրավիրեք վերանայում տրված անունով.:

`jj git push --named {{name}}={{revision}}`
