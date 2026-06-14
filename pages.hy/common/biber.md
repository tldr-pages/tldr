#բիբեր

> `biblatex` փաթեթի հետին պլանի մատենագրության պրոցեսոր:.
> Տես նաև՝ `latexmk`:.
> Լրացուցիչ տեղեկություններ. <https://texdoc.org/serve/biber.pdf/0#section.3>:.

- Ստեղծեք մատենագիտական տվյալներ՝ օգտագործելով BibLaTeX Control File.:

`biber {{path/to/file.bcf}}`

- Ստեղծեք մատենագիտական տվյալներ՝ օգտագործելով կազմաձևման ֆայլը.:

`biber {{path/to/file.bcf}} {{[-g|--configfile]}} {{path/to/config_file}}`

- Միացնել վրիպազերծումը.:

`biber {{path/to/file.bcf}} {{[-D|--debug]}}`
