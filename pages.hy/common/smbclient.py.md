# smbclient.py

> Փոխազդել SMB սերվերների հետ:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Միացեք SMB սերվերին օգտվողի անունով և գաղտնաբառով.:

`smbclient.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Միացեք՝ օգտագործելով NTLM հեշերը նույնականացման համար.:

`smbclient.py -hashes {{LM_HASH}}:{{NT_HASH}} {{domain}}/{{username}}@{{target}}`

- Միացեք Kerberos վավերացման միջոցով.:

`smbclient.py -k {{domain}}/{{username}}@{{target}}`

- Միացեք՝ նշելով տիրույթի վերահսկիչի IP.:

`smbclient.py -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}@{{target}}`

- NetBIOS անվան փոխարեն միացեք կոնկրետ թիրախային IP-ին.:

`smbclient.py -target-ip {{target_ip}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Միացեք ոչ ստանդարտ SMB պորտին.:

`smbclient.py -port {{port}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Կատարեք հրամաններ մուտքագրված ֆայլից SMB shell-ում.:

`smbclient.py -inputfile {{path/to/input_file}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Մուտքագրեք SMB հաճախորդի հրամանները ելքային ֆայլում.:

`smbclient.py -outputfile {{path/to/output_file}} {{domain}}/{{username}}:{{password}}@{{target}}`
