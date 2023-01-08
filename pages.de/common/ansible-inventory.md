# ansible-inventory

> Anzeigen oder Ausgeben eines Ansible-Inventars.
> Siehe auch: `ansible`.
> Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Anzeigen des Standardinventars:

`ansible-inventory --list`

- Anzeigen eines Benutzerdefinierten Inventars:

`ansbile-inventory --list --inventory {{pfad/zu/deiner_datei_oder_deinem_script_oder_deinem_verzeichniss}}`

- Anzeigen des Standardinventars in YAML:

`ansible-inventory --list --yaml`

- Ausgabe des Standardinventars in eine Datei:

`ansible-inventory --list --output {{pfad/zu/datei}}`
