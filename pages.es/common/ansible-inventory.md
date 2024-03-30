# ansible-inventory

> Muestra o vuelca un inventario de Ansible.
> Vea también: `ansible`.
> Más información: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Muestra el inventario por defecto:

`ansible-inventory --list`

- Muestra un inventario personalizado:

`ansible-inventory --list --inventory {{ruta/al/archivo_o_script_o_directorio}}`

- Muestra el inventario por defecto en YAML:

`ansible-inventory --list --yaml`

- Vuelca el inventario por defecto a un fichero:

`ansible-inventory --list --output {{ruta/al/archivo}}`
