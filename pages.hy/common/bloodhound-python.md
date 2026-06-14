# bloodhound-python

> Python ingestor BloodHound-ի համար, որն օգտագործվում է Active Directory-ի հարաբերությունները թվարկելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/dirkjanm/BloodHound.py#usage>:.

- Հավաքեք բոլոր տվյալները՝ օգտագործելով լռելյայն հավաքման մեթոդները (ներառյալ խմբերը, նիստերը և վստահությունները).:

`bloodhound-python --username {{username}} --password {{password}} --domain {{domain}}`

- Հավաքեք տվյալներ Kerberos վավերացման միջոցով՝ առանց պարզ տեքստի գաղտնաբառ պահանջելու.:

`bloodhound-python --collectionmethod {{All}} --kerberos --domain {{domain}}`

- Նույնականացրեք՝ օգտագործելով NTLM հեշերը՝ գաղտնաբառի փոխարեն.:

`bloodhound-python --collectionmethod {{All}} --username {{username}} --hashes {{LM:NTLM}} --domain {{domain}}`

- Նշեք հատուկ անվանման սերվեր DNS հարցումների համար.:

`bloodhound-python --collectionmethod {{All}} --username {{username}} --password {{password}} --domain {{domain}} --nameserver {{nameserver}}`

- Պահպանեք ելքային ֆայլերը որպես սեղմված ZIP արխիվ.:

`bloodhound-python --collectionmethod {{All}} --username {{username}} --password {{password}} --domain {{domain}} --zip`
