# chpass

> Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
> Bekijk ook: `passwd`.
> Meer informatie: <https://man.openbsd.org/chsh>.

- Stel interactief een specifieke login shell in voor de huidige gebruiker:

`doas chsh`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`doas chsh -s {{pad/naar/shell}}`

- Stel een login [s]hell in voor een specifieke gebruiker:

`doas chsh -s {{pad/naar/shell}} {{gebruikersnaam}}`

- Specificeer een gebruikersdatabase entry in het `passwd` bestandsformaat:

`doas chsh -a {{gebruikersnaam:gecodeerd_wachtwoord:uid:gid:...}}`
