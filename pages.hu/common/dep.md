# dep

> CLI eszköz PHP alkalmazások telepítéséhez. Megjegyzés: Az azonos nevű `dep` Go parancs elavult és archivált. További információ: <https://deployer.org>.

- Interaktívan inicializálja a deployert a helyi elérési útvonalon (használjon keretrendszer-sablont a `--template={{template}}`):

`dep init`

- Alkalmazás telepítése egy távoli állomáson:

`dep deploy {{hostname}}`

- Visszaállítás az előző működő kiadásra:

`dep rollback`

- Csatlakozás egy távoli állomáshoz ssh-n keresztül:

`dep ssh {{hostname}}`

- Parancsok listázása:

`dep list`

- Bármilyen tetszőleges parancs futtatása a távoli állomáson:

`dep run "{{command}}"`

- Súgó megjelenítése egy parancshoz:

`dep help {{command}}`
