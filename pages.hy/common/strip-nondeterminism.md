# strip-nodeterminism

> Հեռացրեք ոչ դետերմինիստական տեղեկատվությունը (օրինակ՝ ժամանակի դրոշմանիշերը) ֆայլերից:.
> Լրացուցիչ տեղեկություններ. <https://salsa.debian.org/reproducible-builds/strip-nondeterminism>:.

- Ֆայլից հանել ոչ դետերմինիստական տեղեկատվությունը.:

`strip-nondeterminism {{path/to/file}}`

- Հեռացրեք ոչ որոշիչ տեղեկատվությունը ֆայլից՝ ձեռքով նշելով ֆայլի տեսակը.:

`strip-nondeterminism --type {{filetype}} {{path/to/file}}`

- Հեռացնել ոչ որոշիչ տեղեկատվությունը ֆայլից. Ժամադրոշմները հեռացնելու փոխարեն դրանք սահմանեք նշված UNIX ժամադրոշմին՝:

`strip-nondeterminism --timestamp {{unix_timestamp}} {{path/to/file}}`
