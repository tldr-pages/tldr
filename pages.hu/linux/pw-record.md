# pw-record

> A pw-cat --playback rövidítése. További információ: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Az összes elérhető rekordcélpont listázása:

`pw-record --list-targets`

- Mintafelvétel rögzítése az alapértelmezett célpont használatával:

`pw-record {{path/to/file.wav}}`

- Mintafelvétel rögzítése más hangerővel:

`pw-record --volume={{0.1}} {{path/to/file.wav}}`

- Mintafelvétel rögzítése más mintavételi frekvenciával:

`pw-record --rate={{6000}} {{path/to/file.wav}}`
