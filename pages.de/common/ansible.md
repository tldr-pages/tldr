# ansible

> Verwalte Computergruppen per Fernzugriff über SSH (Verwende die Datei `/etc/ansible/hosts`, um neue Gruppen/Hosts hinzuzufügen).
> Manche Unterbefehle wie `galaxy` sind separat dokumentiert.
> Weitere Informationen: <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- Liste Hosts auf, die zu einer Gruppe gehören:

`ansible {{gruppe}} --list-hosts`

- Pinge eine Gruppe von Hosts an:

`ansible {{gruppe}} {{[-m|--module-name]}} ping`

- Zeige Informationen über eine Gruppe von Hosts an:

`ansible {{gruppe}} {{[-m|--module-name]}} setup`

- Führe einen Befehl auf einer Gruppe von Hosts aus:

`ansible {{gruppe}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{befehl}}'`

- Führe einen Befehl mit administrativen Privilegien aus:

`ansible {{gruppe}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{befehl}}'`

- Führe einen Befehl mit einer benutzerdefinierten Inventardatei aus:

`ansible {{Gruppe}} {{[-i|--inventory]}} {{inventardatei}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{befehl}}'`

- Liste alle Gruppen eines Inventars auf:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
