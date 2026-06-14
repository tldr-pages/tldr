# pbzip2

> `bzip2` ֆայլերի կոմպրեսորի զուգահեռ իրականացում:.
> Տես նաև՝ `bzip2`, `tar`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pbzip2>:.

- Կոմպրես ֆայլ.:

`pbzip2 {{path/to/file}}`

- Կոմպրես ֆայլը՝ օգտագործելով պրոցեսորների նշված քանակությունը.:

`pbzip2 -p{{4}} {{path/to/file}}`

- Կոմպրես կուպրի հետ համատեղ (տարբերակները կարող են փոխանցվել `pbzip2`-ին):

`tar -cf {{path/to/compressed_file}}.tar.bz2 {{[-I|--use-compress-program]}} "pbzip2 {{-option1 -option2 ...}}" {{path/to/file}}`

- Ապասեղմել ֆայլը.:

`pbzip2 {{[-d|--decompress]}} {{path/to/compressed_file.bz2}}`

- Ցուցադրել օգնությունը.:

`pbzip2 {{[-h|--help]}}`
