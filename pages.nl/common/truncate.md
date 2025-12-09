# truncate

> Verkort of verleng de grootte van een bestand naar de opgegeven grootte.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html>.

- Stel een grootte van 10 GB in voor een bestaand bestand, of maak een nieuw bestand met de opgegeven grootte:

`truncate {{[-s|--size]}} 10G {{pad/naar/bestand}}`

- Verleng de bestandsgrootte met 50 MiB, vul met gaten (die lezen als null bytes):

`truncate {{[-s|--size]}} +50M {{pad/naar/bestand}}`

- Verkort het bestand met 2 GiB door gegevens van het einde van het bestand te verwijderen:

`truncate {{[-s|--size]}} -2G {{pad/naar/bestand}}`

- Leeg de inhoud van het bestand:

`truncate {{[-s|--size]}} 0 {{pad/naar/bestand}}`

- Leeg de inhoud van het bestand, maar maak het bestand niet aan als het niet bestaat:

`truncate {{[-s|--size]}} 0 {{[-c|--no-create]}} {{pad/naar/bestand}}`
