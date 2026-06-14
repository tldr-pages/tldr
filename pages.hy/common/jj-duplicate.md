# jj կրկնօրինակ

> Ստեղծեք նոր փոփոխություններ նույն բովանդակությամբ, ինչ գոյություն ունեցողները:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-duplicate>:.

- Կրկնօրինակեք ընթացիկ վերանայումը իր գոյություն ունեցող մայրիկի վրա.:

`jj duplicate`

- Կրկնօրինակեք հատուկ վերանայում իր գոյություն ունեցող ծնողի վրա.:

`jj duplicate {{revset}}`

- Կրկնօրինակեք վերանայումը մեկ այլ ծնողի վրա.:

`jj duplicate {{[-d|--destination]}} {{dest_revset}} {{revset}}`

- Կրկնօրինակեք վերանայումը և տեղադրեք այն այլ վերանայում(ներ)ից հետո.:

`jj duplicate {{[-A|--insert-after]}} {{after_revset}} {{revset}}`

- Կրկնօրինակեք վերանայումը և տեղադրեք այն այլ վերանայում(ներ)ից առաջ.:

`jj duplicate {{[-B|--insert-before]}} {{before_revset}} {{revset}}`

- Կրկնօրինակեք բազմաթիվ ծնողների վրա (ստեղծում է միաձուլման պարտավորություն).:

`jj duplicate {{[-d|--destination]}} {{destination1}} {{[-d|--destination]}} {{destination2}} {{revset}}`

- Կրկնօրինակեք բազմաթիվ վերանայումներ.:

`jj duplicate {{revset1 revset2 ...}}`
