# git արխիվ

> Ստեղծեք ֆայլերի արխիվ ծառից:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-archive>:.

- Ստեղծեք `.tar` արխիվ ընթացիկ `HEAD`-ի բովանդակությունից և տպեք այն `stdout`-ում:

`git archive {{[-v|--verbose]}} HEAD`

- Օգտագործեք Zip ձևաչափը և մանրամասնորեն զեկուցեք առաջընթացի մասին.:

`git archive {{[-v|--verbose]}} --format zip HEAD`

- Zip արխիվը թողարկեք որոշակի ֆայլ.:

`git archive {{[-v|--verbose]}} {{[-o|--output]}} {{path/to/file.zip}} HEAD`

- Ստեղծեք `.tar` արխիվ կոնկրետ մասնաճյուղի վերջին commit-ի բովանդակությունից.:

`git archive {{[-o|--output]}} {{path/to/file.tar}} {{branch_name}}`

- Օգտագործեք որոշակի գրացուցակի բովանդակությունը.:

`git archive {{[-o|--output]}} {{path/to/file.tar}} HEAD:{{path/to/directory}}`

- Պատրաստեք ուղի դեպի յուրաքանչյուր ֆայլ՝ այն արխիվացնելու համար որոշակի գրացուցակում.:

`git archive {{[-o|--output]}} {{path/to/file.tar}} --prefix {{path/to/prepend}}/ HEAD`
