# multipass

> CLI az Ubuntu virtuális gépek kezelésére natív hipervizorok használatával. További információ: <https://multipass.run/>.

- Sorolja fel a példányok indításához használható aliasokat:

`multipass find`

- Új példány indítása, nevének beállítása és a cloud-init konfigurációs fájl használata:

`multipass launch -n {{instance_name}} --cloud-init {{configuration_file}}`

- Az összes létrehozott példány és néhány tulajdonságuk felsorolása:

`multipass list`

- Egy adott példány elindítása név alapján:

`multipass start {{instance_name}}`

- Egy példány tulajdonságainak megjelenítése:

`multipass info {{instance_name}}`

- Shell prompt megnyitása egy adott példányon név szerint:

`multipass shell {{instance_name}}`

- Egy példány törlése név szerint:

`multipass delete {{instance_name}}`

- Könyvtárat csatolni egy adott példányba:

`multipass mount {{path/to/local/directory}} {{instance_name}}:{{path/to/target/directory}}`
