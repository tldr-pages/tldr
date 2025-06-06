# sudo

> Voert een commando uit als de superuser of een andere gebruiker.
> Meer informatie: <https://www.sudo.ws/sudo.html>.

- Voer een commando uit als de superuser:

`sudo {{less /var/log/syslog}}`

- Pas een bestand aan als superuser met jouw standaardeditor:

`sudo {{[-e|--edit]}} {{/etc/fstab}}`

- Voer een commando uit als een andere gebruiker en/of groep:

`sudo {{[-u|--user]}} {{gebruiker}} {{[-g|--group]}} {{groep}} {{id -a}}`

- Herhaal het laatste commando met `sudo` ervoor (alleen in Bash, Zsh, etc.):

`sudo !!`

- Start de standaard shell met superuserrechten en voer login-specifieke bestanden uit (`.profile`, `.bash_profile`, etc.):

`sudo {{[-i|--login]}}`

- Start de standaard shell met superuserrechten zonder de omgeving te veranderen:

`sudo {{[-s|--shell]}}`

- Start de standaard shell als de opgegeven gebruiker, laad de omgeving van de gebruiker en lees login-specifieke bestanden (`.profile`, `.bash_profile`, etc.):

`sudo {{[-i|--login]}} {{[-u|--user]}} {{gebruiker}}`

- Toon de toegestane (en verboden) commando's voor de aanroepende gebruiker:

`sudo {{[-ll|--list --list]}}`
