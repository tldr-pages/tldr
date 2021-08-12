# gitk

> Un browser grafic de depozit Git.
> Mai multe informaţii: <https://git-scm.com/docs/gitk>

- Afișați browserul de depozit pentru depozitul Git curent:

`gitk`

- Arată browser-ul de depozit pentru un anumit fișier sau director:

`gitk {{path/to/file_or_directory}}`

- Arată angajările făcute începând cu 1 săptămână în urmă:

`gitk --since="{{1 week ago}}"`

- Arată angajările mai vechi de 1/1/2016:

`gitk --until="{{1/1/2015}}"`

- Arată cel mult 100 de modificări în toate ramurile:

` gitk --max-count={{100}} --all`
