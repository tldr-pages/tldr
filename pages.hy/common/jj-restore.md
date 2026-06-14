# jj վերականգնել

> Վերականգնել ֆայլերը մեկ այլ տարբերակից:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-restore>:.

- Վերականգնել ֆայլերը վերանայումից մեկ այլ տարբերակի.:

`jj restore {{[-f|--from]}} {{revset}} {{[-t|--into]}} {{revset}} {{filesets}}`

- Չեղարկել վերանայման փոփոխությունները՝ համեմատած դրա ծնողների միաձուլման հետ.:

`jj restore {{[-c|--changes-in]}} {{revset}} {{filesets}}`

- Ինտերակտիվ կերպով ընտրեք, թե որ մասերը վերականգնելու համար.:

`jj restore {{[-f|--from]}} {{revset}} {{[-t|--into]}} {{revset}} {{[-i|--interactive]}}`
