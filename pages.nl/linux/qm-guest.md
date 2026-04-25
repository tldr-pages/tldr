# qm guest

> Beheer een VM gast agent.
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_guest_cmd>.

- Toon de status van een specifieke PID:

`qm {{[g|guest]}} {{[exec-s|exec-status]}} {{100}} {{pid}}`

- Stel interactief een wachtwoord in voor een specifieke gebruiker in een virtuele machine:

`qm {{[g|guest]}} {{[p|passwd]}} {{100}} {{gebruikersnaam}}`

- Stel interactief een reeds gehasht wachtwoord in voor een specifieke gebruiker in een virtuele machine:

`qm {{[g|guest]}} {{[p|passwd]}} {{100}} {{gebruikersnaam}} --crypted 1`

- Voer een specifiek QEMU Guest Agent-commando uit:

`qm {{[g|guest]}} {{[c|cmd]}} {{100}} {{fsfreeze-freeze|fsfreeze-status|fsfreeze-thaw|fstrim|get-fsinfo|...}}`

- Voer een specifiek commando uit via een guest agent:

`qm {{[g|guest]}} exec {{100}} {{commando}} {{argument1 argument2 ...}}`

- Voer een specifiek commando asynchroon uit via een guest agent:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2 ...}} --synchronous 0`

- Voer een specifieke opdracht uit via een gast agent met een opgegeven time-out van 10 seconden:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2...}} --timeout {{10}}`

- Voer een specifieke opdracht uit via een gast agent en stuur invoer van `stdin` tot EOF door naar de gast agent:

`qm {{[g|guest]}} exec {{100}} {{argument1 argument2 ...}} --pass-stdin 1`
