# dockerd

> Un proces persistent pentru pornirea și gestionarea containerelor de andocare.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/dockerd/>

- Rulați demonul docker:

`dockerd`

- Rulați docker daemon și configurați-l pentru a asculta anumite prize (unix, tcp):

`dockerd --host unix://{{path/to/tmp.sock}} --host tcp://{{ip}}`

- Rulați cu fișierul PID daemon specific:

`dockerd --pidfile {{path/to/pid_file}}`

- Rulați în modul de depanare:

`dockerd --debug`

- Rulați și setați un anumit nivel de jurnal:

`dockerd --log-level={{debug|info|warn|error|fatal}}`
