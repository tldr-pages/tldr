# bzip2

> Բլոկ-տեսակավորող ֆայլերի կոմպրեսոր:.
> Տես նաև՝ `bzcat`, `bunzip2`, `bzip2recover`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/bzip2>:.

- Կոմպրես ֆայլ.:

`bzip2 {{path/to/file_to_compress}}`

- Ապասեղմել ֆայլը.:

`bzip2 {{[-d|--decompress]}} {{path/to/compressed_file.bz2}}`

- Անջատեք ֆայլը `stdout`:

`bzip2 {{[-dc|--decompress --stdout]}} {{path/to/compressed_file.bz2}}`

- Ստուգեք յուրաքանչյուր ֆայլի ամբողջականությունը արխիվային ֆայլի ներսում.:

`bzip2 {{[-t|--test]}} {{path/to/compressed_file.bz2}}`

- Ցույց տվեք սեղմման հարաբերակցությունը մանրամասն տեղեկություններով մշակված յուրաքանչյուր ֆայլի համար.:

`bzip2 {{[-v|--verbose]}} {{path/to/compressed_files.bz2}}`

- Ապասեղմեք գոյություն ունեցող ֆայլերը վերագրող ֆայլը.:

`bzip2 {{[-f|--force]}} {{path/to/compressed_file.bz2}}`

- Ցուցադրել օգնությունը.:

`bzip2 {{[-h|--help]}}`
