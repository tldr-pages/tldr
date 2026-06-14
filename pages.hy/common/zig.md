#զիգ

> Zig կոմպիլյատորը և գործիքների շղթան:.
> Լրացուցիչ տեղեկություններ. <https://ziglang.org/documentation/master/>:.

- Կազմեք նախագիծը ընթացիկ գրացուցակում.:

`zig build`

- Կազմեք և գործարկեք նախագիծը ընթացիկ գրացուցակում.:

`zig build run`

- Նախաձեռնեք `zig build` նախագիծը գրադարանով և գործարկվող.:

`zig init`

- Ստեղծեք և գործարկեք թեստային կառուցվածք.:

`zig test {{path/to/file.zig}}`

- Խաչաձև կազմեք, ստեղծեք և գործարկեք նախագիծ `x86_64` ճարտարապետության և `windows` օպերացիոն համակարգի համար.:

`zig build run -fwine -Dtarget=x86_64-windows`

- Վերափոխեք Zig աղբյուրը կանոնական ձևի.:

`zig fmt {{path/to/file.zig}}`

- Թարգմանեք C ֆայլը `zig`:

`zig translate-c -lc {{path/to/file.c}}`

- Օգտագործեք Zig-ը որպես բացվող C++ կոմպիլյատոր.:

`zig c++ {{path/to/file.cpp}}`
