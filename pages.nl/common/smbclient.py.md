# smbclient.py

> Een op Python gebaseerde SMB-client voor interactie met SMB-servers.
> Meer informatie: <https://github.com/fortra/impacket>.

- Maak verbinding met een SMB server met gebruikersnaam en wachtwoord:

`smbclient.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Maak verbinding met NTLM hashes voor authenticatie:

`smbclient.py -hashes {{LM_HASH}}:{{NT_HASH}} {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Maak verbinding met Kerberos-authenticatie:

`smbclient.py -k {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Maak verbinding door een domeincontroller-IP op te geven:

`smbclient.py -dc-ip {{domein_controller_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Maak verbinding met een specifiek doel-IP in plaats van NetBIOS-naam:

`smbclient.py -target-ip {{doel_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Maak verbinding met een niet-standaard SMB-poort:

`smbclient.py -port {{port}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Voer opdrachten uit vanuit een invoerbestand in de SMB-shell:

`smbclient.py -inputfile {{pad/naar/invoerbestand}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Log SMB-clientopdrachten naar een uitvoerbestand:

`smbclient.py -outputfile {{pad/naar/uitvoerbestand}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`
