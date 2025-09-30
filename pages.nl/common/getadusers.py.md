# GetADUsers.py

> Haal een lijst met gebruikers op van Active Directory, inclusief attributen zoals laatste logon timestamp en email.
> Onderdeel van de Impacket suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Ga over alle Active Directory gebruikers en de attributen:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`

- Verkrijg informatie voor een specifieke gebruiker:

`GetADUsers.py -user {{gebruiker}} -dc-ip {{domain_controller_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`

- Extraheer gebruiksdetials door gebruik te maken van pass-the-hash authentication:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} {{domein}}/{{gebruikersnaam}}`

- Sla de output op in een bestand:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}} > {{pad/naar/output.txt}}`
