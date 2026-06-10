# jj պառակտում

> Բաժանեք վերանայումը երկու մասի:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-split>:.

- Տրված վերանայումը ինտերակտիվ կերպով բաժանեք երկու մասի՝ դրա վրա դնելով երկրորդ տարբերակը.:

`jj split {{[-r|--revision]}} {{revision}}`

- Բաժանել համապատասխան ֆայլերը տվյալ վերանայումից.:

`jj split {{[-r|--revision]}} {{revision}} {{fileset}}`

- Տրված վերանայումը բաժանեք՝ երկրորդ տարբերակը դնելով տվյալ նպատակակետ(ների) վերևում.:

`jj split {{[-r|--revision]}} {{revision}} {{[-d|--destination]}} {{revset}}`

- Տրված վերանայումը բաժանեք՝ երկրորդը դնելով այլ վերանայումից առաջ և/կամ հետո.:

`jj split {{[-r|--revision]}} {{revision}} {{[-B|--insert-before]}} {{revset}} {{[-A|--insert-after]}} {{revset}}`

- Տրված վերանայումը բաժանեք երկու զուգահեռ վերանայումների.:

`jj split {{[-r|--revision]}} {{revision}} {{[-p|--parallel]}}`
