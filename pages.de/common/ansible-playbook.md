# ansible-playbook

> In Playbook definierte Aufgaben auf entfernten Rechnern über SSH ausführen.
> Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Führe Aufgaben im Playbook aus:

`ansible-playbook {{playbook}}`

- Führe Aufgaben im Playbook mit benutzerdefiniertem Host-Bestand aus:

`ansible-playbook {{playbook}} {{[-i|--inventory]}} {{inventory_datei}}`

- Führe Aufgaben im Playbook aus, wobei zusätzliche Variablen über die Befehlszeile definiert werden:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "{{variable1}}={{wert1}} {{variable2}}={{wert2}}"`

- Führe Aufgaben in Playbook mit zusätzlichen Variablen aus, die in einer JSON-Datei definiert sind:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "@{{variablen.json}}"`

- Führe Aufgaben im Playbook für die angegebenen Tags aus:

`ansible-playbook {{playbook}} {{[-t|--tags|]}} {{tag1,tag2}}`

- Führe Aufgaben in einem Playbook aus, die mit einer bestimmten Aufgabe beginnen:

`ansible-playbook {{playbook}} --start-at {{aufgabenname}}`
