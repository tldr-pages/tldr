# last

> Bekijk de laatst ingelogde gebruikers.
> Meer informatie: <https://manned.org/last>.

- Bekijk de laatste logins, hun duur en andere informatie uit `/var/log/wtmp`:

`last`

- Geef aan hoeveel van de laatste logins moeten worden weergegeven:

`last -n {{aantal_logins}}`

- Toon de volledige datum en tijd voor vermeldingen en toon vervolgens de hostnaam-kolom als laatste om afkapping te voorkomen:

`last -F -a`

- Bekijk alle logins van een specifieke gebruiker en toon het IP-adres in plaats van de hostnaam:

`last {{gebruikersnaam}} -i`

- Bekijk alle geregistreerde herstarts (d.w.z. de laatste logins van de pseudo-gebruiker "reboot"):

`last reboot`

- Bekijk alle geregistreerde uitschakelingen (d.w.z. de laatste logins van de pseudo-gebruiker "shutdown"):

`last shutdown`
