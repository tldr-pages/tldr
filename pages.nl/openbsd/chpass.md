# chpass

> Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
> Zie ook: `passwd`.
> Meer informatie: <https://man.openbsd.org/chpass>.

- Stel interactief een specifieke login shell in voor de huidige gebruiker:

`doas chpass`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`doas chpass -s {{pad/naar/shell}}`

- Stel een login [s]hell in voor een specifieke gebruiker:

`doas chpass -s {{pad/naar/shell}} {{gebruikersnaam}}`

- Specificeer een gebruikersdatabase entry in het `passwd` bestandsformaat:

`doas chpass -a {{gebruikersnaam:gecodeerd_wachtwoord:uid:gid:...}}`
