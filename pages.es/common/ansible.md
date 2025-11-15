# ansible

> Gestiona grupos de ordenadores remotamente sobre SSH. (usa el archivo `/etc/ansible/hosts` para añadir nuevos grupos/hosts).
> Algunos subcomandos como `galaxy` tienen su propia documentación de uso.
> Más información: <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- Lista de hosts pertenecientes a un grupo:

`ansible {{grupo}} --list-hosts`

- Hace ping a un grupo de hosts invocando al módulo ping:

`ansible {{grupo}} {{[-m|--module-name]}} ping`

- Muestra información sobre un grupo de hosts invocando al módulo setup:

`ansible {{grupo}} {{[-m|--module-name]}} setup`

- Ejecuta un comando en un grupo de hosts invocando el módulo command con argumentos:

`ansible {{grupo}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{mi_comando}}'`

- Ejecuta un comando con privilegios administrativos:

`ansible {{grupo}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{mi_comando}}'`

- Ejecuta un comando utilizando un archivo de inventario personalizado:

`ansible {{grupo}} {{[-i|--inventory]}} {{archivo_de_inventario}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{mi_comando}}'`

- Lista los grupos de un inventario:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
