# neato

> Randați o imagine a unui grafic de rețea „liniar nedirecționat” dintr-un fișier „grafic”.
> Aspecte: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
> Mai multe informaţii: <https://graphviz.org/doc/info/command.html>

- Randați o imagine `png` cu un nume de fișier bazat pe numele fișierului de intrare și formatul de ieșire (majuscule -O):

`neato -T {{png}} -O {{path/to/input.gv}}`

- Randați o imagine `svg` cu numele fișierului de ieșire specificat (minuscule -o):

`neato -T {{svg}} -o {{path/to/image.svg}} {{path/to/input.gv}}`

- Randați ieșirea în format `ps`, `pdf`, `svg`, `fig`, `png`, `gif`, `jpg`, `json` sau `dot`:

`neato -T {{format}} -O {{path/to/input.gv}}`

- Randați o imagine `gif` folosind stdin și stdout:

`echo "{{graph {this -- that} }}" | neato -T {{gif}} > {{path/to/image.gif}}`

- Ajutor pentru afișare:

`neato -?`
