# lz4

> Սեղմել կամ ապասեղմել .lz4 ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/lz4/lz4>:.

- Կոմպրես ֆայլ.:

`lz4 {{path/to/file}}`

- Ապասեղմել ֆայլը.:

`lz4 {{[-d|--decompress]}} {{file.lz4}}`

- Ապասեղմեք ֆայլը և գրեք `stdout`:

`lz4 {{[-dc|--decompress --stdout]}} {{file.lz4}}`

- Փաթեթավորել և սեղմել գրացուցակը և դրա բովանդակությունը.:

`tar cvf - {{path/to/directory}} | lz4 - {{dir.tar.lz4}}`

- Անջատեք և բացեք գրացուցակը և դրա բովանդակությունը.:

`lz4 {{[-dc|--decompress --stdout]}} {{dir.tar.lz4}} | tar -xv`

- Սեղմեք ֆայլը, օգտագործելով լավագույն սեղմումը.:

`lz4 {{[-12|--best]}} {{path/to/file}}`
