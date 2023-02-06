# docker exec

> Parancs végrehajtása egy már futó Docker konténeren. További információ: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Interaktív shell munkamenet belépése egy már futó konténeren:

`docker exec --interactive --tty {{container_name}} {{/bin/bash}}`

- Egy parancs futtatása a háttérben (leválasztva) egy futó konténeren:

`docker exec --detach {{container_name}} {{command}}`

- Kiválasztja a munkakönyvtárat, amelyben egy adott parancsot végre kell hajtani:

`docker exec --interactive -tty --workdir {{path/to/directory}} {{container_name}} {{command}}`

- Parancs futtatása a háttérben egy már létező konténeren, de a `stdin` nyitva tartása:

`docker exec --interactive --detach {{container_name}} {{command}}`

- Környezeti változó beállítása egy futó Bash munkamenetben:

`docker exec --interactive --tty --env {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- Parancs futtatása egy adott felhasználóként:

`docker exec --user {{user}} {{container_name}} {{command}}`
