# chpass

> Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
> Zie ook: `passwd`.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?query=chpass>.

- Voeg toe of pas interactief de gebruikersdatabase informatie aan voor de huidige gebruiker:

`su -c chpass`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`chpass -s {{pad/naar/shell}}`

- Stel een login [s]hell in voor een specifieke gebruiker:

`chpass -s {{pad/naar/shell}} {{gebruikersnaam}}`

- Pas de account v[e]rloop tijd aan (in seconden vanaf de epoch, UTC):

`su -c 'chpass -e {{tijd}} {{gebruikersnaam}}'`

- Pas een gebruikerswachtwoord aan:

`su -c 'chpass -p {{gecodeerd_wachtwoord}} {{gebruikersnaam}}'`

- Specificeer een [h]ostnaam of adres van een NIS server:

`su -c 'chpass -h {{hostnaam}} {{gebruikersnaam}}'`

- Specificeer een specifiek NIS-[d]omein (standaard systeemdomeinnaam):

`su -c 'chpass -d {{domein}} {{gebruikersnaam}}'`
