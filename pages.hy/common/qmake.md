# qmake

> Ստեղծեք Makefiles Qt նախագծի ֆայլերից:.
> Լրացուցիչ տեղեկություններ. <https://doc.qt.io/qt-6/qmake-running.html>:.

- Ստեղծեք `Makefile` ծրագրի ֆայլից ընթացիկ գրացուցակում.:

`qmake`

- Նշեք `Makefile` և նախագծի ֆայլերի գտնվելու վայրը՝:

`qmake -o {{path/to/Makefile}} {{path/to/project_file.pro}}`

- Ստեղծեք լռելյայն նախագծի ֆայլ.:

`qmake -project`

- Կազմել նախագիծ.:

`qmake && make`

- Միացնել վրիպազերծման ռեժիմը.:

`qmake -d`

- Ցուցադրել օգնությունը.:

`qmake -help`
