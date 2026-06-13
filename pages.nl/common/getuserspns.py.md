# GetUserSPNs.py

> Haal Service Principal Names (SPN's) op die gekoppeld zijn aan Active Directory gebruikersaccounts.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Som gebruikersaccounts met een SPN op en vraag hun Kerberos TGS tickets op:

`GetUserSPNs.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}} -dc-ip {{domain_controller_ip}}`

- Gebruik pass-the-hash authenticatie:

`GetUserSPNs.py {{domein}}/{{gebruikersnaam}} -hashes {{LM_Hash}}:{{NT_Hash}} -dc-ip {{domain_controller_ip}}`

- Sla de uitvoer op in een bestand:

`GetUserSPNs.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}} -dc-ip {{domain_controller_ip}} -outputfile {{pad/naar/uitvoerbestand}}`

- Vraag alleen TGS tickets op:

`GetUserSPNs.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}} -dc-ip {{domain_controller_ip}} -request`

- Vraag alleen TGS tickets aan met pass-the-hash authenticatie:

`GetUserSPNs.py {{domein}}/{{gebruikersnaam}} -dc-ip {{domain_controller_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} -request`
