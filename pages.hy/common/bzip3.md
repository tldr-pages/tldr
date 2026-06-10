# bzip3

> Արդյունավետ վիճակագրական ֆայլերի կոմպրեսոր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/bzip3>:.

- Կոմպրես ֆայլ.:

`bzip3 {{path/to/file_to_compress}}`

- Ապասեղմել ֆայլը.:

`bzip3 {{[-d|--decode]}} {{path/to/compressed_file.bz3}}`

- Անջատեք ֆայլը `stdout`:

`bzip3 {{[-dc|--decode --stdout]}} {{path/to/compressed_file.bz3}}`

- Ստուգեք յուրաքանչյուր ֆայլի ամբողջականությունը արխիվային ֆայլի ներսում.:

`bzip3 {{[-t|--test]}} {{path/to/compressed_file.bz3}}`

- Ցույց տվեք սեղմման հարաբերակցությունը մանրամասն տեղեկություններով մշակված յուրաքանչյուր ֆայլի համար.:

`bzip3 {{[-v|--verbose]}} {{path/to/compressed_files.bz3}}`

- Ապասեղմեք գոյություն ունեցող ֆայլերը վերագրող ֆայլը.:

`bzip3 {{[-d|--decode]}} {{[-f|--force]}} {{path/to/compressed_file.bz3}}`

- Ցուցադրել օգնությունը.:

`bzip3 {{[-h|--help]}}`
