# qpdf

> Բազմակողմանի PDF վերափոխման ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/qpdf>:.

- Քաղեք 1-3, 5 և 6-10 էջերը PDF ֆայլից և պահեք դրանք որպես մեկ այլ:

`qpdf --empty --pages {{path/to/input.pdf}} {{1-3,5,6-10}} -- {{path/to/output.pdf}}`

- Միավորել (միավորել) բազմաթիվ PDF ֆայլերի բոլոր էջերը և պահպանել արդյունքը որպես նոր PDF.:

`qpdf --empty --pages {{path/to/file1.pdf file2.pdf ...}} -- {{path/to/output.pdf}}`

- Միավորել (միավորել) տրված էջերը PDF ֆայլերի ցանկից և պահպանել արդյունքը որպես նոր PDF.:

`qpdf --empty --pages {{path/to/file1.pdf}} {{1,6-8}} {{path/to/file2.pdf}} {{3,4,5}} -- {{path/to/output.pdf}}`

- Գրեք `n` էջերի յուրաքանչյուր խումբ առանձին ելքային ֆայլում՝ տվյալ ֆայլի անվան օրինակով.:

`qpdf --split-pages={{n}} {{path/to/input.pdf}} {{path/to/out_%d.pdf}}`

- Պտտեցնել PDF-ի որոշակի էջերը տվյալ անկյան տակ.:

`qpdf --rotate={{90:2,4,6}} --rotate={{180:7-8}} {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Հեռացրեք գաղտնաբառը գաղտնաբառով պաշտպանված ֆայլից.:

`qpdf --password={{password}} --decrypt {{path/to/input.pdf}} {{path/to/output.pdf}}`
