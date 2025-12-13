# ansible-inventory

> Visualizza o scarica un inventario Ansible.
> Vedi anche: `ansible`.
> Maggiori informazioni: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Visualizza l'inventario predefinito:

`ansible-inventory --list`

- Visualizza un inventario personalizzato:

`ansible-inventory --list {{[-i|--inventory-file]}} {{percorso/del/file_o_script_o_directory}}`

- Visualizza l'inventario predefinito in YAML:

`ansible-inventory --list {{[-y|--yaml]}}`

- Scarica l'inventario predefinito in un file:

`ansible-inventory --list --output {{percorso/del/file}}`
