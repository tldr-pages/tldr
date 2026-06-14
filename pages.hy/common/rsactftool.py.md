# RsaCtfTool.py

> RSA հարձակման գործիք CTF մարտահրավերների համար. վերականգնել մասնավոր բանալիները թույլ հանրային բանալիներից և/կամ վերծանել տվյալները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/RsaCtfTool/RsaCtfTool#usage>:.

- Վերականգնել մասնավոր բանալին հանրային բանալի ֆայլից.:

`RsaCtfTool.py --publickey {{path/to/key.pub}} --private`

- գաղտնազերծել ֆայլը հանրային բանալին օգտագործելով.:

`RsaCtfTool.py --publickey {{path/to/key.pub}} --decryptfile {{path/to/ciphered_file}}`

- Գաղտնազերծեք հատուկ ծածկագրային տեքստի տողը.:

`RsaCtfTool.py --publickey {{path/to/key.pub}} --decrypt "{{ciphertext}}"`

- Թափել RSA հիմնական բաղադրիչները (օրինակ՝ մոդուլը, ցուցիչը) առանցքային ֆայլից.:

`RsaCtfTool.py --dumpkey --key {{path/to/key.pub}}`

- Գործարկել հատուկ հարձակում (օրինակ՝ Fermat factorization)՝ մասնավոր բանալին վերականգնելու համար.:

`RsaCtfTool.py --publickey {{path/to/key.pub}} --private --attack fermat`

- Ստեղծեք հանրային բանալին մոդուլից (n) և ցուցիչից (e):

`RsaCtfTool.py --createpub -n {{modulus}} -e {{exponent}}`

- Փորձեք բոլոր հասանելի հարձակումները վերականգնելու անձնական բանալին.:

`RsaCtfTool.py --publickey {{path/to/key.pub}} --private --attack all`
