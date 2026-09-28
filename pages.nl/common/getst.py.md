# getST.py

> Verzoek een Kerberos Service Ticket (TGS).
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Verzoek een service ticket voor een specifieke SPN:

`getST.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}} -spn {{service}}/{{doel}}`

- Verzoek een ticket met behulp van NTLM hashes (pass-the-hash):

`getST.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domein}}/{{gebruikersnaam}} -spn {{service}}/{{doel}}`

- Verzoek een ticket met behulp van een bestaand Kerberos ccache-bestand:

`getST.py -no-pass -k {{domein}}/{{gebruikersnaam}} -spn {{service}}/{{doel}}`

- Imiteer een andere gebruiker via S4U2Self (vereist delegatierechten):

`getST.py -k -impersonate {{doel_gebruiker}} {{domein}}/{{gebruikersnaam}} -spn {{service}}/{{doel}}`

- Forceer dat het ticket forwardable is (Bronze Bit):

`getST.py -force-forwardable -k {{domein}}/{{gebruikersnaam}} -spn {{service}}/{{doel}}`
