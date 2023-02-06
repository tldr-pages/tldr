# toolbox run

> Egy parancs futtatása egy meglévő `toolbox` konténerben. Lásd még: `toolbox enter`. További információ: <https://manned.org/toolbox-run>.

- Parancs futtatása egy adott `toolbox` konténeren belül:

`toolbox run --container {{container_name}} {{command}}`

- Parancs futtatása a `toolbox` konténeren belül egy adott disztribúció adott kiadásához:

`toolbox run --distro {{distribution}} --release {{release}} {{command}}`

- A `emacs` futtatása egy `toolbox` konténeren belül a Fedora 36 alapértelmezett képét használva:

`toolbox run --distro {{fedora}} --release {{f36}} {{emacs}}`
