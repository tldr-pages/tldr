# lateexpand

> Պարզեցրեք LaTeX աղբյուրի ֆայլերը՝ հեռացնելով մեկնաբանությունները և լուծելով `\include`s, `\input`s և այլն:.
> Լրացուցիչ տեղեկություններ. <https://www.ctan.org/pkg/latexpand>:.

- Պարզեցրեք նշված աղբյուրի ֆայլը և արդյունքը պահպանեք նշված ելքային ֆայլում.:

`latexpand {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- Մի հեռացրեք մեկնաբանությունները.:

`latexpand --keep-comments {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- Մի ընդլայնեք `\include`s, `\input`s և այլն:

`latexpand --keep-includes {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- Ընդարձակեք `\usepackage`s այնքան, որքան հնարավոր է գտնել համապատասխան STY ֆայլերը.:

`latexpand --expand-usepackage {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- Ներդիր նշված BBL ֆայլը.:

`latexpand --expand-bbl {{path/to/bibliography.bbl}} {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`
