# ansible-inventory

> Az Ansible-leltár megjelenítése vagy kiürítése. Lásd még: `ansible`. További információ: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Az alapértelmezett leltár megjelenítése:

`ansible-inventory --list`

- Egyéni leltár megjelenítése:

`ansbile-inventory --list --inventory {{path/to/file_or_script_or_directory}}`

- Az alapértelmezett leltár megjelenítése YAML-ben:

`ansible-inventory --list --yaml`

- Az alapértelmezett leltár dumpolása egy fájlba:

`ansible-inventory --list --output {{path/to/file}}`
