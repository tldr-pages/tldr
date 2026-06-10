# getST.py

> Պահանջել Kerberos ծառայության տոմս (TGS):.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Պահանջել սպասարկման տոմս հատուկ SPN-ի համար.:

`getST.py {{domain}}/{{username}}:{{password}} -spn {{service}}/{{target}}`

- Հայցեք տոմս՝ օգտագործելով NTLM հեշեր (pass-the-hash):

`getST.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}} -spn {{service}}/{{target}}`

- Պահանջեք տոմս՝ օգտագործելով Kerberos ccache ֆայլը.:

`getST.py -no-pass -k {{domain}}/{{username}} -spn {{service}}/{{target}}`

- S4U2Self-ի միջոցով նմանակել մեկ այլ օգտատիրոջ (պահանջում է պատվիրակության իրավունքներ).:

`getST.py -k -impersonate {{target_user}} {{domain}}/{{username}} -spn {{service}}/{{target}}`

- Ստիպեք տոմսը փոխանցելի (բրոնզե բիթ).:

`getST.py -force-forwardable -k {{domain}}/{{username}} -spn {{service}}/{{target}}`
