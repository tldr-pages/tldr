# chmod

> Verander de toegangstoestemmingen van een bestand of map.
> Meer informatie: <https://www.gnu.org/software/coreutils/chmod>.

- Geef een gebruiker ([u]ser) die het bestand beheert het recht om deze uit te voeren (e[x]ecute):

`chmod u+x {{bestand}}`

- Geef de gebruiker ([u]ser) het recht om een bestand of map te lezen ([r]ead) en schrijven ([w]rite):

`chmod u+rw {{bestand_of_map}}`

- Haal uitvoertoestemming (e[x]ecute) voor een bestand weg van de [g]roep:

`chmod g-x {{bestand}}`

- Geef [a]lle gebruikers toegang om een bestand te lezen ([r]ead) en schrijven ([w]rite):

`chmod a+rx {{bestand}}`

- Geef anderen ([o]thers) die niet in de groep van de beheerder zitten, dezelfde rechten als de [g]roep:

`chmod o=g {{bestand}}`

- Haal alle rechten van de anderen ([o]thers) weg:

`chmod o= {{bestand}}`

- Verander de toestemmingen recursief, waarbij de [g]roep en anderen ([o]thers) de mogelijkheid tot schrijven ([w]rite) krijgen:

`chmod -R g+w,o+w {{map}}`
