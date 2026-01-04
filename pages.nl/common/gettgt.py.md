# getTGT.py

> Verzoek een Ticket Granting Ticket (TGT).
> Onderdeel van de Impacket suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Verzoek een TGT met behulp van een wachtwoord:

`getTGT.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`

- Verzoek een TGT met behulp van NTLM hashes:

`getTGT.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domein}}/{{gebruikersnaam}}`

- Gebruik Kerberos authenticatie (van bestaande cache, geen wachtwoord nodig):

`getTGT.py -k -no-pass {{domein}}/{{gebruikersnaam}}`

- Verzoek een TGT met behulp van een AES key (128 of 256 bits):

`getTGT.py -aesKey {{aes_key}} {{domein}}/{{gebruikersnaam}}`

- Specificeer een domain controller IP:

`getTGT.py -dc-ip {{domain_controller_ip}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`

- Vraag direct een serviceticket aan (AS-REQ) voor een specifieke SPN:

`getTGT.py -service {{SPN}} {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}`
