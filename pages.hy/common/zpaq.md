# zpaq

> Ավելացվող մատյանների կրկնօրինակում և արխիվատոր:.
> Լրացուցիչ տեղեկություններ. <https://mattmahoney.net/dc/zpaqdoc.html>:.

- Ավելացնել ֆայլ կամ գրացուցակ նոր կամ գոյություն ունեցող արխիվում.:

`zpaq {{[a|add]}} {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- Ստեղծեք կամ ավելացրեք կոդավորված արխիվում.:

`zpaq {{[a|add]}} -k{{password}} {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- Արտահանեք ֆայլերի ամենավերջին տարբերակները.:

`zpaq {{[x|extract]}} {{path/to/archive.zpaq}}`

- Թվարկեք արխիվի բովանդակությունը.:

`zpaq {{[l|list]}} {{path/to/archive.zpaq}}`

- Սահմանեք սեղմման մակարդակը (ավելի բարձր նշանակում է ավելի շատ սեղմում, բայց ավելի դանդաղ).:

`zpaq {{[a|add]}} {{path/to/archive.zpaq}} -m{{1|2|3|4|5}} {{path/to/file_or_directory}}`

- Արխիվից հանեք նշված ֆայլերը, որոնք նշված ամսաթվից ավելի նոր չեն.:

`zpaq {{[x|extract]}} {{path/to/archive.zpaq}} {{path/in/archive/to/extract}} -to {{path/to/output}} -until {{YYYY-MM-DD}}`
