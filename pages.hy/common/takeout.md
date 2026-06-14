#հանում

> Docker-ի վրա հիմնված միայն կախվածության կառավարիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tighten/takeout>:.

- Ցուցադրել առկա ծառայությունների ցանկը.:

`takeout enable`

- Միացնել հատուկ ծառայություն.:

`takeout enable {{name}}`

- Միացնել որոշակի ծառայություն լռելյայն պարամետրերով.:

`takeout enable --default {{name}}`

- Ցուցադրել միացված ծառայությունների ցանկը.:

`takeout disable`

- Անջատել հատուկ ծառայություն.:

`takeout disable {{name}}`

- Անջատել բոլոր ծառայությունները.:

`takeout disable --all`

- Սկսեք կոնկրետ կոնտեյներ.:

`takeout start {{container_id}}`

- Դադարեցրեք կոնկրետ կոնտեյներ.:

`takeout stop {{container_id}}`
