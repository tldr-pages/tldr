# lp

> Print bestanden.
> Zie ook: `lpstat`, `lpoptions`.
> Meer informatie: <https://manned.org/lp>.

- Print de output van een commando naar de standaard printer (bekijk het `lpstat` commando):

`echo "test" | lp`

- Print een bestand naar de standaard printer:

`lp {{pad/naar/bestand}}`

- Print een bestand naar een printer met naam (bekijk het `lpstat` commando):

`lp -d {{printer_naam}} {{pad/naar/bestand}}`

- Print n kopieën van een bestand naar de standaard printer:

`lp -n {{n}} {{pad/naar/bestand}}`

- Print alleen specifieke pagina's naar de standaard printer (print pagina's 1, 3-5 en 16):

`lp -P 1,3-5,16 {{pad/naar/bestand}}`

- Hervat het printen van een taak:

`lp -i {{taak_id}} -H resume`
