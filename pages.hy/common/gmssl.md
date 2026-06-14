# gmssl

> Crypto գործիքակազմ, որն աջակցում է SM1, SM2, SM3, SM4, SM9 և ZUC/ZUC256:.
> Լրացուցիչ տեղեկություններ. <http://gmssl.org/english.html>:.

- Ստեղծեք SM3 հեշ ֆայլի համար.:

`gmssl sm3 {{path/to/file}}`

- Գաղտնագրեք ֆայլը, օգտագործելով SM4 ծածկագիրը.:

`gmssl sms4 -e -in {{path/to/file}} -out {{path/to/file.sms4}}`

- գաղտնազերծել ֆայլը՝ օգտագործելով SM4 ծածկագիրը.:

`gmssl sms4 -d -in {{path/to/file.sms4}}`

- Ստեղծեք SM2 մասնավոր բանալի.:

`gmssl sm2 -genkey -out {{path/to/file.pem}}`

- Ստեղծեք SM2 հանրային բանալի գոյություն ունեցող մասնավոր բանալիից.:

`gmssl sm2 -pubout -in {{path/to/file.pem}} -out {{path/to/file.pem.pub}}`

- Գաղտնագրեք ֆայլը՝ օգտագործելով ZUC ծածկագիրը.:

`gmssl zuc -e -in {{path/to/file}} -out {{path/to/file.zuc}}`

- Ֆայլի վերծանումը՝ օգտագործելով ZUC ծածկագիրը.:

`gmssl zuc -d -in {{path/to/file.zuc}}`

- Ցուցադրման տարբերակը:

`gmssl version`
