# krunvm

> CLI-alapú segédprogram MicroVM-ek létrehozásához OCI-képekből. További információ: <https://github.com/containers/krunvm>.

- MicroVM létrehozása a Fedora alapján:

`krunvm create {{docker.io/fedora}} --cpus {{number_of_vcpus}} --mem {{memory_in_megabytes}} --name "{{name}}"`

- Indítson el egy adott képet:

`krunvm start "{{image_name}}"`

- Képek listázása:

`krunvm list`

- Egy adott kép módosítása:

`krunvm changevm --cpus {{number_of_vcpus}} --mem {{memory_in_megabytes}} --name "{{new_vm_name}}" "{{current_vm_name}}"`

- Egy adott kép törlése:

`krunvm delete "{{image_name}}"`
