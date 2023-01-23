# lmms

> Ingyenes, nyílt forráskódú, platformokon átívelő digitális audio munkaállomás. `.mmp` vagy `.mmpz` projektfájlok renderelése, `.mmpz` dumpolása XML-ként, vagy a GUI elindítása. További információ: <https://lmms.io>.

- A GUI elindítása:

`lmms`

- A GUI elindítása és külső konfiguráció betöltése:

`lmms --config {{path/to/config.xml}}`

- Indítsa el a GUI-t és importáljon MIDI vagy Hydrogen fájlt:

`lmms --import {{path/to/midi/or/hydrogen/file}}`

- A GUI elindítása megadott ablakmérettel:

`lmms --geometry {{x_size}}x{{y_size}}+{{x_offset}}+{{y_offset}}`

- Dump egy `.mmpz` fájlt:

`lmms dump {{path/to/mmpz/file.mmpz}}`

- Projektfájl renderelése:

`lmms render {{path/to/mmpz_or_mmp/file}}`

- Egy projektfájl egyes sávjainak renderelése:

`lmms rendertracks {{path/to/mmpz_or_mmp/file}} {{path/to/dump/directory}}`

- Renderelés egyéni samplerátával, formátummal és loopként:

`lmms render --samplerate {{88200}} --format {{ogg}} --loop --output {{path/to/output/file.ogg}}`
