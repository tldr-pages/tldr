#բրոտլի

> Սեղմել/անջատել ֆայլերը Brotli սեղմման միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/brotli>:.

- Սեղմեք ֆայլը, ֆայլի կողքին ստեղծելով սեղմված տարբերակ.:

`brotli {{path/to/file}}`

- Ապասեղմեք ֆայլը, ֆայլի կողքին ստեղծելով չսեղմված տարբերակ.:

`brotli {{[-d|--decompress]}} {{path/to/file.br}}`

- Սեղմեք ֆայլը, որը նշում է ելքային ֆայլի անունը.:

`brotli {{path/to/file}} {{[-o|--output]}} {{path/to/compressed_output_file.br}}`

- Decompress Brotli ֆայլը, նշելով ելքային ֆայլի անունը.:

`brotli {{[-d|--decompress]}} {{path/to/compressed_file.br}} {{[-o|--output]}} {{path/to/output_file}}`

- Նշեք սեղմման որակը (1=ամենաարագ (ամենավատ), 11=ամենադանդաղ (լավագույն)):

`brotli {{[-q|--quality]}} {{11}} {{path/to/file}} {{[-o|--output]}} {{path/to/compressed_output_file.br}}`
