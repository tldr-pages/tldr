# share

> Maak lokale bron/bestandssysteem beschikbaar voor mounten door systemen op afstand.
> Meer informatie: <https://docs.oracle.com/cd/E36784_01/html/E36825/gntjt.html>.

- Toon alle momenteel gedeelde bestandssystemen:

`share`

- Deel een map met lees/schrijftoegang:

`share -F nfs -o rw /{{pad/naar/map}}`

- Deel een map met alleen-lezen toegang:

`share -F nfs -o ro /{{pad/naar/map}}`

- Deel een map met specifieke opties (bijvoorbeeld root-toegang toestaan vanaf een bepaalde host):

`share -F nfs -o rw,root={{hostnaam}} /{{pad/naar/map}}`

- Maak delen persistent door entries toe te voegen aan `/etc/dfs/dfstab`:

`echo "share -F nfs -o rw /{{pad/naar/map}}" >> /etc/dfs/dfstab`
