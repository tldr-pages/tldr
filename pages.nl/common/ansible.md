# ansible

> Beheer een groep van computers op afstand over SSH. (Gebruik het `/etc/ansible/hosts` bestand om nieuwe groepen/hosts toe te voegen).
> Sommige subcommando's zoals `ansible galaxy` hebben hun eigen documentatie.
> Meer informatie: <https://www.ansible.com/>.

- Toon de hosts die tot een groep behoren:

`ansible {{groep}} --list-hosts`

- Ping een groep met hosts, met gebruik van de ping module:

`ansible {{groep}} -m ping`

- Toon feiten van een groep met hosts, met gebruik van de installatie module:

`ansible {{groep}} -m setup`

- Voer een commando op een groep met hosts uit. met gebruik van de commando module met argumenten:

`ansible {{groep}} -m command -a '{{mijn_commando}}'`

- Voer een commando uit met administratieve rechten:

`ansible {{groep}} --become --ask-become-pass -m command -a '{{mijn_commando}}'`

- Voer een commando uit met een aangepast inventaris bestand:

`ansible {{groep}} -i {{inventaris_bestand}} -m command -a '{{mijn_command}}'`

- Toon de groepen in een inventaris:

`ansible localhost -m debug -a '{{var=groups.keys()}}'`
