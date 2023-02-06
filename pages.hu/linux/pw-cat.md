# pw-cat

> Pipewire eszköz hangfájlok lejátszásához és rögzítéséhez. További információ: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Az összes elérhető lejátszási célpont listája:

`pw-cat --playback --list-targets`

- WAV-fájl lejátszása az alapértelmezett célponton keresztül:

`pw-cat --playback {{path/to/file.wav}}`

- Az összes elérhető felvételi célpont listázása:

`pw-cat --record --list-targets`

- Mintafelvétel rögzítése más hangerővel:

`pw-cat --record --volume={{0.1}} {{path/to/file.wav}}`

- Mintafelvétel felvétele más mintavételi frekvenciával:

`pw-cat --record --rate={{6000}} {{path/to/file.wav}}`
