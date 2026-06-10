# pbmtolj

> Փոխարկել PBM ֆայլը HP LaserJet ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmtolj.html>:.

- Փոխարկել PBM ֆայլը HP LaserJet ֆայլի.:

`pbmtolj {{path/to/input.pbm}} > {{path/to/output.lj}}`

- Սեղմեք ելքային ֆայլը նշված մեթոդով.:

`pbmtolj -{{packbits|delta|compress}} {{path/to/input.pbm}} > {{path/to/output.lj}}`

- Նշեք պահանջվող բանաձեւը.:

`pbmtolj {{[-r|-resolution]}} {{75|100|150|300|600}} {{path/to/input.pbm}} > {{path/to/output.lj}}`
