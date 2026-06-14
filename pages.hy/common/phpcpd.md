# phpcpd

> Պատճենեք և տեղադրեք դետեկտոր PHP կոդի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sebastianbergmann/phpcpd>:.

- Վերլուծեք կրկնօրինակված կոդը որոշակի ֆայլի կամ գրացուցակի համար.:

`phpcpd {{path/to/file_or_directory}}`

- Վերլուծել՝ օգտագործելով փոփոխականների անունների անորոշ համընկնումը.:

`phpcpd --fuzzy {{path/to/file_or_directory}}`

- Նշեք նույնական տողերի նվազագույն քանակը (կանխադրված է 5).:

`phpcpd --min-lines {{number_of_lines}} {{path/to/file_or_directory}}`

- Նշեք նույնական նշանների նվազագույն քանակը (կանխադրված մինչև 70):

`phpcpd --min-tokens {{number_of_tokens}} {{path/to/file_or_directory}}`

- Բացառել գրացուցակը վերլուծությունից (պետք է հարաբերական լինի աղբյուրին).:

`phpcpd --exclude {{path/to/excluded_directory}} {{path/to/file_or_directory}}`

- Արդյունքները դուրս բերեք PHP-CPD XML ֆայլ.:

`phpcpd --log-pmd {{path/to/log_file}} {{path/to/file_or_directory}}`
