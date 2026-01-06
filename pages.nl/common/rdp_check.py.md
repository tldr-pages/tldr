# rdp_check.py

> Test of een account geldig is op de doelhost met het RDP-protocol (geen volledige aanmelding, alleen verificatiecontrole).
> Onderdeel van de Impacket suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Controleer of referenties geldig zijn op op een doel (wachtwoord wordt gevraagd indien weggelaten):

`rdp_check.py {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Controleer referenties met behulp van NTLM hashes:

`rdp_check.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Controleer referenties met expliciet wachtwoord:

`rdp_check.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Controleer referenties voor een lokaal account op een doel (geen domein):

`rdp_check.py {{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`
