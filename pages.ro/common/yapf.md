# yapf

> Python ghid stil de verificare.
> Mai multe informaţii: <https://github.com/google/yapf>

- Afișați o diff a modificărilor care ar fi făcute, fără a le face (uscat-run):

`yapf --diff {{path/to/file}}`

- Formatați fișierul în loc și afișați o diff a modificărilor:

`yapf --diff --in-place {{path/to/file}}`

- Formatați recursiv toate fișierele Python într-un director, simultan:

`yapf --recursive --in-place --style {{pep8}} --parallel {{path/to/directory}}`
