# bosh

> Parancssori eszköz a bosh director telepítéséhez és kezeléséhez. További információ: <https://bosh.io/docs/cli-v2/>.

- Helyi alias létrehozása a director számára:

`bosh alias-env {{environment_name}} -e {{ip_address|url}} --ca-cert {{ca_certificate}}`

- Környezetek listázása:

`bosh environments`

- Jelentkezzen be a directorba:

`bosh login -e {{environment}}`

- Telepítések listázása:

`bosh -e {{environment}} deployments`

- Környezetek virtuális gépeinek listázása:

`bosh -e {{environment}} vms -d {{deployment}}`

- Ssh virtuális gépre:

`bosh -e {{environment}} ssh {{virtual_machine}} -d {{deployment}}`

- Törzsejt feltöltése:

`bosh -e {{environment}} upload-stemcell {{stemcell_file|url}}`

- Jelenlegi felhő konfiguráció megjelenítése:

`bosh -e {{environment}} cloud-config`
