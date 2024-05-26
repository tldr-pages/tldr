# ansible

> Gestiona grupos de ordenadores de forma remota a través de SSH. (usa el fichero `/etc/ansible/hosts` para añadir nuevos grupos de hosts).
> Algunos subcomandos como `ansible galaxy` tienen su propia documentación.
> Más información: <https://www.ansible.com/>.

- Lista los hosts pertenecientes a un grupo:

`ansible {{grupo}} --list-hosts`

- Hace ping a un grupo de hosts invocando al módulo ping:

`ansible {{grupo}} -m ping`

- Muestra información sobre un grupo de hosts invocando al módulo setup:

`ansible {{grupo}} -m setup`

- Ejecuta un comando en un grupo de hosts invocando el módulo de command con argumentos:

`ansible {{grupo}} -m command -a '{{mi_comando}}'`

- Ejecuta un comando con privilegios administrativos:

`ansible {{grupo}} --become --ask-become-pass -m command -a '{{mi_comando}}'`

- Ejecuta un comando utilizando un archivo de inventario personalizado:

`ansible {{grupo}} -i {{archivo_de_inventario}} -m command -a '{{mi_comando}}'`

- Lista los grupos de un inventario:

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
