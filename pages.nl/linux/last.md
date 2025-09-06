# last

> Toon de laatst ingelogde gebruikers.
> Meer informatie: <https://manned.org/last>.

- Bekijk de laatste inloggegevens (bijv. gebruikersnaam, terminal, opstarttijd, kernel) van alle gebruikers zoals gelezen uit `/var/log/wtmp`:

`last`

- Toon login informatie van een specifieke gebruiker:

`last {{gebruikersnaam}}`

- Specificeer hoeveel van de laatste aanmeldingen weergegeven moeten worden:

`last {{[-n|--limit]}} {{login_count}}`

- Toon de volledige datum en tijd voor vermeldingen en toon vervolgens de kolom met de hostnaam als laatste weer om afkapping te voorkomen:

`last {{[-F|--fulltimes]}} {{[-a|--hostlast]}}`

- Toon alle aanmeldingen van een specifieke gebruiker en toon het IP-adres in plaats van de hostnaam:

`last {{gebruikersnaam}} {{[-i|--ip]}}`

- Toon informatie vanaf een specifieke datum en tijd:

`last {{[-s|--since]}} {{-7days}}`

- Bekijk alle geregistreerde herstarts (d.w.z. de laatste aanmeldingen van de pseudo-gebruiker “reboot”):

`last reboot`

- Toon de help:

`last {{[-h|--help]}}`
