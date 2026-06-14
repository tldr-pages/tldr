# psexec.py

> Կատարեք հրամաններ հեռավոր Windows սարքի վրա՝ օգտագործելով `RemComSvc`՝ ապահովելով PsExec-ի նման գործառույթ:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Հեռավոր թիրախի վրա ստեղծել ինտերակտիվ պատյան.:

`psexec.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Կատարեք որոշակի հրաման հեռավոր թիրախի վրա.:

`psexec.py {{domain}}/{{username}}:{{password}}@{{target}} {{command}}`

- Պատճենեք ֆայլի անունը հետագա կատարման համար, արգումենտները փոխանցվում են հրամանում.:

`psexec.py -c {{filename}} {{domain}}/{{username}}:{{password}}@{{target}} {{command}}`

- Կատարեք հրաման հեռավոր թիրախի վրա կոնկրետ ճանապարհից.:

`psexec.py -path {{path}} {{domain}}/{{username}}:{{password}}@{{target}} {{command}}`

- Նույնականացրեք՝ օգտագործելով «pas-the-hash» նույնականացումը՝ գաղտնաբառի փոխարեն.:

`psexec.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}@{{target}}`

- Օգտագործեք Kerberos նույնականացումը թիրախի համար.:

`psexec.py -k -no-pass {{domain}}/{{username}}@{{target}}`

- Նշեք տիրույթի վերահսկիչի IP հասցեն.:

`psexec.py -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}@{{target}}`
