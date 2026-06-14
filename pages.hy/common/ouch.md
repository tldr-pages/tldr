#վախ

> Կոմունալ ֆայլերի և գրացուցակների սեղմման և ապասեղմման համար:.
> Լրացուցիչ տեղեկություններ. <https://crates.io/crates/ouch>:.

- Կողմնորոշեք որոշակի ֆայլ.:

`ouch decompress {{path/to/archive.tar.xz}}`

- Անջատեք ֆայլը որոշակի վայրում.:

`ouch decompress {{path/to/archive.tar.xz}} --dir {{path/to/directory}}`

- Ապասեղմեք բազմաթիվ ֆայլեր.:

`ouch decompress {{path/to/archive1.tar path/to/archive2.tar.gz ...}}`

- Սեղմել ֆայլերը.:

`ouch compress {{path/to/file1 path/to/file2 ...}} {{path/to/archive.zip}}`
