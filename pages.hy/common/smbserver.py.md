# smbserver.py

> Հյուրընկալել SMB բաժնետոմսերը:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Ստեղծեք հիմնական SMB բաժնետոմս.:

`smbserver.py {{sharename}} {{path/to/share}}`

- Ստեղծեք համօգտագործում հատուկ մեկնաբանությամբ.:

`smbserver.py -comment {{my_share}} {{sharename}} {{path/to/share}}`

- Ստեղծեք համօգտագործում օգտվողի անվան և գաղտնաբառի նույնականացման միջոցով.:

`smbserver.py -username {{username}} -password {{password}} {{sharename}} {{path/to/share}}`

- Ստեղծեք բաժնետոմս NTLM հեշ վավերացման միջոցով.:

`smbserver.py -hashes {{LMHASH}}:{{NTHASH}} {{sharename}} {{path/to/share}}`

- Ստեղծեք բաժնետոմս հատուկ ինտերֆեյսի վրա.:

`smbserver.py {{[-ip|--interface-address]}} {{interface_ip_address}} {{sharename}} {{path/to/share}}`

- Ստեղծեք բաժնետոմս ոչ ստանդարտ SMB պորտի վրա.:

`smbserver.py -port {{port}} {{sharename}} {{path/to/share}}`

- Ստեղծեք համօգտագործում SMB2 աջակցությամբ.:

`smbserver.py -smb2support {{sharename}} {{path/to/share}}`

- Ստեղծեք բաժնետոմս և մուտքագրեք հրամաններ ելքային ֆայլում.:

`smbserver.py -outputfile {{path/to/output_file}} {{sharename}} {{path/to/share}}`
