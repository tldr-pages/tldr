# addcomputer.py

> Ավելացնել համակարգչային հաշիվ տիրույթում:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Ավելացնել համակարգիչ հատուկ անունով և գաղտնաբառով.:

`addcomputer.py -computer-name {{COMPUTER_NAME$}} -computer-pass {{computer_password}} {{domain}}/{{username}}:{{password}}`

- Սահմանեք նոր գաղտնաբառ միայն գոյություն ունեցող համակարգչում.:

`addcomputer.py -no-add -computer-name {{COMPUTER_NAME$}} -computer-pass {{computer_password}} {{domain}}/{{username}}:{{password}}`

- Ջնջել գոյություն ունեցող համակարգչային հաշիվը.:

`addcomputer.py -delete -computer-name {{COMPUTER_NAME$}} {{domain}}/{{username}}:{{password}}`

- Ավելացնել համակարգիչ՝ օգտագործելով Kerberos նույնականացումը.:

`addcomputer.py -k -no-pass {{domain}}/{{username}}@{{hostname}}`

- Ավելացնել համակարգիչ LDAPS-ի միջոցով (պորտ 636) SAMR-ի փոխարեն (պորտ 445):

`addcomputer.py -method LDAPS -port 636 {{domain}}/{{username}}:{{password}}`

- Նշեք ճշգրիտ տիրույթի վերահսկիչը, երբ կան բազմաթիվ DC-ներ.:

`addcomputer.py -dc-host {{hostname}} {{domain}}/{{username}}:{{password}}`
