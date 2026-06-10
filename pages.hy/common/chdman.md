#չդման

> Կառավարեք և փոխակերպեք CHD (Տվյալների սեղմված հատվածներ) պատկերները:.
> Սովորաբար օգտագործվում է MAME-ի և ռետրո խաղի պատկերների հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.mamedev.org/tools/chdman.html>:.

- Ստեղծեք CHD BIN/CUE զույգից (CD-ROM պատկեր).:

`chdman createcd {{[-i|--input]}} {{path/to/file.cue}} {{[-o|--output]}} {{path/to/file.chd}}`

- Ստեղծեք CHD հում կոշտ սկավառակի պատկերից.:

`chdman createhd {{[-i|--input]}} {{path/to/disk.img}} {{[-o|--output]}} {{path/to/disk.chd}}`

- Քաղեք (ապակոմպրես) մի CHD հետ BIN/CUE:

`chdman extractcd {{[-i|--input]}} {{path/to/file.chd}} {{[-o|--output]}} {{path/to/file.cue}}`

- Ստուգեք CHD ֆայլի ամբողջականությունը.:

`chdman verify {{[-i|--input]}} {{path/to/file.chd}}`

- Դիտեք CHD մետատվյալների տեղեկատվությունը.:

`chdman info {{[-i|--input]}} {{path/to/file.chd}}`

- Թարմացրեք CHD ֆայլը վերջին ձևաչափի տարբերակին.:

`chdman copy {{[-i|--input]}} {{path/to/old_file.chd}} {{[-o|--output]}} {{path/to/new_file.chd}}`

- Վերափոխեք սեղմված կոշտ սկավառակի պատկերը չսեղմվածի (խմբագրման համար).:

`chdman extracthd {{[-i|--input]}} {{path/to/disk.chd}} {{[-o|--output]}} {{path/to/disk.img}}`
