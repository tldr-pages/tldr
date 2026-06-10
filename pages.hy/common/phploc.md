# phploc

> Արագ չափեք PHP նախագծի չափը և վերլուծելով կառուցվածքը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sebastianbergmann/phploc>:.

- Վերլուծեք գրացուցակը և տպեք արդյունքը.:

`phploc {{path/to/directory}}`

- Ներառեք միայն կոնկրետ ֆայլեր ստորակետերով բաժանված ցուցակից (գլոբերը թույլատրվում են).:

`phploc {{path/to/directory}} --names '{{path/to/file1,path/to/file2,...}}'`

- Բացառել կոնկրետ ֆայլեր ստորակետերով բաժանված ցուցակից (գլոբերը թույլատրվում են).:

`phploc {{path/to/directory}} --names-exclude '{{path/to/file1,path/to/file2,...}}'`

- Բացառեք որոշակի գրացուցակ վերլուծությունից.:

`phploc {{path/to/directory}} --exclude {{path/to/exclude_directory}}`

- Արդյունքները գրանցեք կոնկրետ CSV ֆայլում.:

`phploc {{path/to/directory}} --log-csv {{path/to/file}}`

- Արդյունքները գրանցեք հատուկ XML ֆայլում.:

`phploc {{path/to/directory}} --log-xml {{path/to/file}}`

- Հաշվեք PHPUnit թեստային դեպքերի դասերը և փորձարկման մեթոդները.:

`phploc {{path/to/directory}} --count-tests`
