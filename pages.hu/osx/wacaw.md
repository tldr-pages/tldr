# wacaw

> A macOS parancssori eszköze állóképek és videók rögzítésére egy csatlakoztatott kameráról. További információ: <http://webcam-tools.sourceforge.net>.

- Kép készítése webkameráról:

`wacaw {{filename}}`

- Videó felvétele:

`wacaw --video {{filename}} --duration {{duration_in_seconds}}`

- Készítsen képet egyéni felbontással:

`wacaw --width {{width}} --height {{height}} {{filename}}`

- Az imént készített kép másolása a vágólapra:

`wacaw --to-clipboard`

- A rendelkezésre álló eszközök listázása:

`wacaw --list-devices`
