# mqtt_check.py

> Eenvoudig hulpprogramma voor het testen en valideren van MQTT aanmeldgegevens.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Controleer MQTT aanmeldingsgegevens voor een doel (hostnaam van de MQTT broker):

`mqtt_check.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel_naam}}`

- Geef een aangepaste client-ID op voor authenticatie:

`mqtt_check.py -client-id {{client_id}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel_naam}}`

- Schakel SSL in voor de verbinding:

`mqtt_check.py -ssl {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel_naam}}`

- Maak verbinding met een specifieke poort (standaard is 1883):

`mqtt_check.py -port {{port}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel_naam}}`

- Schakel debug-uitvoer in:

`mqtt_check.py -debug {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel_naam}}`

- Toon de help:

`mqtt_check.py --help`
