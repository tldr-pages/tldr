# sniff.py

> Leg netwerkpakketten vast en geef weer met de `pcapy` bibliotheek.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Maak een lijst van beschikbare netwerkinterfaces en selecteer er een om te beginnen met het vastleggen van pakketten (vereist `sudo`):

`sudo sniff.py`

- Leg pakketten vast en sla uitvoer op in een bestand terwijl het op de terminal wordt weergegeven:

`sudo sniff.py | sudo tee {{pad/naar/uitvoerbestand}}`
