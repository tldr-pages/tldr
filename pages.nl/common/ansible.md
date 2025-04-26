# ansible

> Beheer een groep van computers op afstand over SSH. (Gebruik het `/etc/ansible/hosts` bestand om nieuwe groepen/hosts toe te voegen).
> Sommige subcommando's zoals `galaxy` hebben hun eigen documentatie.
> Meer informatie: <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- Toon de hosts die tot een groep behoren:

`ansible {{groep}} --list-hosts`

- Ping een groep met hosts, met gebruik van de ping module:

`ansible {{groep}} {{[-m|--module-name]}} ping`

- Toon feiten van een groep met hosts, met gebruik van de installatie module:

`ansible {{groep}} {{[-m|--module-name]}} setup`

- Voer een commando op een groep met hosts uit. met gebruik van de commando module met argumenten:

`ansible {{groep}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{mijn_commando}}'`

- Voer een commando uit met administratieve rechten:

`ansible {{groep}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{mijn_commando}}'`

- Voer een commando uit met een aangepast inventaris bestand:

`ansible {{groep}} {{[-i|--inventory]}} {{inventaris_bestand}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{mijn_commando}}'`

- Toon de groepen in een inventaris:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
