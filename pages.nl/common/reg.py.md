# reg.py

> Query, voeg toe, verwijder, sla op, of maak back-ups van registersleutels/-waarden op een externe Windows-machine via SMB/RPC.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Bevraag subsleutels en waarden onder een registerpad:

`reg.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} query -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}'`

- Bevraag recursief alle subsleutels en waarden onder een registerpad:

`reg.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} query -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}' -s`

- Voeg een nieuwe registersleutel of -waarde toe (standaard waardetype is `REG_SZ`):

`reg.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} add -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}' -v {{waarde_naam}} -vt {{REG_SZ|REG_NONE|REG_EXPAND_SZ|REG_BINARY|REG_DWORD|REG_DWORD_BIG_ENDIAN|REG_LINK|REG_MULTI_SZ|REG_QWORD}} -vd {{waarde_data}}`

- Verwijder een registersleutel of -waarde:

`reg.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} delete -keyName '{{HKLM\SOFTWARE\Example}}' -v {{waarde_naam}}`

- Sla een registersleutel (en subsleutels) op in een bestand op het doel via een UNC-pad:

`reg.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} save -keyName '{{HKLM\SOFTWARE\Example}}' -o '\\{{doel}}\{{share}}\{{output_bestand.reg}}'`

- Maak een back-up van de SAM-, SYSTEM- en SECURITY-hives naar een bestand op een doel via een UNC-pad (vereist SYSTEM-rechten):

`reg.py {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}} backup -o '\\{{doel}}\{{share}}'`
