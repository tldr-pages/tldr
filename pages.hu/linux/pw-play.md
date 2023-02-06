# pw-play

> A pw-cat --playback rövidítése. További információ: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Az összes elérhető lejátszási célpont listázása:

`pw-play --list-targets`

- Egy wav hangfájl lejátszása az alapértelmezett célponton keresztül:

`pw-play {{path/to/file.wav}}`

- Egy wav hangfájl lejátszása más hangerővel:

`pw-play --volume={{0.1}} {{path/to/file.wav}}`
