# rpcdump.py

> Informatie over RPC-eindpunten op afstand dumpen via de Endpoint Mapper.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Dump RPC eindpunten met gebruikersnaam en wachtwoord:

`rpcdump.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Dump RPC eindpunten met NTLM hashes:

`rpcdump.py -hashes {{LMHASH}}:{{NTHASH}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Geef expliciet een doel-IP-adres op (handig als de doelnaam een NetBIOS-naam is):

`rpcdump.py -target-ip {{doel_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Maak verbinding met een specifieke poort (standaard is 135 voor RPC Endpoint Mapper):

`rpcdump.py -port {{poort_nummer}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Schakel debug-uitvoer in:

`rpcdump.py -debug {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`
