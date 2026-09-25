# lpoptions

> Toon of stel printeropties en standaardinstellingen in.
> Zie ook: `lpadmin`, `lp`, `lpstat`.
> Meer informatie: <https://openprinting.github.io/cups/doc/man-lpoptions.html>.

- Stel de standaardprinter in:

`lpoptions -d {{printer}}/{{instantie}}`

- Toon printeropties van de standaardprinter:

`lpoptions -l`

- Toon de momenteel ingestelde opties van een specifieke printer:

`lpoptions -p {{printer}}`

- Toon welke opties het stuurprogramma blootstelt voor een printer:

`lpoptions -p {{printer}} -l`

- Stel een nieuwe optie in op de standaardprinter:

`lpoptions -o {{optie}}`

- Verwijder de opties van een specifieke printer:

`lpoptions -x {{printer}}`
