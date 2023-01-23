# scp

> Biztonságos másolás. Fájlok másolása állomáshely között a Secure Copy Protocol használatával SSH-n keresztül. További információ: <https://man.openbsd.org/scp>.

- Helyi fájl másolása egy távoli gépre:

`scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Egy adott port használata a távoli állomáshoz való csatlakozáskor:

`scp -P {{port}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Fájl másolása egy távoli állomásról egy helyi könyvtárba:

`scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Egy könyvtár tartalmának rekurzív másolása egy távoli állomásról egy helyi könyvtárba:

`scp -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Fájl másolása két távoli állomás között, a helyi állomáson keresztül történő átvitel:

`scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_directory}}`

- Egy adott felhasználónév használata a távoli állomáshoz való csatlakozáskor:

`scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_directory}}`

- Egy adott ssh privát kulcs használata a távoli állomáson történő hitelesítéshez:

`scp -i {{~/.ssh/private_key}} {{local_file}} {{remote_host}}:{{/path/remote_file}}`
