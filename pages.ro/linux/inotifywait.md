# inotifywait

> Așteaptă modificările la unul sau mai multe fișiere.

- Rulați o comandă atunci când un fișier se schimbă:

`while inotifywait {{path/to/file}}; do {{command}}; done`

- Fii liniștit despre vizionarea schimbărilor:

`while inotifywait --quiet {{path/to/file}}; do {{command}}; done`

- Urmăriți un director recursiv pentru modificări:

`while inotifywait --recursive {{path/to/directory}}; do {{command}}; done`

- Excludeți fișierele care se potrivesc unei expresii regulate:

`while inotifywait --recursive {{path/to/directory}} --exclude '{{regular_expression}}'; do {{command}}; done`

- Așteptați cel mult 30 de secunde:

`while inotifywait --timeout {{30}} {{path/to/file}}; do {{command}}; done`

- Urmăriți numai evenimentele de modificare a fișierelor:

`while inotifywait --event {{modify}} {{path/to/file}}; do {{command}}; done`
