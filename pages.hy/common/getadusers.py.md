# GetADUsers.py

> Առբերեք օգտատերերի ցուցակը Active Directory-ից, ներառյալ այնպիսի ատրիբուտներ, ինչպիսիք են մուտքի վերջին ժամադրոշմը և էլ.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Թվարկեք Active Directory-ի բոլոր օգտվողներին և նրանց ատրիբուտները.:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}`

- Առբերեք տեղեկատվություն միայն որոշակի օգտվողի համար.:

`GetADUsers.py -user {{user}} -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}`

- Քաղեք օգտվողի տվյալները՝ օգտագործելով pass-the-hash վավերացում.:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}`

- Պահպանեք արդյունքը ֆայլում.:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}} > {{path/to/output.txt}}`
