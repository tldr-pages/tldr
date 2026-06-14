# secretsdump.py

> Թափել NTLM հեշերը, պարզ տեքստի գաղտնաբառերը և տիրույթի հավատարմագրերը հեռավոր Windows համակարգերից:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Թափել հավատարմագրերը Windows սարքից՝ օգտագործելով օգտվողի անուն և գաղտնաբառ.:

`secretsdump.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Թափել հեշերը մեքենայից՝ օգտագործելով pass-the-hash վավերացում.:

`secretsdump.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}@{{target}}`

- Թափել հավատարմագրերը Active Directory-ի NTDS.dit ֆայլից.:

`secretsdump.py -just-dc {{domain}}/{{username}}:{{password}}@{{target}}`

- Քաղեք հավատարմագրերը տեղական SAM տվյալների բազայից՝ օգտագործելով ռեեստրի փեթակները.:

`secretsdump.py -sam {{path/to/SAM}} -system {{path/to/SYSTEM}}`

- Թափել հեշերը սարքից՝ առանց գաղտնաբառ տրամադրելու (եթե գոյություն ունի վավերացման վավերական նիստ, օրինակ՝ Kerberos-ի կամ NTLM SSO-ի միջոցով):

`secretsdump.py -no-pass {{domain}}/{{username}}@{{target}}`
