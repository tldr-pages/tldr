# machine_role.py

> Bepaal de rol van een externe Windows-machine (bijv. domeincontroller, lidserver of werkstation).
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Bepaal de rol van een machine met een gebruikersnaam en wachtwoord:

`machine_role.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Bepaal de rol met behulp van pass-the-hash-authenticatie:

`machine_role.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Bepaal de rol zonder te vragen om een wachtwoord (bijv. met behulp van een bestaande sessie):

`machine_role.py -no-pass {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Bepaal de rol met behulp van Kerberos-authenticatie:

`machine_role.py -k {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Specificeer het IP-adres van de domeincontroller:

`machine_role.py -dc-ip {{ip_adres}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`
