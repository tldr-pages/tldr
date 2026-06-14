#gzip

> Սեղմել/անջատել ֆայլերը `gzip` սեղմումով (LZ77):.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/gzip/manual/gzip.html>:.

- Սեղմեք ֆայլը՝ այն փոխարինելով `gzip` արխիվով.:

`gzip {{path/to/file}}`

- Ապասեղմեք ֆայլը՝ այն փոխարինելով սկզբնական չսեղմված տարբերակով.:

`gzip {{[-d|--decompress]}} {{path/to/file.gz}}`

- Ցուցադրել անունը և կրճատման տոկոսը յուրաքանչյուր սեղմված ֆայլի համար.:

`gzip {{[-v|--verbose]}} {{path/to/file.gz}}`

- Կոմպրես ֆայլը՝ պահպանելով բնօրինակ ֆայլը.:

`gzip {{[-k|--keep]}} {{path/to/file}}`

- Սեղմեք ֆայլը՝ նշելով ելքային ֆայլի անունը.:

`gzip {{[-c|--stdout]}} {{path/to/file}} > {{path/to/compressed_file.gz}}`

- Ապասեղմեք `gzip` արխիվը՝ նշելով ելքային ֆայլի անունը.:

`gzip {{[-cd|--stdout --decompress]}} {{path/to/file.gz}} > {{path/to/uncompressed_file}}`

- Նշեք սեղմման մակարդակը: 1-ն ամենաարագն է (ցածր սեղմում), 9-ը ամենադանդաղն է (բարձր սեղմում), 6-ը լռելյայն է.:

`gzip -{{1..9}} {{[-c|--stdout]}} {{path/to/file}} > {{path/to/compressed_file.gz}}`

- Թվարկեք սեղմված ֆայլի բովանդակությունը.:

`gzip {{[-l|--list]}} {{path/to/file.txt.gz}}`
