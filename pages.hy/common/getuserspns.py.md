# GetUserSPNs.py

> Ստացեք ծառայության հիմնական անունները (SPN), որոնք կապված են Active Directory օգտվողների հաշիվների հետ:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Թվարկեք օգտվողների հաշիվները SPN-ով և խնդրեք նրանց Kerberos TGS տոմսերը.:

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}}`

- Օգտագործեք «pas-the-hash» վավերացում.:

`GetUserSPNs.py {{domain}}/{{username}} -hashes {{LM_Hash}}:{{NT_Hash}} -dc-ip {{domain_controller_ip}}`

- Պահպանեք արդյունքը ֆայլում.:

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}} -outputfile {{path/to/output_file}}`

- Պահանջեք միայն TGS տոմսեր.:

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}} -request`

- Խնդրեք միայն TGS տոմսեր՝ օգտագործելով pass-the-hash վավերացում.:

`GetUserSPNs.py {{domain}}/{{username}} -dc-ip {{domain_controller_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} -request`
