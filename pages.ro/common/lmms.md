# lmms

> Stație de lucru audio digitală gratuită, open source, cross-platform.
> Randați un fișier de proiect `.mmpz` sau `.mmpz `, dump un `.mmpz` ca XML sau porniți GUI.
> Mai multe informaţii: <https://lmms.io>

- Porniți interfața grafică:

`lmms`

- Porniți GUI și încărcați configurația externă:

`lmms --config {{path/to/config.xml}}`

- Porniți GUI și importați fișierul MIDI sau hidrogen:

`lmms --import {{path/to/midi/or/hydrogen/file}}`

- Porniți GUI cu o dimensiune specificată a ferestrei:

`lmms --geometry {{x_size}}x{{y_size}}+{{x_offset}}+{{y_offset}}`

- Dump un fișier `.mmpz `:

`lmms dump {{path/to/mmpz/file.mmpz}}`

- Randarea unui fișier de proiect:

`lmms render {{path/to/mmpz_or_mmp/file}}`

- Randați piesele individuale ale unui fișier de proiect:

`lmms rendertracks {{path/to/mmpz_or_mmp/file}} {{path/to/dump/directory}}`

- Randare cu samplerat personalizat, format, și ca o buclă:

`lmms render --samplerate {{88200}} --format {{ogg}} --loop --output {{path/to/output/file.ogg}}`
