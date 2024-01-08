# ansible-inventory

> Anzeigen oder Ausgeben eines Ansible-Inventars.
> Siehe auch: `ansible`.
> Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Anzeigen des Standardinventars:

`ansible-inventory --list`

- Anzeigen eines Benutzerdefinierten Inventars:

`ansible-inventory --list --inventory {{pfad/zu/datei_oder_skript_oder_verzeichnis}}`

- Anzeigen des Standardinventars in YAML:

`ansible-inventory --list --yaml`

- Ausgabe des Standardinventars in eine Datei:

`ansible-inventory --list --output {{pfad/zu/datei}}`
