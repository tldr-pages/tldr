# genie

> A WSL (Windows Subsystem for Linux) alatt a systemd futtatásához egy "palack" névtér beállítása és használata. Ha ezeket Windowsról szeretné futtatni egy már futó disztribúció helyett, akkor a `wsl` előzze meg őket. További információ: <https://github.com/arkane-systems/genie>.

- A palack inicializálása (egyszer futtatjuk, indításkor):

`genie -i`

- Futtasson egy bejelentkezési héjat a palackon belül:

`genie -s`

- Egy megadott parancs futtatása a palackon belül:

`genie -c {{command}}`
