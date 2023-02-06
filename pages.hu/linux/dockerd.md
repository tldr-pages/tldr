# dockerd

> Állandó folyamat a docker konténerek indításához és kezeléséhez. További információ: <https://docs.docker.com/engine/reference/commandline/dockerd/>.

- A docker démon futtatása:

`dockerd`

- A docker daemon futtatása és konfigurálása, hogy bizonyos foglalatokat (UNIX és TCP) figyeljen:

`dockerd --host unix://{{path/to/tmp.sock}} --host tcp://{{ip}}`

- Futtatás meghatározott démon PID fájljával:

`dockerd --pidfile {{path/to/pid_file}}`

- Futtatás hibakeresési módban:

`dockerd --debug`

- Futtatás és meghatározott naplózási szint beállítása:

`dockerd --log-level={{debug|info|warn|error|fatal}}`
