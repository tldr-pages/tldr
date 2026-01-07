# addcomputer.py

> Voeg een computeraccount toe aan het domein.
> Onderdeel van de Impacket suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Voeg een computer toe met een specifieke naam en wachtwoord:

`addcomputer.py -computer-name {{COMPUTER_NAAM$}} -computer-pass {{computer_wachtwoord}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`

- Stel alleen een nieuw wachtwoord in op een bestaande computer:

`addcomputer.py -no-add -computer-name {{COMPUTER_NAAM$}} -computer-pass {{computer_wachtwoord}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`

- Verwijder een bestaand computeraccount:

`addcomputer.py -delete -computer-name {{COMPUTER_NAAM$}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`

- Voeg een computer toe met behulp van Kerberos authenticatie:

`addcomputer.py -k -no-pass {{domein}}/{{gebruikersnaam}}@{{hostnaam}}`

- Voeg een computer toe via LDAPS (poort 636) in plaats van SAMR (poort 445):

`addcomputer.py -method LDAPS -port 636 {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`

- Geef de exacte domeincontroller op als er meerdere DC's bestaan:

`addcomputer.py -dc-host {{hostnaam}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`
