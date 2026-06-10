# pax

> Արխիվացման և պատճենահանման ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pax.1p>:.

- Թվարկեք արխիվի բովանդակությունը.:

`pax -f {{archive.tar}}`

- Թվարկեք `gzip` արխիվի բովանդակությունը.:

`pax -zf {{archive.tar.gz}}`

- Ստեղծեք արխիվ ֆայլերից.:

`pax -wf {{target.tar}} {{path/to/file1 path/to/file2 ...}}`

- Ստեղծեք արխիվ ֆայլերից՝ օգտագործելով ելքային վերահղումը.:

`pax -w {{path/to/file1 path/to/file2 ...}} > {{target.tar}}`

- Արխիվ հանեք ընթացիկ գրացուցակում.:

`pax -rf {{source.tar}}`

- Պատճենել գրացուցակում՝ պահպանելով բնօրինակ մետատվյալները. `target/` պետք է գոյություն ունենա՝:

`pax -rw {{path/to/file1}} {{path/to/directory1 path/to/directory2 ...}} {{target/}}`
