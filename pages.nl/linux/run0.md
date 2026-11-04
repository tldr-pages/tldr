# run0

> Verhoog rechten interactief.
> Vergelijkbaar met `sudo`, maar het is geen SUID-binary, authenticatie verloopt via polkit, en commando's worden aangeroepen vanuit een `systemd`-service.
> Zie ook: `sudo`, `pkexec`, `doas`.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/latest/run0.html>.

- Voer een commando uit als root:

`run0 {{commando}}`

- Voer een commando uit als een andere gebruiker en/of groep:

`run0 {{[-u|--user]}} {{gebruikersnaam|gebruikers_id}} {{[-g|--group]}} {{groepsnaam|groeps_id}} {{commando}}`
