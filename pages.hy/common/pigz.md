# խոզ

> Multithreaded zlib սեղմման կոմունալ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pigz>:.

- Սեղմեք ֆայլը լռելյայն ընտրանքներով.:

`pigz {{path/to/file}}`

- Կոմպրես ֆայլը՝ օգտագործելով սեղմման լավագույն մեթոդը.:

`pigz {{[-9|--best]}} {{path/to/file}}`

- Սեղմեք ֆայլը առանց սեղմման և 4 պրոցեսորների.:

`pigz -0 {{[-p|--processes]}} {{4}} {{path/to/file}}`

- Կոմպրես գրացուցակը օգտագործելով tar:

`tar cf - {{path/to/directory}} | pigz > {{path/to/file.tar.gz}}`

- Ապասեղմել ֆայլը.:

`pigz {{[-d|--decompress]}} {{archive.gz}}`

- Թվարկեք արխիվի բովանդակությունը.:

`pigz {{[-l|--list]}} {{archive.tar.gz}}`
