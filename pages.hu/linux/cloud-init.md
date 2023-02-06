# cloud-init

> Parancssori eszköz a felhőpéldányok inicializálásának kezelésére. További információ: <https://cloudinit.readthedocs.io>.

- A legutóbbi cloud-init futtatás állapotának megjelenítése:

`cloud-init status`

- Várja meg a cloud-init futásának befejezését, majd jelentse az állapotot:

`cloud-init status --wait`

- Lista a lekérdezhető felső szintű metaadatkulcsokról:

`cloud-init query --list-keys`

- A gyorsítótárazott példány metaadatok lekérdezése adatokért:

`cloud-init query {{dot_delimited_variable_path}}`

- Naplók és leletek megtisztítása a cloud-init újbóli futtatásához:

`cloud-init clean`
