# gpg-zip

> Գաղտնագրեք ֆայլերը և գրացուցակները արխիվում՝ օգտագործելով GPG:.
> Լրացուցիչ տեղեկություններ. <https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html>:.

- Գաղտնագրեք գրացուցակը `archive.gpg`-ում՝ օգտագործելով անցաբառը՝:

`gpg-zip {{[-c|--symmetric]}} {{[-o|--output]}} {{archive.gpg}} {{path/to/directory}}`

- Ապակոդավորել `archive.gpg`-ը նույն անունով գրացուցակի մեջ.:

`gpg-zip {{[-d|--decrypt]}} {{path/to/archive.gpg}}`

- Թվարկեք կոդավորված `archive.gpg` բովանդակությունը.:

`gpg-zip --list-archive {{path/to/archive.gpg}}`
