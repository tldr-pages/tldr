# ansible-playbook

> In Playbook definierte Aufgaben auf entfernten Rechnern über SSH ausführen.
> Mehr Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Ausführen von Aufgaben im Playbook:

`ansible-playbook {{playbook}}`

- Führen Sie Aufgaben im Playbook mit benutzerdefiniertem Host-Bestand aus:

`ansible-playbook {{playbook}} -i {{inventory_file}}`

- Führen Sie Aufgaben im Playbook aus, wobei zusätzliche Variablen über die Befehlszeile definiert werden:

`ansible-playbook {{playbook}} -e "{{Variable1}}={{Wert1}} {{Variable2}}={{Wert2}}"`

- Führen Sie Aufgaben in Playbook mit zusätzlichen Variablen aus, die in einer Json-Datei definiert sind:

`ansible-playbook {{playbook}} -e "@{{variables.json}}"`

- Führen Sie Aufgaben im Playbook für die angegebenen Tags aus:

`ansible-playbook {{playbook}} --tags {tags {tags}}`

- Führen Sie Aufgaben in einem Playbook aus, die mit einer bestimmten Aufgabe beginnen:

`ansible-playbook {{playbook}} --start-at {{task_name}}`
