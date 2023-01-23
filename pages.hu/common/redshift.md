# redshift

> Állítsa be a képernyő színhőmérsékletét a környezetének megfelelően. További információ: <http://jonls.dk/redshift>.

- Kapcsolja be a Redshiftet nappal 5700K színhőmérséklettel, éjszaka pedig 3600K színhőmérséklettel:

`redshift -t {{5700}}:{{3600}}`

- Kapcsolja be a Redshiftet egy kézzel megadott egyéni helyzettel:

`redshift -l {{latitude}}:{{longitude}}`

- Kapcsolja be a Redshiftet 70%-os képernyőfényerősséggel nappal és 40%-os fényerővel éjszaka:

`redshift -b {{0.7}}:{{0.4}}`

- Redshift bekapcsolása egyéni gamma-szintekkel (0 és 1 között):

`redshift -g {{red}}:{{green}}:{{blue}}`

- A Redshift bekapcsolása állandó, változatlan színhőmérséklettel:

`redshift -O {{temperature}}`
