# chpass

> Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
> Bekijk ook: `passwd`.
> Meer informatie: <https://man.openbsd.org/chsh>.

- Stel interactief een specifieke login shell in voor de huidige gebruiker:

`su -c chpass`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`chpass -s {{pad/naar/shell}}`

- Stel een login [s]hell in voor een specifieke gebruiker:

`chpass chsh -s {{pad/naar/shell}} {{gebruikersnaam}}`

- Specificeer een gebruikersdatabase entry in het `passwd` bestandsformaat:

`su -c 'chpass -a {{gebruikersnaam:gecodeerd_wachtwoord:uid:gid:...}} -s {{pad/naar/bestand}}' {{gebruikersnaam}}`

- Pas alleen het lokale wachtwoord bestand aan:

`su -c 'chpass -l -s {{pad/naar/shell}}' {{gebruikersnaam}}`

- Pas geforceerd een database [y]P wachtwoord database entry aan:

`su -c 'chpass -y -s {{pad/naar/shell}}' {{gebruikersnaam}}`
