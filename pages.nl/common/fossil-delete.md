# fossil delete

> Verwijder bestanden of mappen uit Fossil-versiebeheer.
> Zie ook: `fossil forget`.
> Meer informatie: <https://fossil-scm.org/home/help/delete>.

- Verwijder een bestand of map uit Fossil-versiebeheer:

`fossil {{[rm|delete]}} {{pad/naar/bestand_of_map}}`

- Verwijder een bestand of map uit Fossil-versiebeheer en ook van de schijf:

`fossil {{[rm|delete]}} --hard {{pad/naar/bestand_of_map}}`

- Voeg alle eerder verwijderde en niet-vastgelegde bestanden opnieuw toe aan Fossil-versiebeheer:

`fossil {{[rm|delete]}} --reset`
