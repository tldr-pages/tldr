# ansible

> Verwalten von Computergruppen per Fernzugriff über SSH.
> Verwenden Sie die Datei `/etc/ansible/hosts`, um neue Gruppen/Hosts hinzuzufügen.
> Weitere Informationen: <https://www.ansible.com/>.

- Hosts auflisten, die zu einer Gruppe gehören:

`ansible {{Gruppe}} --list-hosts`

- Pingen Sie eine Gruppe von Hosts an, indem Sie das Ping-Modul aufrufen:

`mögliche {{Gruppe}} -m ping`

- Zeigen Sie Fakten über eine Gruppe von Hosts an, indem Sie das Setup-Modul aufrufen:

`mögliche {{Gruppe}} -m setup`

- Führen Sie einen Befehl auf einer Gruppe von Hosts aus, indem Sie das Command-Modul mit Argumenten aufrufen:

`mögliche {{Gruppe}} -m command -a '{{mein_command}}'`

- Führen Sie einen Befehl mit administrativen Privilegien aus:

`möglich {{Gruppe}} --become --ask-become-pass -m command -a '{{mein_command}}'`

- Führen Sie einen Befehl mit einer benutzerdefinierten Inventardatei aus:

`möglich {{Gruppe}} -i {{Inventardatei}} -m command -a '{{mein_command}}'`
