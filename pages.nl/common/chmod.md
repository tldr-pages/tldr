# chmod

> Verander de toegangstoestemmingen van een bestand of map.
> Meer informatie: <https://www.gnu.org/software/coreutils/chmod>.

- Geef een gebruiker ([u]ser) die het bestand beheert het recht om deze uit te voeren (e[x]ecute):

`chmod u+x {{pad/naar/bestand}}`

- Geef de gebruiker ([u]ser) het recht om een bestand of map te lezen ([r]ead) en schrijven ([w]rite):

`chmod u+rw {{pad/naar/bestand_of_map}}`

- Haal uitvoertoestemming (e[x]ecute) voor een bestand weg van de [g]roep:

`chmod g-x {{pad/naar/bestand}}`

- Geef [a]lle gebruikers toegang om een bestand te lezen ([r]ead) en schrijven ([w]rite):

`chmod a+rx {{pad/naar/bestand}}`

- Geef anderen ([o]thers) die niet in de groep van de beheerder zitten, dezelfde rechten als de [g]roep:

`chmod o=g {{pad/naar/bestand}}`

- Haal alle rechten van de anderen ([o]thers) weg:

`chmod o= {{pad/naar/bestand}}`

- Verander de toestemmingen recursief, waarbij de [g]roep en anderen ([o]thers) de mogelijkheid tot schrijven ([w]rite) krijgen:

`chmod -R g+w,o+w {{map}}`

- Geef recursief alle gebruikers ([a]ll users) toegang om bestanden te lezen ([r]ead) en uitvoertoestemming (e[X]ecute) voor alle onderliggende mappen in een map:

`chmod -R a+rX {{pad/naar/map}}`
