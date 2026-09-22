# DumpNTLMInfo.py

> Voer NTLM-authenticatie uit tegen een externe host zonder inloggegevens en dump informatie die is gelekt in het NTLMSSP-bericht.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Dump NTLM-informatie van het doel (SMB, standaard poort 445):

`DumpNTLMInfo.py {{doel}}`

- Dump NTLM-informatie met behulp van een specifiek IP:

`DumpNTLMInfo.py -target-ip {{doel_ip}} {{doel}}`

- Specificeer een aangepaste poort:

`DumpNTLMInfo.py -port {{poort}} {{doel}}`

- Dump NTLM-informatie met behulp van het RPC-protocol (standaard poort 135):

`DumpNTLMInfo.py -protocol RPC -port 135 {{doel}}`

- Schakel debug-uitvoer in:

`DumpNTLMInfo.py -debug {{doel}}`
