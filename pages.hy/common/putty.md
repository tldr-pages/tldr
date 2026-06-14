#ծեփամածիկ

> SSH, Telnet և Rlogin հաճախորդ՝ հեռավոր սերվերներին միանալու համար:.
> Նշում. Linux-ում բնիկ `ssh` հաճախորդը հաճախ ավելի հարմար է: PuTTY-ն ավելի հաճախ օգտագործվում է Windows-ում:.
> Լրացուցիչ տեղեկություններ. <https://the.earth.li/~sgtatham/putty/latest/htmldoc/Chapter3.html#using-cmdline>:.

- Միացեք հեռավոր հոսթին SSH-ի միջոցով.:

`putty -ssh {{username}}@{{hostname_or_ip}}`

- Միացեք հեռավոր հոսթին որոշակի [P] պորտի վրա.:

`putty -ssh {{username}}@{{hostname_or_ip}} -P {{port}}`

- Բեռնել պահպանված նստաշրջանը.:

`putty -load {{session_name}}`

- Միացեք անձնական բանալիով նույնականացման համար.:

`putty -ssh {{username}}@{{hostname_or_ip}} -i {{path/to/private_key.ppk}}`

- Միացեք Telnet-ի միջոցով.:

`putty -telnet {{hostname_or_ip}}`

- Միացնել [X]11 վերահասցեավորումը՝:

`putty -ssh {{username}}@{{hostname_or_ip}} -X`

- Կարգավորեք [L] տեղական նավահանգիստների վերահասցեավորումը.:

`putty -ssh {{username}}@{{hostname_or_ip}} -L {{local_port}}:{{destination_host}}:{{destination_port}}`

- Ցուցադրել օգնությունը.:

`putty -help`
