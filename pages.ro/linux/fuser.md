# fuser

> Afișați ID-uri de proces care utilizează în prezent fișiere sau prize.
> Mai multe informaţii: <https://manned.org/fuser>

- Găsiți ce procese accesează un fișier sau un director:

`fuser {{path/to/file_or_directory}}`

- Afișează mai multe câmpuri („USER', „PID”, „ACCESTE” și „COMANDĂ”):

`fuser --verbose {{path/to/file_or_directory}}`

- Identificarea proceselor folosind un soclu TCP:

`fuser --namespace tcp {{port}}`

- Omoară toate procesele care accesează un fișier sau un director (trimite semnalul `SIGKILL`):

`fuser --kill {{path/to/file_or_directory}}`

- Află ce procese accesează sistemul de fișiere care conține un anumit fișier sau director:

`fuser --mount {{path/to/file_or_directory}}`
