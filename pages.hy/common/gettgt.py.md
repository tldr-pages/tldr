# getTGT.py

> Պահանջել Տոմսերի շնորհման տոմս (TGT):.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Խնդրեք TGT՝ օգտագործելով գաղտնաբառ.:

`getTGT.py {{domain}}/{{username}}:{{password}}`

- Խնդրեք TGT՝ օգտագործելով NTLM հեշեր.:

`getTGT.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}`

- Օգտագործեք Kerberos վավերացում (առկա ccache-ից, գաղտնաբառի կարիք չկա).:

`getTGT.py -k -no-pass {{domain}}/{{username}}`

- Խնդրեք TGT օգտագործելով AES բանալի (128 կամ 256 բիթ).:

`getTGT.py -aesKey {{aes_key}} {{domain}}/{{username}}`

- Նշեք տիրույթի վերահսկիչի IP.:

`getTGT.py -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}`

- Պահանջել սպասարկման տոմս ուղղակիորեն (AS-REQ) կոնկրետ SPN-ի համար.:

`getTGT.py -service {{SPN}} {{domain}}/{{username}}:{{password}}`
