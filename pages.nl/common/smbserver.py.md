# smbserver.py

> Een op Python gebaseerde SMB-server voor het hosten van shares (root vereist voor poort 445).
> Meer informatie: <https://github.com/fortra/impacket>.

- Stel een basis SMB share in:

`smbserver.py {{share_naam}} {{pad/naar/share}}`

- Stel een share in met een aangepast commentaar:

`smbserver.py -commentaar {{my_share}} {{share_naam}} {{pad/naar/share}}`

- Stel een share in met gebruikersnaam en wachtwoord verificatie:

`smbserver.py -username {{gebruikersnaam}} -password {{password}} {{share_naam}} {{pad/naar/share}}`

- Stel een share in met NTLM hash-authenticatie:

`smbserver.py -hashes {{LMHASH}}:{{NTHASH}} {{share_naam}} {{pad/naar/share}}`

- Stel een share in op een specifieke interface:

`smbserver.py {{[-ip|--interface-address]}} {{interface_ip_address}} {{share_naam}} {{pad/naar/share}}`

- Stel een share in op een niet-standaard SMB-poort:

`smbserver.py -port {{port}} {{share_naam}} {{pad/naar/share}}`

- Stel een share in met SMB2 ondersteuning:

`smbserver.py -smb2support {{share_naam}} {{pad/naar/share}}`

- Stel een share in en log de commando's in een uitvoerbestand:

`smbserver.py -outputfile {{pad/naar/uitvoerbestand}} {{share_naam}} {{pad/naar/share}}`
