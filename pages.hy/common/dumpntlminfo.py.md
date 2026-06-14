# DumpNTLMIinfo.py

> Կատարեք NTLM նույնականացում հեռավոր հոսթի դեմ՝ առանց հավատարմագրերի և NTLMSSP հաղորդագրության մեջ արտահոսած տեղեկատվության արտահոսքի:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Թափել NTLM տեղեկատվությունը թիրախից (SMB, լռելյայն պորտ 445):

`DumpNTLMInfo.py {{target}}`

- Թափել NTLM տեղեկատվությունը՝ օգտագործելով հատուկ IP.:

`DumpNTLMInfo.py -target-ip {{target_ip}} {{target}}`

- Նշեք հատուկ նավահանգիստ.:

`DumpNTLMInfo.py -port {{port}} {{target}}`

- Թափել NTLM տեղեկատվությունը՝ օգտագործելով RPC արձանագրությունը (կանխադրված նավահանգիստ 135):

`DumpNTLMInfo.py -protocol RPC -port 135 {{target}}`

- Միացնել վրիպազերծման ելքը.:

`DumpNTLMInfo.py -debug {{target}}`
