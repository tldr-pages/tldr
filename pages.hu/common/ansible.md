# ansible

> Számítógépcsoportok távoli kezelése SSH-n keresztül. (új csoportok/hostok hozzáadásához használja a `/etc/ansible/hosts` fájlt). Néhány alparancsnak, például a `ansible galaxy` parancsnak saját használati dokumentációja van. További információ: <https://www.ansible.com/>.

- Egy csoporthoz tartozó hosztok listázása:

`ansible {{group}} --list-hosts`

- Pingeljen meg egy állomáscsoportot a ping modul meghívásával:

`ansible {{group}} -m ping`

- Tények megjelenítése egy állomáscsoportról a setup modul meghívásával:

`ansible {{group}} -m setup`

- Parancs végrehajtása egy állomáscsoporton a command modul argumentumokkal történő meghívásával:

`ansible {{group}} -m command -a '{{my_command}}'`

- Parancs végrehajtása rendszergazdai jogosultságokkal:

`ansible {{group}} --become --ask-become-pass -m command -a '{{my_command}}'`

- Parancs végrehajtása egyéni leltárfájl használatával:

`ansible {{group}} -i {{inventory_file}} -m command -a '{{my_command}}'`

- A leltárban szereplő csoportok listázása:

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
