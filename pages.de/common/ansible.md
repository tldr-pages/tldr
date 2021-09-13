# ansible

> Verwalte Computergruppen per Fernzugriff über SSH (Verwende die Datei `/etc/ansible/hosts`, um neue Gruppen/Hosts hinzuzufügen).
> Manche Unterbefehle wie `ansible galaxy` sind separat dokumentiert.
> Weitere Informationen: <https://www.ansible.com/>.

- Liste Hosts auf, die zu einer Gruppe gehören:

`ansible {{gruppe}} --list-hosts`

- Pinge eine Gruppe von Hosts an:

`ansible {{gruppe}} -m ping`

- Zeige Informationen über eine Gruppe von Hosts an:

`ansible {{gruppe}} -m setup`

- Führe einen Befehl auf einer Gruppe von Hosts aus:

`ansible {{gruppe}} -m command -a '{{befehl}}'`

- Führe einen Befehl mit administrativen Privilegien aus:

`ansible {{gruppe}} --become --ask-become-pass -m command -a '{{befehl}}'`

- Führe einen Befehl mit einer benutzerdefinierten Inventardatei aus:

`ansible {{Gruppe}} -i {{inventardatei}} -m command -a '{{befehl}}'`

- Liste alle Gruppen eines Inventars auf:

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
